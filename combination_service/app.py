from flask_restx import Api, Namespace, Resource
from flask import Flask, Response, request
import random, time
import py_eureka_client.eureka_client as eureka_client
from flask_jwt_extended import *
from pymongo import MongoClient
from config import Config
from bson.objectid import ObjectId
from bson.json_util import dumps
from recommendation import return_list, linear_regression
from get_combination_impl import return_id_list, budget_cut_list, return_as_dict, send_to_mongo, send_to_mongo_nocelery

#Prometheus
from prometheus_client import REGISTRY, Counter, Gauge, Histogram, generate_latest
from prometheus_flask_exporter import PrometheusMetrics, RESTfulPrometheusMetrics

#Caching
from flask_caching import Cache


# Register Eureka
eureka_client.init(
                    eureka_server="http://localhost:8761/eureka",
                    app_name="flask-service", 
                    instance_port=Config.FLASK_PORT,
                    )

# Grafana Setting
REQUESTS = Counter('http_requests_total', 'Total HTTP Requests (count)', ['method', 'endpoint', 'status_code'])
IN_PROGRESS = Gauge('http_requests_inprogress', 'Number of in progress HTTP requests')
TIMINGS = Histogram('http_request_duration_seconds', 'HTTP request latency (seconds)')
COMBINATION_GENERATION = Counter('combination_generation','Combination Generation Number', ['combination_no'])

REQUESTS_CACHED = Counter('http_requests_total_cached', 'Total HTTP Requests (count)', ['method', 'endpoint', 'status_code'])
IN_PROGRESS_CACHED = Gauge('http_requests_inprogress_cached', 'Number of in progress HTTP requests')
TIMINGS_CACHED = Histogram('http_request_duration_seconds_cached', 'HTTP request latency (seconds)')
COMBINATION_GENERATION_CACHED = Counter('combination_generation_cached','Combination Generation Number', ['combination_no'])

#Initiate Cache as global variable for namespaces
cache = Cache()
counter = Counter('total_number_counter','Used to divide cache hitrate')
cache_hit = Counter('cache_hit','Number of Cache Hits')

# App Factory
def create_app(): 

    # app = Flask(__name__)
    app1 = Flask(__name__)
    app1.config.from_object(Config)

    cache.init_app(app1)
    jwt = JWTManager(app1)
    
    # API Server Setting
    api_server = Api(
        app1,
        version='0.10',
        title="Roombi Combination API",
        description="Furniture Combination Generator",
    )

    # API URL: /combination/getcombination
    api_server.add_namespace(GetCombination, '/combination')


    #Prometheus Setting
    metrics = RESTfulPrometheusMetrics(app1, api_server)
    metrics.info('roombi_combi', 'Service of Combination Generation', version='1.0.0')


    @app1.route('/hello')
    # @jwt_required
    def hello():
        # jwt_validity = get_jwt_identity()
        jwt_validity = 1
        if jwt_validity is None:
            return "User Only!"
        else:
            return "Hello"

    #Find Combination by Combination UUID
    @app1.route('/<string:id>')
    @cache.cached(timeout=300)
    def find(id):
        client = MongoClient('mongodb://{}:{}@localhost:27017/'.format(Config.MONGODB_USER,Config.MONGODB_PASSWORD))
        db = client.roombi_combination
        collection = db.combination_log
        
        # Insert ID_list to Combination Log
        data = collection.find_one({'_id': ObjectId(id)})
        return dumps(data)


    #Prometheus Metric Collection
    @app1.route('/metrics')
    @metrics.do_not_track()
    def metrics():
        return Response(generate_latest(REGISTRY))

    return app1

GetCombination = Namespace(name="GetCombination", description="Combination Generator. Returns a list of furniture combination with designated user preference.",)

@GetCombination.route('/getcombination')
class GetCombinationPost(Resource):

    @TIMINGS.time()
    @IN_PROGRESS.track_inprogress()
    # @COMBINATION_GENERATION
    def post(self):
        # jwt_validity = get_jwt_identity()
        jwt_validity = 1
        if jwt_validity is None:
            return "User Only!"
        else:
            """Input: json{user_id, furniture_combination, user_color, money(budget)}"""
            user_preference = {}
            user_preference['furniture_combination'] = request.json.get('furniture preference')
            user_preference['user_color'] = request.json.get('color preference')
            budget = request.json.get('money')
            user_id = request.json.get('user_id')   

            for i,k in enumerate(user_preference['user_color']):
                user_preference['user_color'][i] -= 1   

            # Return Combination Result
            final_list = return_list(user_preference)

            # Return Linear Regression Measurement
            final_list = linear_regression(final_list)   

            # Change the result into Furniture ID list 
            final_id_list = return_id_list(final_list,user_id) 

            # Celery unsynchronized MongoDB query
            send_to_mongo(final_id_list)

            # Budget Cut of Combinations
            final_id_list_with_budget = budget_cut_list(final_id_list,budget)   

            #Return result as JSON format
            if final_id_list_with_budget:
                # Convert List to Dictionary(JSON type)                
                final_id_list_with_budget = return_as_dict(final_id_list_with_budget) 

                #Prometheus Metrics
                REQUESTS.labels(method='POST', endpoint="/getcombination", status_code=200).inc()
                COMBINATION_GENERATION.labels(combination_no='created').inc()

                return final_id_list_with_budget[0:Config.NUMBER_OF_RETURN_LIST+1], 200 
                
            else:    
                #Prometheus Metrics
                REQUESTS.labels(method='POST', endpoint="/getcombination", status_code=204).inc()
                COMBINATION_GENERATION.labels(combination_no='not created').inc()

                return None, 204

@GetCombination.route('/getcombination_no_celery')
class GetCombinationPostNoCelery(Resource):

    @TIMINGS.time()
    @IN_PROGRESS.track_inprogress()
    # @COMBINATION_GENERATION
    def post(self):
        # jwt_validity = get_jwt_identity()
        jwt_validity = 1
        if jwt_validity is None:
            return "User Only!"
        else:
            """Input: json{user_id, furniture_combination, user_color, money(budget)}"""
            user_preference = {}
            user_preference['furniture_combination'] = request.json.get('furniture preference')
            user_preference['user_color'] = request.json.get('color preference')
            budget = request.json.get('money')
            user_id = request.json.get('user_id')   

            for i,k in enumerate(user_preference['user_color']):
                user_preference['user_color'][i] -= 1   

            # Return Combination Result
            final_list = return_list(user_preference)

            # Return Linear Regression Measurement
            final_list = linear_regression(final_list)   

            # Change the result into Furniture ID list 
            final_id_list = return_id_list(final_list,user_id) 

            # Celery unsynchronized MongoDB query
            send_to_mongo_nocelery(final_id_list)

            # Budget Cut of Combinations
            final_id_list_with_budget = budget_cut_list(final_id_list,budget)   

            #Return result as JSON format
            if final_id_list_with_budget:
                # Convert List to Dictionary(JSON type)                
                final_id_list_with_budget = return_as_dict(final_id_list_with_budget) 

                #Prometheus Metrics
                REQUESTS.labels(method='POST', endpoint="/getcombination", status_code=200).inc()
                COMBINATION_GENERATION.labels(combination_no='created').inc()

                return final_id_list_with_budget[0:Config.NUMBER_OF_RETURN_LIST+1], 200 
                
            else:    
                #Prometheus Metrics
                REQUESTS.labels(method='POST', endpoint="/getcombination", status_code=204).inc()
                COMBINATION_GENERATION.labels(combination_no='not created').inc()

                return None, 204


@GetCombination.route('/getcombination_cached')
class GetCombinationPostCached(Resource):
    
    @TIMINGS.time()
    @IN_PROGRESS.track_inprogress()
    def post(self):

        # jwt_validity = get_jwt_identity()
        jwt_validity = 1
        if jwt_validity is None:
            return "User Only!"
        else:
            """Input: json{user_id, furniture_combination, user_color, money(budget)}"""
            user_preference = {}
            user_preference['furniture_combination'] = request.json.get('furniture preference')
            user_preference['user_color'] = request.json.get('color preference')
            budget = request.json.get('money')
            user_id = request.json.get('user_id')   
            

            for i,k in enumerate(user_preference['user_color']):
                user_preference['user_color'][i] -= 1   

            ##  Apply Caching
            # key = furniture category choices + # + color choices
            redis_key = ''.join(map(str, user_preference['furniture_combination'])) + '#' +''.join(map(str, user_preference['user_color']))
            cache_data = cache.get(redis_key)

            if cache_data:
                final_id_list = cache_data
                cache_hit.inc()
            else:
                # Return Combination Result
                final_list = return_list(user_preference)

                # Return Linear Regression Measurement
                final_list = linear_regression(final_list)   

                # Change the result into Furniture ID list 
                final_id_list = return_id_list(final_list,user_id)

                send_to_mongo(final_id_list)

                # Save Algorithm Result to Redis Cache
                cache.set(redis_key,final_id_list)  
                
            # Budget Cut of Combinations
            final_id_list_with_budget = budget_cut_list(final_id_list,budget)   

            counter.inc()
            #Return result as JSON format
            if final_id_list_with_budget:
                # Convert List to Dictionary(JSON type)
                final_id_list_with_budget = return_as_dict(final_id_list_with_budget) 

                #Prometheus Metrics
                REQUESTS.labels(method='POST', endpoint="/getcombination", status_code=200).inc()
                COMBINATION_GENERATION.labels(combination_no='created').inc()

                
                final_result = final_id_list_with_budget[0:Config.NUMBER_OF_RETURN_LIST+1]

                # Save Result to Redis Cache
                return final_result, 200 
                
            else:    
                #Prometheus Metrics
                REQUESTS.labels(method='POST', endpoint="/getcombination", status_code=204).inc()
                COMBINATION_GENERATION.labels(combination_no='not created').inc()

                return None, 204


if __name__ == "__main__":
    app1 = create_app()
    app1.run(debug=False, host='0.0.0.0', port=Config.FLASK_PORT)

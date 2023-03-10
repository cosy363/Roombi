from flask import request, Response, Flask
from flask_jwt_extended import *

# flask_restx 관련 class import 
from flask_restx import Resource, Namespace

#Prometheus 설정
from prometheus_client import REGISTRY, Counter, Gauge, Histogram, generate_latest, Summary

from recommendation import return_list, linear_regression
from get_combination_impl import return_id_list, budget_cut_list, return_as_dict
from config import Config

# Primitive Time Counter
import time
import random


# Grafana Setting
REQUESTS = Counter('http_requests_total', 'Total HTTP Requests (count)', ['method', 'endpoint', 'status_code'])
IN_PROGRESS = Gauge('http_requests_inprogress', 'Number of in progress HTTP requests')
TIMINGS = Histogram('http_request_duration_seconds', 'HTTP request latency (seconds)')
COMBINATION_GENERATION = Counter('combination_generation','Combination Generation Number', ['combination_no'])

REQUESTS_CACHED = Counter('http_requests_total_cached', 'Total HTTP Requests (count)', ['method', 'endpoint', 'status_code'])
IN_PROGRESS_CACHED = Gauge('http_requests_inprogress_cached', 'Number of in progress HTTP requests')
TIMINGS_CACHED = Histogram('http_request_duration_seconds_cached', 'HTTP request latency (seconds)')
COMBINATION_GENERATION_CACHED = Counter('combination_generation_cached','Combination Generation Number', ['combination_no'])

# namespace 설정 추가
GetCombination = Namespace(name="GetCombination", description="Combination Generator. Returns a list of furniture combination with designated user preference.",)

from flask_caching import Cache
from flask import current_app
from app import app1

app_cache = Cache(app1)

# namespace 객체 함수명으로 route
# 매개변수로 Resource 추가
@GetCombination.route('/getcombination')
class GetCombinationPost(Resource):

    @TIMINGS.time()
    @IN_PROGRESS.track_inprogress()
    # @COMBINATION_GENERATION
    @app_cache.cached(timeout=500)
    def post(self):
        print("working...")
        # jwt_validity = get_jwt_identity()
        jwt_validity = 1
        if jwt_validity is None:
            return "User Only!"
        else:
            start = time.time()
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

            # Budget Cut of Combinations
            final_id_list_with_budget = budget_cut_list(final_id_list,budget)   

            # Convert List to Dictionary(JSON type)
            final_id_list_with_budget = return_as_dict(final_id_list_with_budget) 

            #Return result as JSON format
            if final_id_list_with_budget:
                #Prometheus Metrics
                REQUESTS.labels(method='POST', endpoint="/getcombination", status_code=200).inc()
                COMBINATION_GENERATION.labels(combination_no='created').inc()

                print("수행시간 = ",time.time()-start,"초")
                return final_id_list_with_budget[0:Config.NUMBER_OF_RETURN_LIST+1], 200 
                
            else:    
                #Prometheus Metrics
                REQUESTS.labels(method='POST', endpoint="/getcombination", status_code=204).inc()
                COMBINATION_GENERATION.labels(combination_no='not created').inc()

                print("수행시간 = ",time.time()-start,"초")
                return None, 204
    
@GetCombination.route('/getcombination_cached')
class GetCombinationPostCached(Resource):
    
    @TIMINGS_CACHED.time()
    @IN_PROGRESS_CACHED.track_inprogress()
    @app_cache.cached(timeout=300)
    def get(self):
        return random.randint(1,10)


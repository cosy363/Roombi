import json
from flask import request, make_response, jsonify
from flask_jwt_extended import *

# flask_restx 관련 class import 
from flask_restx import Resource, Namespace
from recommendation import return_list, linear_regression
from get_combination_impl import return_id_list, budget_cut_list, return_as_dict
# from prometheus_client import generate_latest, REGISTRY, Counter, Gauge, Histogram
from config import Config


#Setting
# REQUESTS = Counter('http_requests_total', 'Total HTTP Requests (count)', ['method', 'endpoint', 'status_code'])
# 
# IN_PROGRESS = Gauge('http_requests_inprogress', 'Number of in progress HTTP requests')
# 
# TIMINGS = Histogram('http_request_duration_seconds', 'HTTP request latency (seconds)')

# namespace 설정 추가
GetCombination = Namespace(name="GetCombination", description="Combination Generator. Returns a list of furniture combination with designated user preference.",)

# namespace 객체 함수명으로 route
# 매개변수로 Resource 추가
@GetCombination.route('/getcombination')
# @TIMINGS.time()
# @IN_PROGRESS.track_inprogress()
class GetCombinationPost(Resource):
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

            # Budget Cut of Combinations
            final_id_list_with_budget = budget_cut_list(final_id_list,budget)   

            # Convert List to Dictionary(JSON type)
            final_id_list_with_budget = return_as_dict(final_id_list_with_budget) 

            #Return result as JSON format
            if final_id_list_with_budget:
                return final_id_list_with_budget[0:Config.NUMBER_OF_RETURN_LIST+1], 200 
            else:    
                return None, 204
from flask import Flask
from flask_restx import Resource, Api, Namespace
from flask_cors import CORS
from flask import Flask, request, abort
from get_combination import GetCombination
import py_eureka_client.eureka_client as eureka_client
from flask_jwt_extended import *
from prometheus_client import generate_latest, REGISTRY, Counter, Gauge, Histogram
import config

port = 5000
# Register Eureka
# eureka_client.init(
#                     eureka_server="http://naming-service:8761/eureka",
#                     app_name="flask-service", 
#                     instance_port=port,
#                     )

# Instance 
app = Flask(__name__)

app.config.from_object(config.Config)

jwt = JWTManager(app)

# Prometheus Monitering

# API Server Setting
api_server = Api(
    app,
    version='0.10',
    title="Roombi Combination API",
    description="Furniture Combination Generator",
)

# API URL: /combination/getcombination
api_server.add_namespace(GetCombination, '/combination')

# Blocks Access from other IP
# @app.before_request
# def limit_remote_addr():
#     if request.remote_addr != '127.0.0.1':
#         print("No!!")
#         abort(403)  # Forbidden

@app.route('/hello')
# @jwt_required
def hello():
    # jwt_validity = get_jwt_identity()
    jwt_validity = 1
    if jwt_validity is None:
        return "User Only!"
    else:
        return "Hello"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=port)
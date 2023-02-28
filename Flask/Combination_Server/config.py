class Config(object):
    DEBUG = True
    FLASK_PORT= 5004
    #TOKEN
    JWT_SECRET_KEY = "user_token"
    #MYSQL CONNECTION SETTINGS
    MYSQL_IP = "127.0.0.1"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "0000"
    MYSQL_DB = "furniture_DB"
    # MYSQL_IP = "127.0.0.1/3306"
    # MYSQL_USER = "root"
    # MYSQL_PASSWORD = "kimjin12!"
    # MYSQL_DB = "furniture_DB"
    #MONGODB CONNECTION SETTINGS
    MONGODB_IP = "localhost:27017/"
    MONGODB_USER = "root"
    MONGODB_PASSWORD = "kimjin12!"
    MONGODB_COLLECTION = "combination_log"
    #NUMBER OF LIST RETURNS
    NUMBER_OF_RETURN_LIST = 20
    #Flask-Caching related configs
    CACHE_TYPE = "RedisCache"
    CACHE_DEFAULT_TIMEOUT = 720000
    CACHE_REDIS_URL="redis://127.0.0.1:7617/0"
    CACHE_REDIS_HOST= "127.0.0.1"
    CACHE_REDIS_PORT=7617
    CACHE_REDIS_DB=0    
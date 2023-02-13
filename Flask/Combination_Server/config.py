class Config(object):
    DEBUG = True
    #TOKEN
    JWT_SECRET_KEY = "user_token"
    #MYSQL CONNECTION SETTINGS
    MYSQL_IP = "database-1.cnxa3k5tfaa9.ap-northeast-2.rds.amazonaws.com"
    MYSQL_USER = "admin"
    MYSQL_PASSWORD = "kimjin12!"
    MYSQL_DB = "furniture_DB"
    #MONGODB CONNECTION SETTINGS
    MONGODB_IP = "localhost:27017/"
    MONGODB_USER = "root"
    MONGODB_PASSWORD = "kimjin12!"
    MONGODB_COLLECTION = "combination_log"
    #NUMBER OF LIST RETURNS
    NUMBER_OF_RETURN_LIST = 20
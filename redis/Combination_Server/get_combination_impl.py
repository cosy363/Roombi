from config import Config
from pymongo import MongoClient


def return_id_list(final_list_with_sum, user_id):
    id_list = []

    for i,a in enumerate(final_list_with_sum):
        for j,b in enumerate(final_list_with_sum[i]):
            for k,c in enumerate(final_list_with_sum[i][j]):
                for l,d in enumerate(final_list_with_sum[i][j][k]):
                    # pri = final_list_with_sum[i][j][k][l][0]['New_ID']
                    # sec = final_list_with_sum[i][j][k][l][1]['New_ID']
                    # thr = final_list_with_sum[i][j][k][l][2]['New_ID']
                    # fin = final_list_with_sum[i][j][k][l][3]['New_ID']
                    pri = final_list_with_sum[i][j][k][l][0]
                    sec = final_list_with_sum[i][j][k][l][1]
                    thr = final_list_with_sum[i][j][k][l][2]
                    fin = final_list_with_sum[i][j][k][l][3]
                    score_sum = final_list_with_sum[i][j][k][l][4]
                    price_sum = final_list_with_sum[i][j][k][l][5]
                    deep_score = final_list_with_sum[i][j][k][l][6]
                    total_score = final_list_with_sum[i][j][k][l][7]

                    # list = [int(pri),int(sec),int(thr),int(fin),float(score_sum),int(price_sum),str(user_id),float(deep_score),float(total_score)]
                    list = [pri,sec,thr,fin,float(score_sum),int(price_sum),str(user_id),float(deep_score),float(total_score)]

                    id_list.append(list)

    ## MYSQL Connection
    # # Update combination log
    # sql = "INSERT INTO furniture_DB.combination_log (product_id1, product_id2, product_id3, product_id4, single_score_sum, price_sum, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    #
    # # Send to mysql DB   
    # conn2, cur2 = None, None
    # conn2 = pymysql.connect(host=Config.MYSQL_IP,user=Config.MYSQL_USER,password=Config.MYSQL_PASSWORD,db=Config.MYSQL_DB,charset='utf8')
    #
    # with conn2:
    #     with conn2.cursor() as cur2:
    #         cur2.executemany(sql,id_list)
    #         conn2.commit()

    ## MongoDB Connection 
    client = MongoClient('mongodb://{}:{}@localhost:27017/'.format(Config.MONGODB_USER,Config.MONGODB_PASSWORD))
    db = client.roombi_combination
    collection = db.combination_log
    
    # Insert ID_list to Combination Log
    collection.insert_many(return_as_dict(id_list))
    client.close()

    return sorted(id_list, key = lambda x: x[7], reverse=True)

def budget_cut_list(return_id_list, budget):
    returnlist = []
    
    for combination in return_id_list:       

        if int(combination[5]) <= budget:
            returnlist.append(combination)
            
    if not returnlist:
        print("No Combination Within Budget")
        return None
    else:
        return returnlist

def return_as_dict(id_list):
    returnlist = []
    
    index=['product_id1','product_id2','product_id3','product_id4','single_score','price_sum','user_id','combination_score','total_score']

    for combination in id_list:
        returnlist.append(dict(zip(index,combination)))     

    return returnlist  

from operator import itemgetter
import numpy as np
import pymysql
import random
from config import Config


def add_price_sum(final_list):
    for i,a in enumerate(final_list):
        for j,b in enumerate(final_list[i]):
            for k,c in enumerate(final_list[i][j]):
                for l,d in enumerate(final_list[i][j][k]):
                    sum = 0.
                    price_sum = 0
                    for m,e in enumerate(final_list[i][j][k][l]):
                        sum += final_list[i][j][k][l][m]['single score']
                        price_sum += final_list[i][j][k][l][m]['Price']
                    final_list[i][j][k][l].append(sum)
                    final_list[i][j][k][l].append(price_sum)
    return final_list

def return_id_list(final_list_with_sum, user_id):
    id_list = []
    # Update combination log
    sql = "INSERT INTO furniture_DB.combination_log (product_id1, product_id2, product_id3, product_id4, single_score_sum, price_sum, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    
    # Send to mysql DB   
    conn2, cur2 = None, None
    conn2 = pymysql.connect(host=Config.MYSQL_IP,user=Config.MYSQL_USER,password=Config.MYSQL_PASSWORD,db=Config.MYSQL_DB,charset='utf8')

    for i,a in enumerate(final_list_with_sum):
      for j,b in enumerate(final_list_with_sum[i]):
          for k,c in enumerate(final_list_with_sum[i][j]):
              for l,d in enumerate(final_list_with_sum[i][j][k]):
                  pri = final_list_with_sum[i][j][k][l][0]['New_ID']
                  sec = final_list_with_sum[i][j][k][l][1]['New_ID']
                  thr = final_list_with_sum[i][j][k][l][2]['New_ID']
                  fin = final_list_with_sum[i][j][k][l][3]['New_ID']
                  score_sum = final_list_with_sum[i][j][k][l][4]
                  price_sum = final_list_with_sum[i][j][k][l][5]
                  list = [int(pri),int(sec),int(thr),int(fin),float(score_sum),int(price_sum),str(user_id)]
                  id_list.append(list)

    with conn2:
        with conn2.cursor() as cur2:
            cur2.executemany(sql,id_list)
            conn2.commit()

    return sorted(id_list, key = lambda x: x[4], reverse=True)

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
    
    index=['product_id1','product_id2','product_id3','product_id4','score_sum','price_sum','user_id']

    for combination in id_list:
        returnlist.append(dict(zip(index,combination)))     

    return returnlist  


#     l2=['a','b','c','d']
# d1=zip(l1,l2)
# print (d1)#Output:<zip object at 0x01149528>
# #Converting zip object to dict using dict() contructor.
# print (dict(d1))
            
#     if not returnlist:
#         print("No Combination Within Budget")
#         return None
#     else:
#         return returnlist
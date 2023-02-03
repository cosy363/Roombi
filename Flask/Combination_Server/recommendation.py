from operator import itemgetter
import numpy as np
import pymysql
import random
from get_combination_impl import add_price_sum
from config import Config 
color_table = [[85,	65,	65,	55,55,	55],[65, 85,65,	65,	75,	75],[65,65,	85,	75,	65,	65],[55,75,	55,	95,	95,	65],[55,55,	75,	95,	95,	65],[65,65,	65,	75,	75,	95]]


def single_comb(preference,stage,comb_list=[]):
    prime_sort_order = [0,2,4,6,1,5,3,9,7,8]
    second_sort_order = [0,1,4,3,2,5,7,6]
    third_sort_order = [1,3,0,2,4]
    final_sort_order = [0,1]

    # import prime가구 category dB from mysql
    conn, cur = None, None
    conn = pymysql.connect(host=Config.MYSQL_IP,user=Config.MYSQL_USER,password=Config.MYSQL_PASSWORD,db='furniture_DB',charset='utf8')
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("SELECT Rating, Reviews, Category_Num, Color_2, Color_Num, New_ID, Image_URL, Price FROM furniture_DB.furniture_list  WHERE Category_Num = {}".format(str(preference['furniture_combination'][stage-1])))
    mysql_list = cur.fetchall()
    
    # Create empty list
    return_list, return_list2, return_list3 = [],[],[]
    furn_list = []

    # Stage 1: Prime Furniture
    if stage == 1:
        if len(mysql_list) >= 500:
            furn_list = random.sample(mysql_list,500)
        else:
            furn_list = random.sample(mysql_list,int(len(mysql_list)/1.5))

        #Single REC 돌리기
        for i,product in enumerate(furn_list):
            score = single_rec(product,preference,stage)
            furn_list[i]['single score'] = score
        
        #furn_list를 single score의 내림차순 정렬 및 재정렬-> 조합 생성
        sorted_dict = sorted(furn_list, key=itemgetter('single score'), reverse=True)
        for j in prime_sort_order:        
            return_list.append(sorted_dict[j])
        return return_list

    
    # Stage 2: Secnd Furuniture
    elif stage == 2:
        if len(mysql_list) >= 150:
            furn_list = random.sample(mysql_list,150)
        else:
            furn_list = random.sample(mysql_list,int(len(mysql_list)/2))

        for prime in comb_list:
            second_list = []
            prime_copy = []

            for i,product in enumerate(furn_list):
                score = single_rec(product,preference,prime)
                furn_list[i]['single score'] = score

            #조합 생성
            sorted_dict = sorted(furn_list, key=itemgetter('single score'), reverse=True)
            for j in second_sort_order:        
                second_list.append(sorted_dict[j])
                prime_copy.append(prime)
            
            combination = [[i,j] for i,j in zip(prime_copy,second_list)]

            return_list.append(combination)

        return return_list
    
    # Stage 3: Third Furniture
    elif stage == 3:
        if len(mysql_list) >= 150:
            furn_list = random.sample(mysql_list,150)
        else:
            furn_list = random.sample(mysql_list,int(len(mysql_list)/1.3))

        #comb_list = [[p1,s1],[p1,s2]...],[[p2,s1]...]]
        for prime_second in comb_list:
            for data in prime_second:
                prime = data[0]
                second = data[1]
                
                third_list = []
                prime_copy = []
                second_copy = []

                for i,product in enumerate(furn_list):
                    score = single_rec(product,preference,prime,second)
                    furn_list[i]['single score'] = score

                sorted_dict = sorted(furn_list, key=itemgetter('single score'), reverse=True)
                for j in third_sort_order:        
                    third_list.append(sorted_dict[j])
                    prime_copy.append(prime)
                    second_copy.append(second)
                
                combination = [[i,j,k] for i,j,k in zip(prime_copy,second_copy,third_list)]

                return_list2.append(combination)
            return_list.append(return_list2)
            return_list2 = []

        return return_list
    
    # Stage 4: Final Furniture
    elif stage == 4:
        if len(mysql_list) >= 150:
            furn_list = random.sample(mysql_list,150)
        else:
            furn_list = random.sample(mysql_list,int(len(mysql_list)/1.3))

        for prime_second_third in comb_list:
            for prime_second in prime_second_third:
                for data in prime_second:
                    prime = data[0]
                    second = data[1]
                    third = data[2]

                    final_list = []
                    prime_copy = []
                    second_copy = []
                    third_copy = []

                    for i,product in enumerate(furn_list):
                        score = single_rec(product,preference,prime,second,third)
                        furn_list[i]['single score'] = score

                    sorted_dict = sorted(furn_list, key=itemgetter('single score'), reverse=True)
                    for j in final_sort_order:        
                        final_list.append(sorted_dict[j])
                        prime_copy.append(prime)
                        second_copy.append(second)
                        third_copy.append(third)
                    
                    combination = [[i,j,k,l] for i,j,k,l in zip(prime_copy,second_copy,third_copy,final_list)]

                    return_list3.append(combination)
                return_list2.append(return_list3)
                return_list3 = []
            return_list.append(return_list2)
            return_list2 = []
        return return_list

def single_rec(furn,preference,stage,prime={},second={},third={},):
    abs, rel = 0, 0

    ### Absolute Score
    review_score, rating_score = 0, 0
    #Rating Score
    rating_num = furn['Rating']
    if rating_num == 'No Review':
        rating_score = 6
    else:
        rating_num = float(rating_num)
        if rating_num >= 4:
            rating_score = 10
        elif rating_num >= 3 and rating_num < 4:
            rating_score = 7
        elif rating_num >= 0 and rating_num < 3:
            rating_score = 3
        else:
            rating_score = 6

    #Review Score
    review_num = furn['Reviews']
    if review_num == 'No Review':
        review_score = 7
    else:
        review_num = int(review_num)
        if review_num >= 31:
            review_score = 10
        elif review_num >= 11 and review_num < 31:
            review_score = 9
        elif review_num >= 6 and review_num < 11:
            review_score = 8
        elif review_num >= 0 and review_num < 6:
            review_score = 7
        else:
            review_score = 7

    # Sum of Abs Score
    abs = (review_score + rating_score + random.uniform(-2, 2)) / 100 
    rel1, rel2, rel3, rel4 = 0, 0, 0, 0

    ### Relational Score
    user_color = preference['user_color']
    furn_color = furn['Color_Num'] - 1
    user_color_num = len(user_color)

    #Case 1. Prime
    if stage == 1:
        for i in user_color:
            rel1 += color_table[furn_color][i] 

        rel1 = (rel1 / user_color_num)
        rel = (rel1+ random.uniform(-8, 8)) * 0.8 * 0.01
    
    #Case 2. Second
    elif stage == 2:
        for i in user_color:
            rel1 += color_table[furn_color][i] 

        rel1 = (rel1 / user_color_num)
        rel2 = color_table[furn_color][prime['Color_Num']-1]
        rel = ((0.5 * rel1)+(0.5 * rel2)+random.uniform(-7, 7))* 0.8 * 0.01
    
    #Case 3. Third
    elif stage == 3:
        for i in user_color:
            rel1 += color_table[furn_color][i] 

        rel1 = (rel1 / user_color_num)
        rel2 = color_table[furn_color][prime['Color_Num']-1]
        rel3 = color_table[furn_color][second['Color_Num']-1]

        rel = ((0.5 * rel1)+(0.3 * rel2)+(0.2 * rel3)+random.uniform(-8, 8))* 0.8 * 0.01
    
    #Case 3. Final    
    elif stage == 4:
        for i in user_color:
            rel1 += color_table[furn_color][i] 

        rel1 = (rel1 / user_color_num)
        rel2 = color_table[furn_color][prime['Color_Num']-1]
        rel3 = color_table[furn_color][second['Color_Num']-1]
        rel4 = color_table[furn_color][third['Color_Num']-1]

        rel = ((0.3 * rel1)+(0.3 * rel2)+(0.2 * rel3)+(0.2 * rel4)+random.uniform(-6, 6))* 0.8 * 0.01

    # Sum of abs and rel plus random number
    score = abs + rel + random.uniform(-0.03, 0)

    return score

def return_list(user_preference):
    prime_list,second_list,third_list,final_list = [],[],[],[]

    # prime furniture single combination alg.
    prime_list = single_comb(user_preference,1)
    # output: 10 Ps

    ## second furniture single combination alg.
    # combination alg. for each 10 Ps = 80 PXS
    second_list = single_comb(user_preference,2,prime_list)

    ## third furniture single combination alg.
    # combination alg. for each 80 PXS = 400 PXSXT
    third_list = single_comb(user_preference,3,second_list)

    ## final furniture single combination alg.
    # combination alg. for 400 PXSXT = 800 PXSXTXF
    final_list = add_price_sum(single_comb(user_preference,4,third_list))

    return final_list
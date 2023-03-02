import pymysql
import json
import numpy as np
import random

json_string='''{
    "id": 1,
    "username": "Bret",
    "furniture preference": [1,2,5,3],
    "color preference": [1,3,6,4]
}'''
table = [[[1,1],[1,2],[1,3]],[[2,1],[2,2],[2,3]]]


# table = [[1,1,2],[1,2,3],[1,3,4],[2,1,2],[2,2,3],[2,3,2]]

sql = "INSERT INTO furniture_DB.combination_log (product_id1, product_id2, product_id3, product_id4, single_score_sum) VALUES (%s, %s, %s, %s, %s)"

pri,sec,thr,fin = 0,0,0,0
sum = 1
print(sql % (str(pri),str(sec),str(thr),str(fin),str(sum)))

# for i in table:
#     print(i[0])

color_rand, furniture_rand = [], []
for i in range(4):
    a = random.randint(1,6)
    b = random.randint(1,9)
    while a in color_rand:
        a = random.randint(1,6)
    while b in furniture_rand:
        b = random.randint(1,9)
    color_rand.append(a)
    furniture_rand.append(b)

print(sorted(color_rand))
print(sorted(furniture_rand))
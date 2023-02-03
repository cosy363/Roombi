from nturl2path import url2pathname
import cv2
from matplotlib import pyplot as plt
import requests
import numpy as np


def imshow(final_list,price,i,j,k,l):    
    url1 = final_list[i][j][k][l][0]['Image_URL']
    url2 = final_list[i][j][k][l][1]['Image_URL']
    url3 = final_list[i][j][k][l][2]['Image_URL']
    url4 = final_list[i][j][k][l][3]['Image_URL']

    image_nparray = np.asarray(bytearray(requests.get(url1).content), dtype=np.uint8)
    image1 = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)

    image_nparray = np.asarray(bytearray(requests.get(url2).content), dtype=np.uint8)
    image2 = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)

    image_nparray = np.asarray(bytearray(requests.get(url3).content), dtype=np.uint8)
    image3 = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)

    image_nparray = np.asarray(bytearray(requests.get(url4).content), dtype=np.uint8)
    image4 = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)
    

    Hori = np.concatenate((image1, image2), axis=1)
    Hori2 = np.concatenate((image3, image4), axis=1)
    # concatenate image Vertically
    Verti = np.concatenate((Hori, Hori2), axis=0)
    
    if len(str(price)) == 7:
        price_text = str(price)[0]+ ","+str(price)[1]+str(price)[2]+ str(price)[3]+"," +str(price)[4]+ str(price)[5]+str(price)[6]+" Won"
    elif len(str(price)) == 6:
        price_text = str(price)[0]+str(price)[1]+str(price)[2]+ "," +str(price)[3]+str(price)[4]+ str(price)[5]+" Won"
    else:
        price_text = str(price)[0]+str(price)[1]+ "," +str(price)[3]+str(price)[4]+ str(price)[5]+" Won"
    cv2.putText(Verti,price_text,(550,1200),cv2.FONT_HERSHEY_PLAIN,6,(0,0,0),8)
    cv2.imshow('Combination', Verti)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

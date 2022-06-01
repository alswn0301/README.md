# -*- coding: utf-8 -*-
"""movie_reviews.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IUUdROBbh3fpn-_D67Pg9qzFsBFNbVAM
"""

import requests
from bs4 import BeautifulSoup
import time
import csv

need_reviews_cnt = 100
reviews = []
review_data=[]

for page in range(15):
    url = f'https://movie.naver.com/movie/point/af/list.naver?&page={page}'
    html = requests.get(url)
    soup = BeautifulSoup(html.content,'html.parser')
    reviews = soup.find_all("td",{"class":"title"})
    
    for review in reviews:
        sentence = review.find("a",{"class":"report"}).get("onclick").split("', '")[2]
        if sentence != "":
            movie = review.find("a",{"class":"movie color_b"}).get_text()
            score = review.find("em").get_text()
            review_data.append([movie,sentence,int(score)])
            need_reviews_cnt-= 1  
    if need_reviews_cnt < 0:                                         
        break
    time.sleep(0.5)
     
columns_name = ["movie","sentence","score"]
with open ( "samples.csv", "w", newline ="",encoding = 'utf8' ) as f:
    write = csv.writer(f)
    write.writerow(columns_name)
    write.writerows(review_data)


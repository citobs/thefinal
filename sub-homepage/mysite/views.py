from django.shortcuts import render, get_object_or_404, redirect
from mysite.models import Post, resultall, fullist, RestaurantMenu,choice
from django.utils import timezone
from django.db import connection

import tensorflow
from tensorflow.keras.preprocessing import image
from tensorflow.keras import models, layers
from tensorflow.keras.models import load_model
import cv2
import numpy as np
import requests
import re
import warnings
from bs4 import BeautifulSoup as bs
import pandas as pd
from time import sleep
import datetime
import sys
import pymysql
import random

# #음식추천 횟수를 조회하는 코드 시작
# res = resultall.objects.all()
# fcount = res.count()
# #끝
# #사진입력 횟수를 조회하는 코드 시작
# sp = Post.objects.all()
# spcount = sp.count()
# #끝

count = 0

#집어넣고 DB에서 끄내올때
def foodview(request):
    f2 = choice.objects.all().order_by('-pk')
    mere = RestaurantMenu.objects.all().order_by('-pk')
    
    
    
    return render(request, 'mysite/choice.html',{'f2':f2,'mere':mere})


def fchoice(request):
    fd = fullist.objects.all()
    # 전체 메뉴 조회
    global count
    count = count + 1
    f3 = []
    f1 = request.GET['choice']
    
    # f1.split(',')
    f3.append(f1.split(','))
    
   
    # df1 = pd.Series(f3)
    df1 =pd.DataFrame(list(f3))
    df1.reset_index
    df1 = df1.rename(columns={0:"음식명",1:"음식점",2:"감정상태", 3:"날씨",4:"계절"})
    # df1.drop([''],axis=1)
    # df1 = df1.columns["메뉴명","음식점","감정상태"]
    # df1[0] = df1[0].str.replace("0"," ", )
    # df1 =pd.DataFrame(f3).transpose()
     

    #0이 음식 /#1이 음식점 /#2가 감정
         
    
    
    choice.objects.create(
       menu = str(df1["음식명"].values).replace("['","").replace("']",""),
       res = str(df1["음식점"].values).replace("['","").replace("']",""),
       emotion = str(df1["감정상태"].values).replace("['","").replace("']",""),
       weather = str(df1["날씨"].values).replace("['","").replace("']",""),
       season = str(df1["계절"].values).replace("['","").replace("']",""),
       
       
        
    )
 
        
    
    
 
    
    foodlist = resultall.objects.all()        
    print(type(f1))
    print(type(f3))
    print(df1.values)
  
      
    return render(request, 'mysite/flist.html',{'fd':fd,'f1':f1, 'count':count, 'foodlist':foodlist})





def base1(request):
    return render(request, 'mysite/base1.html')

def blog1(request):
    return render(request, 'mysite/blog1.html')

def weather(request):
    html = requests.get('https://weather.naver.com/today/09680630?cpName=KMA')
    soup = bs(html.text, 'html.parser') 

    a = soup.find('span', {'class':'weather'}).get_text()

    return render(request, 'mysite/weather.html', {'a':a})




# # Create your views here.
def index(request):
    return render(request,'mysite/index.html')

# # blog.html 페이지를 부르는 blog 함수
# # blog.html 페이지를 부르는 blog 함수
# def blog(request):
#     # 모든 Post를 가져와 postlist에 저장합니다
#     postlist = Post.objects.all()
#     # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다 
#     return render(request, 'mysite/blog.html', {'postlist':postlist})

# def posting(request, pk):
#     # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
#     post = Post.objects.get(pk=pk)
#     # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
#     return render(request, 'mysite/posting.html', {'post':post})

def new_post(request):
    res = resultall.objects.all()
    fcount = res.count()
#끝
#사진입력 횟수를 조회하는 코드 시작
    sp = Post.objects.all()
    spcount = sp.count()
#끝
  
    global count
    count = count+1
    if request.method == 'POST':
        if request.POST.get('mainphoto'):
            new_article=Post.objects.create(
                # postname=request.POST.get('postname'),
                # contents=request.POST.get('contents'),
                mainphoto= request.FILES['mainphoto'],
            )
        else:
            new_article=Post.objects.create(
                # postname=request.POST.get('postname'),
                # contents=request.POST.get('contents'),
                mainphoto= request.FILES['mainphoto'],
            )

        return redirect('/blog/food_list/')
    return render(request, 'mysite/new_post.html', {'count':count,'fcount':fcount, 'spcount':spcount})

def show_post(request):
    res = resultall.objects.all()
    fcount = res.count()
#끝
#사진입력 횟수를 조회하는 코드 시작
    sp = Post.objects.all()
    spcount = sp.count()
#끝
    global count
    count = count+1
    #최신순으로 조회(-pk 역순 조회)
    postlist = Post.objects.all().order_by('-pk')
    return render(request, 'mysite/show.html', {'postlist':postlist,'count':count,'fcount':fcount, 'spcount':spcount})
#끝

#음식기록 추가코드(show_food 페이지와 연결)
def show_food(request):
    res = resultall.objects.all()
    fcount = res.count()
#끝
#사진입력 횟수를 조회하는 코드 시작
    sp = Post.objects.all()
    spcount = sp.count()
    global count
    count = count+1         
    foodlist = resultall.objects.all().order_by('-pk')
    return render(request, 'mysite/foodlist.html', {'foodlist':foodlist,'count':count,'fcount':fcount, 'spcount':spcount})


def molar(request):
    global count
    res = resultall.objects.all()
    count = count+1
    fcount = res.count()
#끝
#사진입력 횟수를 조회하는 코드 시작
    sp = Post.objects.all()
    spcount = sp.count()
#끝
    if request.method == 'POST':
        if request.POST.get('angry'):
            a1 = 'angry'
        elif request.POST.get('happy'):
            a1 = 'happy'
        else:
            a1 = 'sad'
       

        
    return render(request, 'mysite/food_list1.html', {'count':count,'fcount':fcount,'spcount':spcount})


def food_list1(request):
    res = resultall.objects.all()
    fcount = res.count()
#끝
#사진입력 횟수를 조회하는 코드 시작
    sp = Post.objects.all()
    spcount = sp.count()
    global count
    count = count+1   
    if request.method == 'POST':
        if request.POST.get('angry'):
            a1 = 'angry'
            emo = '분노한'
         
        elif request.POST.get('happy'):
            a1 = 'happy'
            emo = '행복한'
        else:
            a1 = 'sad'
            emo = '슬픈'
           

    cursor = connection.cursor()

    strSql = "SELECT * FROM mysite_post"
    result = cursor.execute(strSql)
    datas = cursor.fetchall()

    connection.commit()
    connection.close()


    arr = []
    for data in datas:
        row = {
            'id' : data[0],
            'mainphoto' : data[3]
        }
        arr.append(row)  

    ptlink = arr[-1]["mainphoto"]
    
    model = load_model('g:/VGG16_BatchNor.h5') # 모델명
    
    roi = cv2.imread(f'G:/fianle1/media/{ptlink}') # 파일 경로폴더대로 표시해줘야함
    #roi = cv2.imread('media/{}'.format(arr[-1].mainphoto)) # 파일 경로
    
    w, h = 250, 250
    roi = cv2.resize(roi, (w,h), interpolation = cv2.INTER_AREA)
    roi = roi.astype('float') / 255.0
    # roi = img_to_array(roi)
    roi = np.expand_dims(roi, axis=0)
    # img = img.reshape(1,w,h,3)

    Prediction = model.predict(roi)

    #Prediction[0]   #감정별 백분율 (화남 0, 기쁨 1, 중립 2, 슬픔3)


    # percent = Prediction[0][np.argmax(Prediction)]

    result = np.argmax(Prediction)#백분율이 제일 높은 값
    

    html = requests.get('https://weather.naver.com/today/09680630?cpName=KMA')
    soup = bs(html.text, 'html.parser') 

    
    data1 = soup.find('span', {'class':'weather'}).get_text()
    if data1 == '비':
        b = '_rain'
        wea = '비'
    elif data1 == '눈':
        b = '_snow'
        wea = '눈'
    else:
        b = ''
        wea = '맑음'
        
    
    now = datetime.datetime.now()
    if now.month == [3, 4, 5]:
        c = '_spring'
        sea = '봄'
    elif now.month == [6, 7, 8]:
        c = '_summer'
        sea = '여름'
    elif now.month == [9, 10, 11]:
        c = '_fall'
        sea = '가을'
    else:
        c = '_winter'
        sea = '겨울'
        
    
    final = a1+b+c

    
    
    cursor2 = connection.cursor()

    strSql2 = f"SELECT * from (SELECT * FROM menu_score_all  group by menu order by  {final}  DESC, rand()) res group by restaurant order by {final} DESC;"
    result2 = cursor2.execute(strSql2)
    datas2 = cursor2.fetchall()

    connection.commit()
    connection.close()

    arr2 = []
    for data in datas2:
        row2 = {
            'menu' : data[0],
            'restaurant' : data[1]
        }
        arr2.append(row2)    
    
    menu1 = arr2[0]["menu"]     
    restaurant1 = arr2[0]["restaurant"]
    menu2 = arr2[1]["menu"]     
    restaurant2 = arr2[1]["restaurant"]
    menu3 = arr2[2]["menu"]     
    restaurant3 = arr2[2]["restaurant"]
    menu4 = arr2[3]["menu"]     
    restaurant4 = arr2[3]["restaurant"]
    menu5 = arr2[4]["menu"]     
    restaurant5 = arr2[4]["restaurant"]

    d= []
    e= []
    f=[]

    d.append(menu1)
    d.append(menu2)
    d.append(menu3)
    d.append(menu4)
    d.append(menu5)           
    e.append(restaurant1)
    e.append(restaurant2)
    e.append(restaurant3)
    e.append(restaurant4)
    e.append(restaurant5)
    for i in range(1,len(d)+1):
            i =+i
            f.append(i)
    folist = zip(f, d, e)
    resultall.objects.create(
            restaurant = e,
            menu = d,
            season = final,
            emotion = a1
        )
    
    fullist.objects.create(
        emot = emo,
        sea = sea,
        wea = wea,        
        first = menu1,
        second = menu2,
        third = menu3,
        fourth = menu4,
        fifth = menu5)

    return render(request, 'mysite/food_list1.html', {'arr':arr[-1], 'a1':a1,'b':b,'c':c, 'd':d, 'e':e,'emo':emo, 'folist': folist, 'final':final,'count':count,'fcount':fcount, 'spcount':spcount,'wea':wea,'sea':sea})

    
def food_list(request):
    res = resultall.objects.all()
    fcount = res.count()
#끝
#사진입력 횟수를 조회하는 코드 시작
    sp = Post.objects.all()
    spcount = sp.count()
    global count
    count = count+1 
    try:
        cursor = connection.cursor()

        strSql = "SELECT * FROM mysite_post"
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()


        arr = []
        for data in datas:
            row = {
                'id' : data[0],
                'mainphoto' : data[3]
            }
            arr.append(row)  

        ptlink = arr[-1]["mainphoto"]
        
        model = load_model('g:/VGG16_BatchNor.h5') # 모델명
        
        roi = cv2.imread('media/{}'.format(ptlink)) # 파일 경로
        #roi = cv2.imread('media/{}'.format(arr[-1].mainphoto)) # 파일 경로
        
        w, h = 250,250
        roi = cv2.resize(roi, (w,h), interpolation = cv2.INTER_AREA)
        roi = roi.astype('float') / 255.0
        # roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)
        # img = img.reshape(1,w,h,3)

        Prediction = model.predict(roi)

        #Prediction[0]   #감정별 백분율 (화남 0, 기쁨 1, 중립 2, 슬픔3)


        percent = round(Prediction[0][np.argmax(Prediction)]*100,2)

        result = np.argmax(Prediction)#백분율이 제일 높은 값
        
       

        if result == 0:
            a = 'angry'
            emotion = "분노한"
        elif result == 1:
            a = 'happy'
            emotion = "행복한"
        elif result == 3:
            a = 'sad'
            emotion = "슬픈"
        else:
            return render(request, 'mysite/molar.html')
            


        html = requests.get('https://weather.naver.com/today/09680630?cpName=KMA')
        soup = bs(html.text, 'html.parser') 

        
        data1 = soup.find('span', {'class':'weather'}).get_text()
        if data1 == '비':
            b = '_rain'
            wea = '비'
        elif data1 == '눈':
            b = '_snow'
            wea = '눈'
        else:
            b = ''
            wea = '맑음'
            
        
        now = datetime.datetime.now()
        if now.month == [3, 4, 5]:
            c = '_spring'
            season = "봄"
        elif now.month == [6, 7, 8]:
            c = '_summer'
            season = "여름"
        elif now.month == [9, 10, 11]:
            c = '_fall'
            season = "가을"
        else:
            c = '_winter'
            season = "겨울"
        
        final = a+c+b

        cursor2 = connection.cursor()

        strSql2 = f" SELECT * from (SELECT * FROM menu_score_all  group by menu order by  {final}  DESC, rand()) res group by restaurant order by {final} desc;"
        result2 = cursor2.execute(strSql2)
        datas2 = cursor2.fetchall()

        connection.commit()
        connection.close()

        arr2 = []
        for data in datas2:
            row2 = {
                'menu' : data[0],
                'restaurant' : data[1]
            }
            arr2.append(row2)    
        
        menu1 = arr2[0]["menu"]     
        restaurant1 = arr2[0]["restaurant"]
        menu2 = arr2[1]["menu"]     
        restaurant2 = arr2[1]["restaurant"]
        menu3 = arr2[2]["menu"]     
        restaurant3 = arr2[2]["restaurant"]
        menu4 = arr2[3]["menu"]     
        restaurant4 = arr2[3]["restaurant"]
        menu5 = arr2[4]["menu"]     
        restaurant5 = arr2[4]["restaurant"]

        d= []
        e= []
        f=[]

        d.append(menu1)
        d.append(menu2)
        d.append(menu3)
        d.append(menu4)
        d.append(menu5)           
        e.append(restaurant1)
        e.append(restaurant2)
        e.append(restaurant3)
        e.append(restaurant4)
        e.append(restaurant5)
        for i in range(1,len(d)+1):
                i =+i
                f.append(i)
        folist = zip(f, d, e)
        resultall.objects.create(
            restaurant = e,
            menu = d,
            season = final,
            emotion = a
        )
        
        #감정에 따른 음식 추천 코드
        fullist.objects.create(
            emot = emotion,
            sea = season,
            first = menu1,
            second = menu2,
            third = menu3,
            fourth = menu4,
            fifth = menu5)
        
        # fullist.objects.create(
        #     emot = a,
        #     sea = c,
        #     first = d[0],
        #     second = d[1],
        #     third = d[2],
        #     fourth = d[3],
        #     fifth = d[4]
        #     )




    except:
        connection.rollback()
        print("Failed selecting in DB")
    

    return render(request, 'mysite/food_list.html', {'arr':arr[-1],'emotion':emotion, "count":count, "season":season,'percent':percent,'a':a,'b':b,'c':c, 'd':d, 'e':e, 'folist': folist,'wea':wea, 'final':final,'fcount':fcount, 'spcount':spcount})
#지도 불러오기 함수
#고투웍
def gotowork(request):
    return render(request,'mysite/고투웍map.html')
#구내식당
def gunae(request):
    return render(request,'mysite/구내식당map.html')
#롤링파스타
def rol(request):
    return render(request,'mysite/롤링파스타map.html')
#돌배기집
def dol(request):
    return render(request,'mysite/돌배기집map.html')
#리춘식당
def lee(request):
    return render(request,'mysite/리춘시장map.html')
#막이오름
def mak(request):
    return render(request,'mysite/막이오름map.html')
#미정국수
def mij(request):
    return render(request,'mysite/미정국수map.html')
#백스비빔밥
def bac1(request):
    return render(request,'mysite/백S비빔밥map.html')
#백스비어
def bac2(request):
    return render(request,'mysite/백스비어map.html')
#백철판
def bac3(request):
    return render(request,'mysite/백철판0410map.html')
#본가
def bon(request):
    return render(request,'mysite/본가map.html')
#분식9단
def bun(request):
    return render(request,'mysite/분식9단map.html')
#빽다방
def bac4(request):
    return render(request,'mysite/빽다방map.html')
#빽보이 피자
def bac5(request):
    return render(request,'mysite/빽보이피자map.html')
#새마을 식당
def sae(request):
    return render(request,'mysite/새마을식당map.html')
#성성식당
def sun(request):
    return render(request,'mysite/성성식당map.html')
#역전우동
def yuk(request):
    return render(request,'mysite/역전우동0410map.html')
#연돈볼카츠
def yeo(request):
    return render(request,'mysite/연돈볼카츠map.html')
#원조쌈밥집
def one(request):
    return render(request,'mysite/원조쌈밥집map.html')
#인생설렁탕
def ins(request):
    return render(request,'mysite/인생설렁탕map.html')
#제순식당
def jes(request):
    return render(request,'mysite/제순식당map.html')
#한신포차
def han(request):
    return render(request,'mysite/한신포차map.html')
#홍콩반점
def hon(request):
    return render(request,'mysite/홍콩반점0410map.html')



def map(request):
    res = resultall.objects.all()
    fcount = res.count()
#끝
#사진입력 횟수를 조회하는 코드 시작
    sp = Post.objects.all()
    spcount = sp.count()
    global count
    count = count+1
    return render(request,'mysite/map.html',{'fcount':fcount, 'spcount':spcount, 'count':count})







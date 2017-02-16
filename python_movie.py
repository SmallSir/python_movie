import requests
import string
from bs4 import BeautifulSoup
import pandas
import time
import numpy as np
import xlsxwriter
import re
movie_select=[]
hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},{'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}]
def getmovie(str_x):
     res=requests.get('https://movie.douban.com/tag/'+str_x+'?start=0&type=T',headers=hds[np.random.randint(0,len(hds))])#GET获取网站资源
     res.encoding='utf-8'
     soup=BeautifulSoup(res.text, 'html.parser')
     #获取一共有多少页数
     paginator=soup.select('.article')[0].text
     #print(paginator)
     paginator=soup.select('.paginator a')[-2].text
     paginator=int(paginator)

     #获取该年所有的电影网页
     url='https://movie.douban.com/tag/'+str_x+'?start={}&type=T'
     for i in range(0,paginator):

          #um=int(i)
          #print('开始进行第'+(um+1)+'页搜索')
          movieurl=url.format(i*20)
          res1=requests.get(movieurl,headers=hds[np.random.randint(0,len(hds))])
          res1.encoding='utf-8'
          soup1=BeautifulSoup(res1.text, 'html.parser')
          for link in soup1.select('.pl2')[:20]:
               time.sleep(np.random.rand() * 5)
               movie = {}
               #获取该电影的详情网页
               try:
                    h2=link.select('a')[0]['href']
               except IndexError:
                    continue
               res2=requests.get(h2)
               res2.encoding='utf-8'
               soup2=BeautifulSoup(res2.text, 'html.parser')
               #获得电影的发行国家/地区
               try:
                    info = soup2.select('#info')[0]
               except IndexError:
                    continue
               movie_from=re.findall('(?<=制片国家/地区: ).+?(?=\n)', info.text)[0]
               #获取该电影的评分
               rating_num='0'
               try:
                    rating_num=link.select('.rating_nums')[0].text
               except IndexError:
                    continue
               if(movie_from[0]==('中' or '香' or '台')and float(rating_num)>7.0):
                    #获取电影名称
                    try:
                         name=soup2.select('#content h1 span')[0].text
                    except IndexError:
                         continue
                    movie['电影评分']=rating_num
                    movie['电影名称']=name
                    print(name,rating_num)
                    movie_select.append(movie)
     df=pandas.DataFrame(movie_select)
     df.to_excel(str_x+'电影高分.xlsx')




for x in range(2014,2017):
     str_x=str(x)
     getmovie(str_x)




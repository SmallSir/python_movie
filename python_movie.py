#是2017,2016,2015年,在豆瓣评分中7.0以上的华语电影
import requests
import string
from bs4 import BeautifulSoup
movie_select=[]
def getmovie(str):
     res=requests.get('https://movie.douban.com/tag/'+str_x+'?start=0&type=T')#GET获取网站资源
     res.encoding='utf-8'
     soup=BeautifulSoup(res.text)
     #获取一共有多少页数
     paginator=soup.select('.paginator a')[-2].text
     #print(paginator)
     paginator=int(paginator)
     movie=[]
     #获取该年所有的电影网页
     url='https://movie.douban.com/tag/'+str_x+'?start={}&type=T'
     for i in range(0,paginator):
          movieurl=url.format(i*20)
          res2=requests.get(movieurl)
          res2.encoding='utf-8'
          soup1=BeautifulSoup(res2.text)
          for link in soup1.select('.pl2')[:20]:
               #获取该电影的详情网页
               h2=link.select('a')[0]['href']
               res2=requests.get(h2)
               res2.encoding='utf-8'
               #获取电影名称
               name=link.select('a')[0].text.replace(' ','')
               #获取该电影的评分
               rating_num=link.select('.rating_nums')[0].text
               print(h2,name,rating_num)
x=int(input("请输入要查找的年份:"))
str_x=str(x)
getmovie(str_x)




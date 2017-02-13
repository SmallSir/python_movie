import requests
import string
from bs4 import BeautifulSoup
movie_select=[]
res=requests.get('https://movie.douban.com/tag/2016?start=0&type=T')#GET获取网站资源
res.encoding='utf-8'
soup=BeautifulSoup(res.text)
#获取一共有多少页数
paginator=soup.select('.article')[0].text
#print(paginator)
paginator=soup.select('.paginator a')[-2].text
paginator=int(paginator)
movie=[]
#获取该年所有的电影网页
url='https://movie.douban.com/tag/2016?start={}&type=T'
for i in range(0,paginator):
     movieurl=url.format(i*20)
     res1=requests.get(movieurl)
     res1.encoding='utf-8'
     soup1=BeautifulSoup(res1.text)
     for link in soup1.select('.pl2')[:20]:
          #获取该电影的详情网页
          h2=link.select('a')[0]['href']
          res2=requests.get(h2)
          res2.encoding='utf-8'
          soup2=BeautifulSoup(res2.text)
          country_from=
          print(country_from)
          # #获取电影名称
          # name=soup2.select('#content h1')[0].text
          # #获取该电影的评分
          # rating_num=link.select('.rating_nums')[0].text
          # print(h2,name,rating_num)



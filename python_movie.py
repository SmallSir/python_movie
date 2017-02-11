#是2017,2016,2015年,在豆瓣评分中7.0以上的华语电影
import requests
from bs4 import BeautifulSoup
movie_select=[]
res=requests.get('https://movie.douban.com/tag/2016?start=0&type=T')#GET获取网站资源
res.encoding='utf-8'
soup=BeautifulSoup(res.text)
movie=[]
for link in soup.select('.pl2')[:20]:
     #获取该电影的详情网页
     # h2=link.select('a')[0]['href']
     # res1=requests.get(h2)
     # res1.encoding='utf-8'
     #获取电影名称
     name=link.select('a')[0].text
    #  name=name.get
     print(name)
     #获取该电影的评分
     #rating_num=link.select('.rating_nums')[0].text
    #  print(h2,name,rating_num)





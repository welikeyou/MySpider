# coding=UTF-8
'''
Created on 2019年6月30日

@author: lipengju
'''
import requests
from bs4 import BeautifulSoup
import re
from test.pickletester import MyDict

# 先获取包含一条条公告的页面
url='http://zbb.whuh.com/tenderwinners?currpage='

# 主函数，获取所有中标公告，成一条条数据存在一个列表中
def theMain(url):
    totalList=[]
    for i in range(1,31):
        myNum=str(i)
        url1=url+myNum
        # 模拟浏览器发送http请求
        myResponse=requests.get(url1)
        # 设置编码方式
        myResponse.encoding='utf-8'
        # 网页源码
        html=myResponse.text
        #开始解析html获取每个初始页的url
        list=parseInitHtml(html)
        for m in list:
            totalList.append(getInformation(m))
    print(totalList[3]['yiName'])
    return totalList


#解析初始网页html的函数,需要用到beautifulsoup库
def parseInitHtml(html):
    myUrl='http://zbb.whuh.com'
    myList=[]   #用于存储每页的所有url
    soup=BeautifulSoup(html,"html.parser")
    soup.prettify()  #将html变得符合标准
    #获取想要的a标签
    for j in range(3,16,2):
        num=str(j)
        myA=soup.select('body > div.iframe_content > div > div.article > div > div.article_index > div:nth-child('+num+') > div:nth-child(2) > a')
        #select方法返回的是所有符合选择器条件的数组
        myUrl1=myUrl+myA[0]['href']
        myList.append(myUrl1)
    return myList
        
    
# 通过每个公告URL获取公告页面源码，并对其进行解析获取一条的数据
def getInformation(resultUrl):
    myDict=[]
    lastResponse=requests.get(resultUrl)
    lastResponse.encoding='utf-8'
    lastHtml=lastResponse.text
    myDict=parseLastHtml(lastHtml)
    return myDict
    
#解析中标公告页面的Url获取一条条数据,存到一个键值对数组中
def parseLastHtml(myHtml):
    dict=[]
    mySoup=BeautifulSoup(myHtml,"html.parser")
    mySoup.prettify()
    myTable=mySoup.select('#onlineHelpContents > table')
    #将获得的公告表格中的信息抽取出来
    tr_arr=myTable[0].find_all("tr")
    if len(tr_arr)==6:
        #说明只有一家中标公司
        jiaName=tr_arr[1].select('td:nth-child(2)')[0].text.strip()
        jiaConNum=""
        jiaConMan=""
        yiName=tr_arr[5].select('td:nth-child(2)')[0].text.strip()
        yiConNum=""
        yiConMan=""
        title=mySoup.select('body > div.iframe_content > div > div.article > div > div.article_title > h3')[0].text.strip()
        hasAgency="0"
        zoneInf=""
        content=tr_arr[5].select('td:nth-child(3)')[0].text.strip()
        dealTime=tr_arr[3].select('td:nth-child(2)')[0].text.strip()
        dealMoney=tr_arr[5].select('td:nth-child(4)')[0].text.strip()
        dealCount="1"
        sortInf=""
        dict={'jiaName':jiaName,'jiaConNum':jiaConNum,'jiaConMan':jiaConMan,'yiName':yiName,'yiConNum':yiConNum,'yiConMan':yiConMan,'title':title,'hasAgency':hasAgency,
              'zoneInf':zoneInf,'content':content,'dealTime':dealTime,'dealMoney':dealMoney,'dealCount':dealCount,'sortInf':sortInf}
        
    return dict
    
    
    
theMain(url)

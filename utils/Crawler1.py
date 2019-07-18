'''
Created on 2019年7月5日

@author: dell
'''
#动态获取网址
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
from pydoc import browse

browser=webdriver.Chrome()    #声明浏览器对象
url='https://www.job592.com/zb/wuhan.html'

def parseSequence(pageNum):
    pageSequnece = pageNum.split("=")
    return pageSequnece[1]

def parseTime(pageTime):
    timeArr0 = pageTime.split("：")
    timeArr1 = timeArr0[1].split('-')
    timeStr = timeArr1[0] + timeArr1[1] + timeArr1[2]
    return timeStr

#获取所有公告的url
def getContent(myKeyWord):
    #allUrl=[]
    try:
        browser.get(url)#起始地址
        input=browser.find_element_by_id('keywords')  #找到id为kw的元素
        input.send_keys(myKeyWord)     #敲入要搜索的关键字
        input.send_keys(Keys.ENTER)   #敲入回车
        wait=WebDriverWait(browser,10)  
        wait.until(EC.presence_of_element_located((By.CLASS_NAME,'c_swrap')))   #等待某个元素加载出来
        browser.switch_to.window(browser.window_handles[1])   #切换到跳转后的标签页
        # myWait.until(EC.presence_of_element_located((By.CLASS_NAME, 'sd_page')))  # 等待某个元素加载出来
        wait.until(EC.text_to_be_present_in_element((By.ID, "resultpage"), u"下一页"))#因为下一页按钮是动态加载的，所以不能直接等待class加载。
        # 得到总页数
        totalPage = browser.find_element_by_css_selector('#resultpage > a:nth-last-child(2)').text
        print(totalPage)
        i = 0
        while i < int(totalPage):
            i = i+1
            wait.until(EC.text_to_be_present_in_element((By.ID, "resultpage"), u"下一页"))
            html = browser.page_source
            # pq模块解析网页源代码
            doc = pq(html)
            pageUrlInfos = doc(".artitem").items()
            for pageUrlInfo in pageUrlInfos:
                pageNum = pageUrlInfo("h2 a").attr("href")
                pageTime = pageUrlInfo(".afoot > span:last-child").text()
                theUrl = "https://show.job592.com/zb/" + parseTime(pageTime)+"_"+parseSequence(pageNum)+".html"
                # 在这里调用解析详情的函数
                print(theUrl)
            # 获取到下一页的按钮
            nextPage = browser.find_element_by_css_selector('#resultpage > a:last-child')
            nextPage.click()

    finally:
        #print(allUrl[0])
        #browser.close()
        print("hahaha")

myWord='医院 中标公告'
getContent(myWord)
    

    

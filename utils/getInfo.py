from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from urllib.error import HTTPError
import re

#定义一个武汉第一医院的爬虫类
class first_hospital_infos:

    #对象初始化
    def __init__(self):
        url = 'http://www.whyyy.com.cn/search/news/4909.aspx'
        self.url = url

        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2}) # 不加载图片,加快访问速度
        options.add_experimental_option('excludeSwitches', ['enable-automation']) # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium

        self.browser = webdriver.Chrome(executable_path=chromedriver_path, options=options)
        self.wait = WebDriverWait(self.browser, 10) #超时时长为10s

 # 爬取当前页面数据
    def crawl_page_data(self):
        self.browser.get("http://www.ccgp.gov.cn/cggg/dfgg/zbgg/201907/t20190712_12450657.htm")
        soup = BeautifulSoup(self.browser.page_source, "lxml")
        # 爬取网页信息
        # 需要等待信息全部加载后再读取
        # self.wait.until(EC.presence_of_element_located(By.CLASS_NAME,myFooter))
        info_text = soup.find('div',class_=re.compile(r'(.*?)con(.*?)')).get_text()
        info_text.encode('utf-8')
        # 保存到文本文档中，a+表示以读写且添加的方式写入，编码为utf-8，默认编码为gbk
        with open('D:\\我的文档\\学习文档\\大三下\\2019刘老师实验室暑期实训\\data\\raw_data.txt','a+',encoding='utf-8') as f:
            f.write(info_text)
            #作为分割
            f.write('wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww')
            f.close()


if __name__ == "__main__":

    chromedriver_path = "C:\Program Files (x86)\Google\Chrome\Application/chromedriver.exe" #改成你的chromedriver的完整路径地址

    a = first_hospital_infos()
    a.crawl_page_data() #爬取当前页面数据
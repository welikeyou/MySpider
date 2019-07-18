from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pyquery import PyQuery as pq
from time import sleep

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
        # 获取本页面源代码
        self.browser.get("http://www.hbyxjzcg.cn/publish/show4727.html")
        html = self.browser.page_source
        # pq模块解析网页源代码
        doc = pq(html)

        # 爬取网页信息
        info_text = doc('div').text()
        print(info_text)


if __name__ == "__main__":

    chromedriver_path = "C:\Program Files (x86)\Google\Chrome\Application/chromedriver.exe" #改成你的chromedriver的完整路径地址

    a = first_hospital_infos()
    a.crawl_page_data() #爬取当前页面数据
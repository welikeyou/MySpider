from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from urllib.error import HTTPError
import re

#解析网页

# 定义一个用于保存数据的结构体
# DataType = np.dtype({'name':['jia_name','jia_contact_way','jia_linkman','yi_name','yi_contact_way','yi_linkman',
#                              'web_url','has_agency','address','content','money','amount','time'],'formats':
#                              ['S32','S32','S32','S32','S32','S32','S32','S32','S32','S32','S32','S32','S32']})

class DataType:
    def __init__(self):
        self.jia_name = "null"
        self.jia_contact_way = "null"
        self.jia_linkman = "null"
        self.yi_name = "null"
        self.yi_contact_way = "null"
        self.yi_linkman = "null"
        self.web_url = "null"
        self.has_agency = "null"
        self.address = "null"
        self.content = "null"
        self.money = "null"
        self.amount = "null"
        self.time = "null"


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
    def parse_detail(str):
        strArr = str.split(":")
        return strArr[1]
 # 爬取当前页面数据

    #爬取武汉第一人民医院
    def crawl_page_data_first_hospital_0(self):
        # 获取本页面源代码
        try:
            url = "http://www.whyyy.com.cn/search/news/4909.aspx"
            html = self.browser.get(url)
            wait = WebDriverWait(self.browser, 10)
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'list_aboutpage')))  # 等待某个元素加载出来
            soup = BeautifulSoup(self.browser.page_source, "lxml")
            spiderData = DataType()
            try:
                jia_fang = soup.find(text=re.compile("采购人联系方式")).find_parent().find_parent().find_next_siblings("p")
            except AttributeError:
                jia_fang = soup.find(text=re.compile("采购人联系方式")).find_parent().find_next_siblings("p")
            try:
                spiderData.jia_name = jia_fang[0].find("span").get_text()
            except IndexError:
                spiderData.jia_name = "武汉市第一医院"
            print(spiderData.jia_name)
            try:
                spiderData.jia_contact_way = "电话：" + soup.find_all(text=re.compile("电话："))[0].find_parent().find(
                    "span").get_text()
            except AttributeError:
                try:
                    spiderData.jia_contact_way = soup.find(text=re.compile("电话："))
                except AttributeError:
                    spiderData.jia_contact_way = "null"
            print(spiderData.jia_contact_way)
            try:
                spiderData.jia_linkman = jia_fang.find(text=re.compile("联系人")).get_text()
            except AttributeError as e:
                spiderData.jia_linkman = "null"
            print(spiderData.jia_linkman)
            try:
                spiderData.address = jia_fang[1].get_text()
            except IndexError:
                spiderData.address = "null"
            print(spiderData.address)
            try:
                spiderData.yi_contact_way = soup.find_all(text=re.compile("电话："))[1]
            except IndexError:
                spiderData.yi_contact_way = "null"
            spiderData.yi_name = soup.find(text=re.compile("中标(人|供应商)名称")).find_parent().get_text()
            print(spiderData.yi_name)
            spiderData.money = soup.find(text=re.compile("中标金额(.*)"))
            if spiderData.money == "中标金额：":
                spiderData.money = soup.find(text=re.compile("中标金额(.*)")).find_parent().find_next_sibling().get_text()
            print(spiderData.money)
            spiderData.time = soup.find("h4", class_="meta").find("span").get_text()
            print(spiderData.time)
            spiderData.content = soup.find(class_="about_header").find(class_="title").get_text()
            print(spiderData.content)
            try:
                spiderData.amount = soup.find(text=re.compile("数量：")).find_parent().get_text()
            except AttributeError:
                spiderData.amount = "null"
            print(spiderData.amount)
            spiderData.web_url = url  # 实际调用时是参数
            print(spiderData.web_url)
        except HTTPError as e:
            print(e)



        # 针对招标预警网的解析
        # temp = soup.find_all(text=re.compile(r'^ *采购人'))
        # tempArr=temp.split("：")#使用中文冒号
        # spiderData.jia_name = tempArr[1]
        # print(spiderData.jia_name)

    # 爬取武汉第一人民医院
    def crawl_page_data_first_hospital_1(self):
        # 获取本页面源代码
        try:
            url = "http://www.whyyy.com.cn/search/news/2724.aspx"
            html = self.browser.get(url)
            wait = WebDriverWait(self.browser, 10)
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'list_aboutpage')))  # 等待某个元素加载出来
            text = html.content.decode('utf-8')#进行编码
            soup = BeautifulSoup(text, "lxml")
            spiderData = DataType()
            spiderData.jia_name = "武汉市第一医院"
            print(spiderData.jia_name)
            try:
                spiderData.jia_contact_way =  soup.find(text=re.compile("(.*)电(.*)话(.*)")).get_text()
            except AttributeError:
                spiderData.jia_contact_way = "null"
            print(spiderData.jia_contact_way)
            try:
                spiderData.jia_linkman = soup.find_all(text=re.compile("(.*)联(.*)系(.*)人(.*)：(.*)"))
            except AttributeError as e:
                spiderData.jia_linkman = "null"
            print(spiderData.jia_linkman)
            try:
                spiderData.address = soup.find_all(text=re.compile("地(.*)址：(.*)"))
            except IndexError:
                spiderData.address = "null"
            print(spiderData.address)
            spiderData.yi_name = soup.find(text=re.compile("(.*)中标单位")).find_parent("p").get_text()
            print(spiderData.yi_name)
            spiderData.money = soup.find(text=re.compile("中标金额(.*)")).find_parent("p").get_text()
            print(spiderData.money)
            spiderData.time = soup.find("h4", class_="meta").find("span").get_text()
            print(spiderData.time)
            spiderData.content = soup.find(class_="about_header").find(class_="title").get_text()
            print(spiderData.content)
            spiderData.amount = "null"
            print(spiderData.amount)
            spiderData.web_url = url  # 实际调用时是参数
            print(spiderData.web_url)
        except HTTPError as e:
            print(e)

        # 针对招标预警网的解析
        # temp = soup.find_all(text=re.compile(r'^ *采购人'))
        # tempArr=temp.split("：")#使用中文冒号
        # spiderData.jia_name = tempArr[1]
        # print(spiderData.jia_name)

    #爬取武汉招标预警网信息 未完成
    def crawl_page_data_first_hospital_2(self):
        # 获取本页面源代码
        try:
            url = "http://www.whyyy.com.cn/search/news/4909.aspx"
            html = self.browser.get(url)
            wait = WebDriverWait(self.browser, 10)
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'list_aboutpage')))  # 等待某个元素加载出来
            soup = BeautifulSoup(self.browser.page_source, "lxml")
            spiderData = DataType()
            try:
                jia_fang = soup.find(text=re.compile("采购人联系方式")).find_parent().find_parent().find_next_siblings("p")
            except AttributeError:
                jia_fang = soup.find(text=re.compile("采购人联系方式")).find_parent().find_next_siblings("p")
            try:
                spiderData.jia_name = jia_fang[0].find("span").get_text()
            except IndexError:
                spiderData.jia_name = "武汉市第一医院"
            print(spiderData.jia_name)
            try:
                spiderData.jia_contact_way = "电话：" + soup.find_all(text=re.compile("电话："))[0].find_parent().find(
                    "span").get_text()
            except AttributeError:
                try:
                    spiderData.jia_contact_way = soup.find(text=re.compile("电话："))
                except AttributeError:
                    spiderData.jia_contact_way = "null"
            print(spiderData.jia_contact_way)
            try:
                spiderData.jia_linkman = jia_fang.find(text=re.compile("联系人")).get_text()
            except AttributeError as e:
                spiderData.jia_linkman = "null"
            print(spiderData.jia_linkman)
            try:
                spiderData.address = jia_fang[1].get_text()
            except IndexError:
                spiderData.address = "null"
            print(spiderData.address)
            try:
                spiderData.yi_contact_way = soup.find_all(text=re.compile("电话："))[1]
            except IndexError:
                spiderData.yi_contact_way = "null"
            spiderData.yi_name = soup.find(text=re.compile("中标(人|供应商)名称")).find_parent().get_text()
            print(spiderData.yi_name)
            spiderData.money = soup.find(text=re.compile("中标金额(.*)"))
            if spiderData.money == "中标金额：":
                spiderData.money = soup.find(text=re.compile("中标金额(.*)")).find_parent().find_next_sibling().get_text()
            print(spiderData.money)
            spiderData.time = soup.find(text="发布时间：").find_parent().find_parent().get_text().spilt("：")[2]  #固定格式
            print(spiderData.time)
            spiderData.content = soup.find(text=re.compile("^项目名称：")).find(class_="title").get_text()
            print(spiderData.content)
            try:
                spiderData.amount = soup.find(text=re.compile("数量：")).find_parent().get_text()
            except AttributeError:
                spiderData.amount = "null"
            print(spiderData.amount)
            spiderData.web_url = url  # 实际调用时是参数
            print(spiderData.web_url)
        except HTTPError as e:
            print(e)

if __name__ == "__main__":

    chromedriver_path = "C:\Program Files (x86)\Google\Chrome\Application/chromedriver.exe" #改成你的chromedriver的完整路径地址

    a = first_hospital_infos()
    a.crawl_page_data_first_hospital_1() #爬取第一医院数据
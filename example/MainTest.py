import Crawler1

if __name__ == "__main__":

    chromedriver_path = "C:\Program Files (x86)\Google\Chrome\Application/chromedriver.exe" #改成你的chromedriver的完整路径地址

    a = first_hospital_infos()
    a.crawl_page_data() #爬取当前页面数据
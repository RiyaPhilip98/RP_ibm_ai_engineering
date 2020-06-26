#bmc website 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import csv
from htmldate import find_date

data = {}

class scraper:
    def __init__(self):
        self.driver = webdriver.Chrome('/Users/riyaphilip/Downloads/chromedriver 2')
        self.links = []
        self.final_links = []
        self.alert_date = None 
        
    def open_browser(self,url_link):
        self.driver.get(url_link)

    def obtain_links_homepage(self):
        for elements in self.driver.find_elements_by_tag_name('a'):
            urls = elements.get_attribute('href')
            self.links.append(urls)
    
    def obtain_links_insidepages(self):
        for elements in self.driver.find_elements_by_tag_name('a'):
            urls = elements.get_attribute('href')
            self.final_links.append(urls)
            
    
    def update_date(self):
        self.driver.execute_script("javascript:alert(document.lastModified)")
        alert_box = self.driver.switch_to.alert
        self.alert_date = alert_box.text
        alert_box.accept()

    def get_robots_txt(url_link):
        if url_link.endswith('/'):
            path = url_link
        else:
            path = url + '/'
        req = urllib.request.urlopen(path + "robots.txt", data=None)
        data = io.TextIOWrapper(req, encoding = 'utf-8')
        return data.read()

run = scraper()
run.open_browser('https://www.brynmawr.edu/?fbclid=IwAR0tbPZms9IOEFLPoo5FOkb3dfJwTPbmHjwFPtAh_y7aIgWViLQZIboI6KE')
run.obtain_links_homepage()
print(run.links)
print(run.get_robots_txt)

for elems in run.links:
    run.open_browser(elems)
    last_updated = find_date(elems)
    run.obtain_links_insidepages()
    run.update_date()
    data.update({
        'Link': elems,
        'Date-Modified' : last_updated,
        'Date-Crawled': run.alert_date
    })
    print(data)



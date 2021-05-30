from selenium.webdriver.remote.webelement import WebElement
import config as cfg
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


PATH = cfg.PATH + "/chromedriver"
driver = webdriver.Chrome(PATH)

# add website names here
web_list = list()
link1 = list()
count = 1
web_list = ["https://academicpositions.com/find-jobs/PhD-in-Chemistry-by-all-in-all/all/1"]

for iter in web_list:
    print("inside for")
    print(iter)
    driver.get(iter)
    if iter == "https://academicpositions.com/find-jobs/PhD-in-Chemistry-by-all-in-all/all/1":
        time.sleep(3)
        try:
            print("inside tryyy")
            anch = driver.find_elements_by_tag_name("a")
            for i in  anch:
                print("inside anch for")
                try:
                    if i.get_attribute("class") == "job__title js-gtm-joblink":
                        print("inside TRY ",count)
                        count+=1
                        i.click()
                        # print(i.get_attribute("href"))
                        print("found a page")
                except:
                    print("no class found")
                    continue
                
            #     link1 = driver.find_element_by_link_text("job__title js-gtm-joblink")
            # print(link1)
        except:
            print("Dindint find /ad/")
            continue
import config as cfg
import time

from selenium import webdriver

PATH = cfg.PATH + "/chromedriver"
driver = webdriver.Chrome(PATH)
# 
# 
#
topic = list()

def click_link_academicposition():
    time.sleep(3)
    try:
        print("inside tryyy")
        anch = driver.find_elements_by_tag_name("a")
        for i in  anch:
            if i.get_attribute("class") == "job__title js-gtm-joblink":
                print("inside TRY ")
                driver.get(i.get_attribute("href"))
                # i.click()
                print("found a page")
                print("i = ", i)
                print("title: ",driver.title)
                # time.sleep(5)

                # finding clgname
                page_anch = driver.find_elements_by_tag_name("h1")
                print("!!!!!!!!",type(page_anch))
                print("QQQQQQQQQQQQ",len(page_anch))

                for y in page_anch:
                    print(y.text)
                #     # print(y.get_attribute("class"))
                #     if y.get_attribute("class") == "job-title":
                #         print("CLASS FOUND")
                #         print(y.text)
    except:
        print("Dindint find any anch tag")
# 
# 
#
# add website names here
web_list = list()
web_list = ["https://academicpositions.com/find-jobs/PhD-in-Chemistry-by-all-in-all/all/1"]
 
for iter in web_list:
    print("inside for")
    print(iter)
    driver.get(iter)
    if iter == "https://academicpositions.com/find-jobs/PhD-in-Chemistry-by-all-in-all/all/1":
        click_link_academicposition()



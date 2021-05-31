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
    anch = driver.find_elements_by_tag_name("h1")
    # print("anch")
    print(anch[0].text)
                

# 
#
# add website names here
web_list = list()
web_list = ["https://academicpositions.com/ad/max-planck-institute-for-solid-state-research/2021/phd-position-spintronics-with-van-der-waals-heterostructures/159117"]
 
for iter in web_list:
    print("inside for")
    print(iter)
    driver.get(iter)
    if iter == "https://academicpositions.com/ad/max-planck-institute-for-solid-state-research/2021/phd-position-spintronics-with-van-der-waals-heterostructures/159117":
        click_link_academicposition()



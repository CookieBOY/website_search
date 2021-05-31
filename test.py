from contextlib import nullcontext
import config as cfg
import time

from selenium import webdriver

PATH = cfg.PATH + "/chromedriver"
driver = webdriver.Chrome(PATH)
# 
# 
#
topic = list()
clg_name = list()
page_urls = list()

def click_link_academicposition():
    print((driver.find_element_by_xpath('//a[@class = "job-employer-title"][1]')).text)
    print((driver.find_element_by_xpath('//h1[@class = "job-title"][1]')).text)
    # if driver.find_element_by_xpath('//a[@class = "job-location"]'):  
    try:    
        try:
            if (driver.find_element_by_xpath('//span[@class = "job-publishing-date"][1]').text) == "":
                print("No Date Found")
            else:
                print((driver.find_element_by_xpath('//span[@class = "job-publishing-date"][1]')).text)
    # else:
        except:
            print("No Date Found")
        print((driver.find_element_by_xpath('//a[@class = "job-location"][1]')).text)
    # else:
    except:
        print("No Location Found")
    # if (driver.find_element_by_xpath('//span[@class = "job-publishing-date"][1]')):
    


    driver.close()
    
    # driver.close()
# 
#
# add website names here
web_list = list()
# no date url
web_list = ["https://academicpositions.com/ad/max-planck-institute-for-solid-state-research/2021/phd-position-spintronics-with-van-der-waals-heterostructures/159117"]

# all good url
# web_list = ["https://academicpositions.com/ad/national-institute-of-chemical-physics-and-biophysics-nicpb/2021/phd-position-synthesis-of-flexible-cavitands-as-efficient-drug-discovery-and-delivery-agents-and-sensors/158605"]

# no location no date url
# web_list = ['https://academicpositions.com/ad/academic-positions/2020/covid-19-research-positions-phd-and-postdoc/142410']

for iter in web_list:
    print("inside for")
    print(iter)
    driver.get(iter)
    if iter == "https://academicpositions.com/ad/max-planck-institute-for-solid-state-research/2021/phd-position-spintronics-with-van-der-waals-heterostructures/159117":
        click_link_academicposition()
    # if iter == "https://academicpositions.com/ad/national-institute-of-chemical-physics-and-biophysics-nicpb/2021/phd-position-synthesis-of-flexible-cavitands-as-efficient-drug-discovery-and-delivery-agents-and-sensors/158605":
    #     click_link_academicposition()
    # if iter == 'https://academicpositions.com/ad/academic-positions/2020/covid-19-research-positions-phd-and-postdoc/142410':
    #     click_link_academicposition()



import config as cfg
import time
import pandas as pd

from selenium import webdriver

PATH = cfg.PATH + "/chromedriver"
driver = webdriver.Chrome(PATH)
# 
# 
#
page_urls = list()
total_links = 0
clg_name = list()
location = list()
topic = list()
last_date = list()
bad_page_url = list()

def nav_academicposition_pages(pageurls):
    url_count = 0
    for url in pageurls:
        print(url)
        driver.get(url)
        try:
            clg_name.append((driver.find_element_by_xpath('//a[@class = "job-employer-title"][1]')).text)
            topic.append((driver.find_element_by_xpath('//h1[@class = "job-title"][1]')).text)
            bad_page_url.append("")

        
            # if location class not fount at that path
            try:
                try:
                    if ((driver.find_element_by_xpath('//span[@class = "job-publishing-date"][1]')).text) == "":
                        last_date.append('DATE NOT FOUND')
                    else:
                        last_date.append((driver.find_element_by_xpath('//span[@class = "job-publishing-date"][1]')).text)
                except:
                    last_date.append('DATE NOT FOUND')
                location.append((driver.find_element_by_xpath('//a[@class = "job-location"][1]')).text)
            except:
                location.append("LOCATION NOT FOUND")
        except:
            clg_name.append("NO NAME FOUND")
            topic.append("NO TOPIC FOUND")
            bad_page_url.append(url)
        url_count += 1
        print("We just finished taking values from url: ",url_count)

    print("clgname: ",clg_name)
    print("topic: ",topic)
    print("location: ",location)
    print("last_date: ",last_date)
    data_index = pd.DataFrame({'COLLEGE NAME': clg_name,
                               'TOPIC': topic,
                               'LOCATION': location,
                               'LAST DATE': last_date,
                               'BAD PAGES': bad_page_url})
    writer = pd.ExcelWriter('CHEM_PHD.xlsx', engine='xlsxwiter')
    data_index.to_excel(writer, sheet_name='ACADEMIC_POSITION', index=False)
    writer.save()
    driver.close()


def academicposition():
    time.sleep(3)
    try:
        # finding the total number of links to lookup in the entire website
        total_links = int(((driver.find_element_by_xpath('//span[@class="child-item-count"][1]')).text)[1:-1])

        # collecting all the links
        # navigating pages
        anch = driver.find_elements_by_tag_name("a")
        for i in  anch:
            if i.get_attribute("class") == "job__title js-gtm-joblink":
                page_urls.append(i.get_attribute("href"))
        if len(page_urls)<=total_links:
            print(len(page_urls))
            # press the next page button
            path = driver.find_element_by_xpath('//a[@aria-label="Next"]')
            print(path)
            path.click()
            academicposition()
        else:
            nav_academicposition_pages(page_urls)
            driver.close()
    except:
        print("Dindint find any anch tag")
# 
# 
#
# add website names here
web_list = list()
web_list = ["https://academicpositions.com/find-jobs/PhD-in-Chemistry-by-all-in-all/all/1"]

for iter in web_list:
    print(iter)
    driver.get(iter)
    if iter == "https://academicpositions.com/find-jobs/PhD-in-Chemistry-by-all-in-all/all/1":
        academicposition()



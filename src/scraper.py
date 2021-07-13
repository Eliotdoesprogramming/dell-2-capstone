from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
import time
import os
class myScraper(object):
    #initialize with a webdriver object, a description of image to scrape from google
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def scrape_for_image(self, search_term, number_of_images):
        self.driver.get("https://www.google.com/search?q=" + search_term)
        imagelink = self.driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[3]/a')
        imagelink.click()
        time.sleep(1)
        

        images = self.driver.find_elements_by_class_name('rg_i')
        for idx,image in enumerate(images):
            try:
                image.screenshot(self.driver_path[:-16]+'/images/'+str(idx)+'.png')
            except:
                pass

            # next_page = self.driver.find_element_by_class_name('pn')
            # next_page.click()
            # time.sleep(1)

    def close_browser(self):       
        self.driver.close()       
        self.driver.quit()       
        print("Browser closed.")       
        return


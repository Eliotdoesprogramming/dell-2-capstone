from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
import time
import os
import requests
import base64
class myScraper(object):
    #initialize with a webdriver object, a description of image to scrape from google
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.driver = self.open_browser()

    def scrape_for_image_google(self, search_term, number_of_images):
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

    
    #scrape bing for images on a certain topic
    def scrape_bing_for_images(self, search_term, number_of_images):
        failcounter=0       
        self.driver.get("https://www.bing.com/images/search?q=" + search_term)
        image_src_paths = set()
        time.sleep(1)
        while(len(image_src_paths) < number_of_images):
            for path in self.grab_bing_image_src():       
                if(path not in image_src_paths):       
                    image_src_paths.add(path)

            if(self.scroll_down()):       
                failcounter = 0
            else:
                failcounter += 1
            if failcounter > 5:       
                break

            self.bing_seemore_button()
            # time.sleep(1)
            print(len(image_src_paths),' image sources found')

        start_index = self.get_start_index(search_term)
        for idx, url in enumerate(image_src_paths):
            if (url[:4] != 'data'):
                self.download_image_from_url(url, self.driver_path[:-16]+'/images/'+str(search_term)+'/'+str(idx+start_index)+'.png')
            elif(url[:4] == 'data'):       
                image_base64 = url.split('base64,')[1]
                format = 'jpeg' if url.split('image/')[1][0:4] == 'jpeg' else 'png'
                imgdata = base64.b64decode(image_base64)
                #write the base64 image to a file
                with open(self.driver_path[:-16]+'/images/'+str(search_term)+'/'+str(idx+start_index)+'.'+format, 'wb') as f:
                    f.write(imgdata)
                    f.close()
            
    
    #grab all of the image elements from the images with class mimg. then return a list of their src attributes
    def grab_bing_image_src(self):       
        images = self.driver.find_elements_by_class_name('mimg')
        src_paths = []
        for image in images:   
            src = image.get_attribute('src')
            #if not base64 image, continue
            if(src != None):       
                src_paths.append(src)
            
        return src_paths

    def full_screen_browser(self)->bool:       
        try:       
            self.driver.fullscreen_window()
            time.sleep(1)       
            return True       
        except:       
            return False

    def download_image_from_url(self, image_url, file_path):       
        response = requests.get(image_url)       
        with open(file_path, 'wb') as f:       
            f.write(response.content)       
        return

    def get_start_index(self, searchterm)->int:
        #if a directory doesnt exist for this search term, create it
        if not os.path.exists(self.driver_path[:-16]+'/images/'+str(searchterm)):
            os.makedirs(self.driver_path[:-16]+'/images/'+str(searchterm))

        images = os.listdir(self.driver_path[:-16]+'/images/'+str(searchterm))
        nums = []
        for image in images:
            if(image[-4:] == '.png' or image[-4:] == '.jpg'):
                try:
                    nums.append(int(image[:-4]))
                except Exception as e:
                    print(e)
                    pass
        return 0 if len(nums)==0 else max(nums)
                
        

    def bing_seemore_button(self)->bool:
        seemore = self.driver.find_element_by_xpath('//*[@id="bop_container"]/div[2]/a')
        if(seemore.is_displayed()):       
            seemore.click()       
            time.sleep(1)
            return True
        else:
            print("No seemore button found.")
            return False

    def scroll_down(self):
        #check window position
        scroll_position = self.driver.execute_script("return window.GetScrollTop()")
        self.driver.execute_script("window.scrollTo({left:0,top:(window.GetScrollTop()+1000),behavior:'smooth'});") 
        time.sleep(1) 
        #check to see if window position has changed
        new_scroll_position = self.driver.execute_script("return window.GetScrollTop()")
        
        return new_scroll_position != scroll_position
    #method to scroll up 200 pixels
    def scroll_up(self):
        self.driver.execute_script("window.scrollTo(0, -200);")
        time.sleep(1)
        return 
    def open_browser(self):
        driver = webdriver.Chrome(self.driver_path)
        return driver
    def close_browser(self):       
        self.driver.close()       
        self.driver.quit()       
        print("Browser closed.")       
        return


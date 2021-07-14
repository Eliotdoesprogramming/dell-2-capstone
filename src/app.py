import os
from main.scraper import myScraper



cdriver_path = os.path.dirname(__file__)[:-3].replace('\\','/')+'assets/chromedriver.exe'

scraper = myScraper(cdriver_path)
#scraper.scrape_for_image('pizza',40)

scraper.scrape_bing_for_images('salad',100)
scraper.close_browser()

# driver.get('http://www.google.com/')

# box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
# box.send_keys('pizza')
# box.send_keys(Keys.RETURN)


# time.sleep(1)
# #find all images on the page

   
# driver.quit()
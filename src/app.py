import os
from .scraper import myScraper



cdriver_path = os.path.dirname(__file__)[:-3].replace('\\','/')+'assets/chromedriver.exe'

scraper = myScraper(cdriver_path)
scraper.scrape('pizza',40)

# driver.get('http://www.google.com/')

# box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
# box.send_keys('pizza')
# box.send_keys(Keys.RETURN)


# time.sleep(1)
# #find all images on the page

   
# driver.quit()
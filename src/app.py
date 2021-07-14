import os
from main.scraper import myScraper



cdriver_path = os.path.dirname(__file__)[:-3].replace('\\','/')+'assets/chromedriver.exe'

scraper = myScraper(cdriver_path)
#scraper.scrape_for_image('pizza',40)


#scraper.scrape_bing_for_images('salad',100)
scraper.scrape_google_for_images('cow',100)
scraper.close_browser()

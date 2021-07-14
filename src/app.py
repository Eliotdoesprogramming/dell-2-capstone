import os
from main.scraper import myScraper



cdriver_path = os.path.dirname(__file__)[:-3].replace('\\','/')+'assets/chromedriver.exe'

scraper = myScraper(cdriver_path)
scraper.scrape_google_for_images('porter robinson',200)
scraper.close_browser()

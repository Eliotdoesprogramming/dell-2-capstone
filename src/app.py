import os
from main.scraper import myScraper



cdriver_path = os.path.dirname(__file__)[:-3].replace('\\','/')+'assets/chromedriver.exe'

scraper = myScraper(cdriver_path)



def scrape_all_sites(search_term,num_images):
    imgcount = 0
    imgcount += scraper.scrape_google_for_images(search_term,num_images)
    imgcount += scraper.scrape_bing_for_images(search_term,num_images)
    imgcount += scraper.scrape_yahoo_for_images(search_term,num_images)
    return imgcount
imgcount = 0
# imgcount += scrape_all_sites('pizza',1000)
# imgcount += scrape_all_sites('cheese pizza',1000)
# imgcount += scrape_all_sites('pepperoni pizza',1000)
# imgcount += scrape_all_sites('mushroom pizza',1000)
# pizzacount = imgcount
# imgcount += scrape_all_sites('animal',200)
# imgcount += scrape_all_sites('fruit',200)
# imgcount += scrape_all_sites('vegetable',200)
# imgcount += scrape_all_sites('people',400)
# imgcount += scrape_all_sites('car',200)
# imgcount += scrape_all_sites('airplane',200)

imgcount += scrape_all_sites('woman',200)
imgcount += scrape_all_sites('man',200)

print(imgcount, 'images downloaded')
scraper.close_browser()

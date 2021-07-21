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

# imgcount+=scrape_all_sites('penne pasta',150)
# imgcount+=scrape_all_sites('macaroni pasta',150)
# imgcount+=scrape_all_sites('spaghetti pasta',150)
# imgcount+=scrape_all_sites('fettuccine pasta',150)

imgcount+=scrape_all_sites('chocolate chip cookie',150)
imgcount+=scrape_all_sites('snickerdoodle',150)
imgcount+=scrape_all_sites('sugar cookies',150)
imgcount+=scrape_all_sites('shortbread cookies',150)

imgcount+=scrape_all_sites('granny smith apple',150)
imgcount+=scrape_all_sites('fuji apple',150)
imgcount+=scrape_all_sites('red apple',150)
imgcount+=scrape_all_sites('green apple',150)

imgcount+=scrape_all_sites('coca cola can',150)
imgcount+=scrape_all_sites('pepsi can',150)
imgcount+=scrape_all_sites('sprite can',150)
imgcount+=scrape_all_sites('fanta can',150)

imgcount+=scrape_all_sites('vanilla ice cream cone',150)
imgcount+=scrape_all_sites('chocolate ice cream cone',150)
imgcount+=scrape_all_sites('chocolate ice cream scoop',150)
imgcount+=scrape_all_sites('vanilla ice cream scoop',150)

imgcount+=scrape_all_sites('chicken nuggets',150)
imgcount+=scrape_all_sites('chic fil a chicken nuggets',150)
imgcount+=scrape_all_sites('dino chicken nuggets',150)
imgcount+=scrape_all_sites('chicken nuggets big',150)

imgcount+=scrape_all_sites('plain burger',150)
imgcount+=scrape_all_sites('deluxe burger burger',150)
imgcount+=scrape_all_sites('burger',150)
imgcount+=scrape_all_sites('royale burger',150)

imgcount+=scrape_all_sites('french fries',150)
imgcount+=scrape_all_sites('mcdonalds french fries',150)
imgcount+=scrape_all_sites('burger king french fries',150)
imgcount+=scrape_all_sites('jack in the box french fries',150)

imgcount+=scrape_all_sites('salad',150)
imgcount+=scrape_all_sites('cobb salad',150)
imgcount+=scrape_all_sites('ceaser salad',150)
imgcount+=scrape_all_sites('southwest salad',150)

print(imgcount, 'images downloaded')
scraper.close_browser()

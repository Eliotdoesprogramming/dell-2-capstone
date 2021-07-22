# Image Classification using Tensor Flow


## Introduction

As a milestone in completing my Machine Learning training at Talent Path, our cohort was asked to create a project to showcase our skills within the Machine Learning space. With broad agency as to what sort of technologies to build, I set out to build a project that could showcase my ability to deliver quality product in less than ideal environments. In our training I felt that there was limited amounts of instruction towards nueral networks and image classification. To showcase my ability to learn rapidly and comprehensively, I decided that Image classification would be an excellent problem to challenge.

<div style="text-align:center"><iframe width="560" height="315" src="https://www.youtube.com/embed/NrmMk1Myrxc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

My project was inspired by Amazon's Go stores that they had opened initially in Seattle, and had expanded to other locations throughout the United States. I remember seeing these stores open up and thinking of how revolutionary the technology was. In Amazon's value proposition of these stores was as follows:


> "What if we could weave the most advanced machine learning computer vision and AI into the very fabric of a store so you never have to wait in line? No lines. No checkouts. No registers."

Combining that inspiration with the practical use cases came to me while talking with Stephen Logan about how Dell operates and what we should expect in our work with Dell. Something he mentioned was that for most products that Dell creates, it will be adopted internally before being used for the consumer market. This sparked the idea to build a prototype or first steps in creating a "Dell Go" store for Dell's internal employees. Could we allow Dell employees to grab their food and go, maximizing their productiveness making use of our own machine learning and computer vision technology?

# Project Model 1: Pizza Classification

The premise of my first model was building classifiers to accurately predict whether or not each food item is present from an employee's tray. This model would be one of many binary classification models that would predict whether or not a food item was present. In this case, the model will classify True or False based on whether an employee has pizza on their tray


## Data Collection:

My first step was gathering a dataset. An important step in the data science process is gathering and manipulating the data in order to process them into manageable pieces for our machine learning models. Because the premise of this project was to build many models to classify various food items, I wanted to make sure that I was able to build a dataset myself without relying on outside sources such as Kaggle to give pre-built, manicured image set. It was important to me that I had personal control of the data collection, including what types of images were used for each of the classes within my model.

<div style="text-align:center; "><img src="./images/selenium.png" style="max-height:400px;"></div>

The solution for this problem came in the form of a scraper built on selenium, a popular library used for automation and testing. 

<div style="text-align:center; "><img src="./images/2021-07-22-13-39-26.png" style="max-height:400px;"></div>

The scraper works by scrolling through an image search engine and collecting image source paths of the search result images. It then downloads them by interpreting their source paths. If the source path is a http url, it will use the request library to download the result of making a http get request to that url. That being said, not all image results are being stored as files on seperate servers. A large amount of images from these search results have images stored in base64 strings. Because of this, I wrote code that will determine if an image's source is a base64 string, and will take that string and encode an image file of the property format into the images folder storing my scraped results.

<div style="display:flex; max-height:300px; justify-content:space-around">
<img src="images/google.svg.png" style="width:30%"><img src="images/bing.svg" style="width:30%"><img src="images/yahoo.svg" style="width:30%">
</div>

The next hurdle was that each search engine limits the amount of search results per image search. I remedied this by searching google images, bing images, and yahoo images in order to increase the amount of image results I can get per search term. Between the three search engines, I could get approximately 1800 images per search term. Additionally a failsafe that I found to be nearly exclusive to google was that they will limit results further if you scrape their site too quickly. In order to remedy that, I added extra human delay and smooth scrolling to maximize the amount of results.


![](images/2021-07-22-14-05-57.png)

From there all that was left to do was build my dataset. For pizza classification I scraped a dataset of 10,000 images. 5,000 images of pizza and 5,000 images of not pizza.


## Model Building and Training




<div id="test" style="height:100px; width:100px;"></div>

<script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
<script type="text/javascript" src="requests.js">
# Image Classification using Tensor Flow
- [Try the Pizza model](#try-the-pizza-model)
- [Try the 10 food](#try-the-10-food-model)

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



<div style="text-align:center; "><img src="./images/2021-07-22-14-05-57.png" style="max-height:400px;"></div>


From there all that was left to do was build my dataset. For pizza classification I scraped a dataset of 10,000 images. 5,000 images of pizza and 5,000 images of not pizza.


## Model Building and Training

I moved all of the images into their own directories and converted them into 180x180x3 tensors to feed into my model, using a 80-20 split between training and validation

<div style="text-align:center; "><img src="./images/2021-07-22-15-26-29.png" style="max-height:400px;"></div>


after which, I verified that the images were correctly labeled by using matplotlib and PIL

<div style="text-align:center; "><img src="./images/2021-07-22-15-27-28.png" style="max-height:400px;"></div>


Next I built my Sequential keras model that preprocesses the image arrays to scale their red green blue values from 0-255 to 0-1. The model alternates between convolutional layers using a `relu` activation function and pooling layers 3 times and then flattens the layers and uses a Dense layer to make its final prediction.

<div style="text-align:center; "><img src="./images/2021-07-22-15-38-21.png" style="max-height:400px;"></div>



I compile the model using `adam` as my optimizer and `sparse categorical crossentropy` as my loss function. I then fit the model using a callback for early stopping on validation accuracy in order to maximize accuracy of my model. Additionally, the callback will restore the best weights effectively ensuring that it will maintain its highest accuracy across all epochs

<div style="text-align:center; "><img src="./images/2021-07-22-15-42-13.png" style="max-height:400px;"></div>

After 13 epochs, the rate of my model's learning slowed down and the early stopping callback kicked in. I then compared the predictions my model made to the actual labels assigned to the images.

<div style="text-align:center; "><img src="./images/2021-07-22-15-47-37.png" style="max-height:400px;"></div>

I found that my model worked extremely well, predicting correctly on our validation set 93% of the time. Additionally we kept strong f1 scores meaning that both are classes 0 being ``not pizza`` and 1 being ``pizza`` are well represented in the model.

taking it a step further, I used images not in the dataset to verify that the model did in fact correctly predict images as pizza and not pizza. 


<div style="text-align:center; "><img src="./images/2021-07-22-16-03-24.png" style="max-height:400px;"></div>

<div style="text-align:center; "><img src="./images/2021-07-22-16-05-40.png" style="max-height:400px;"></div>


The model even did well with images of food similar to pizza such as a frittata
<div style="text-align:center; "><img src="./images/2021-07-22-16-09-18.png" style="max-height:400px;"></div>


Finally, I trained the model on the whole dataset.

## Try the Pizza Model
If you want to try this model out yourself, I have it hosted in a Flask based api. Send the model an image's source and see what it predicts!

<div id="model1" class="card shadow-lg" style="display:flex; justify-content:center; padding:20px; margin:40px">
    <div class="input-group mb-3">
        <input type="text" class="form-control" placeholder="image url here" aria-label="" aria-describedby="basic-addon1" id="modelurl1">
        <div class="input-group-prepend">
            <button class="btn btn-outline-secondary" type="button" id="submit1">Submit Image URL</button>
        </div>
    </div>
</div>
<div id="model1result">
</div>

## Model 2: Multiclass Image Classification

The next approach I went to try with building an image classification model for Dell's employees was a multiclass classification approach where I would use a single model to identify multiple different types of foods.

### Data Collection
Following the same scraping methodology as model 1, I scraped bing, google and yahoo images to build my dataset. This time I scraped for 10 classes:

```python
classes = ['apple',
 'burger',
 'cookie',
 'fries',
 'ice-cream',
 'nuggets',
 'pasta',
 'pizza',
 'salad',
 'soda']
```
 Taking notes from my last attempt at data collecting, I had found that using more specific search terms generally gave better image results in the search engines so each of the classes had 3-4 specific sub searches to build the dataset. For example, apple's search terms consisted of ``granny smith apple, fuji apple, red apple, green apple`` 

 For each of the classes, I scraped 2000 images to train my model with for a total of 20,000 images.

 ### Model Building and Training

Following many of the same initial steps I used keras to pull the images from their directories and into my dataset.

I verified that my images were labeled correctly and started building my keras model

<div style="text-align:center; "><img src="./images/2021-07-23-12-23-07.png" style="max-height:400px;"></div>



My first model I built in the same methodology as the binary classification model, minimal image preprocessing only adjusting the amount of classes in the output.

<div style="text-align:center; "><img src="./images/2021-07-23-12-26-17.png" style="max-height:400px;"></div>


My model this time did reasonably with a 81% accuracy on the validation set. That being said, I wanted to see if I could get accuracy to the same level that I had seen previously with the binary classification
<div style="text-align:center; "><img src="./images/2021-07-23-12-32-52.png" style="max-height:400px;"></div>



Something else to note about the model is that it was fitted perfectly to the training set, with 100% accuracy and 0 categorical loss. Training the model for more epochs wouldn't give my model any more benefits, there had to be changes to the data that would help my model learn better.

### Data Augmentation
Seeing as the data was fitting too closely to our training dataset, I starting using image augmentation to manipulate the training set and allow our validation set to train for longer.

The first of the image augmentation methods I used was randomly applying rotational and horizontal flips to the image.

<div style="text-align:center; "><img src="./images/2021-07-23-12-46-50.png" style="max-height:400px;"></div>
<div style="text-align:center; "><img src="./images/2021-07-23-12-52-45.png" style="max-height:400px;"></div>


This extra layer of preprocessing did extremely well in having my model fit less closely to the training set
<div style="text-align:center; "><img src="./images/2021-07-23-12-48-24.png" style="max-height:400px;"></div>


What I found was that even after 50 epochs, my model was still learning! That being said, the rate at which my model learned was significantly hit. I ended up fitting again for another 40 epochs and got an 83% accurate model, slightly higher than the unaugmented images. That being said, this model was less tightly fitted to the training set, making it a more generalized acceptable model.

<div style="text-align:center; "><img src="./images/2021-07-23-12-58-54.png" style="max-height:400px;"></div>


Other methods of augmentation that I used were applying grayscale and color inversion by building custom keras layers to manipulate the image data.

<div style="text-align:center; "><img src="./images/2021-07-27-12-02-21.png" style="max-height:400px;"></div>
<div style="text-align:center; "><img src="./images/2021-07-23-13-00-55.png" style="max-height:400px;"></div>
<div style="text-align:center; "><img src="./images/2021-07-23-13-01-37.png" style="max-height:400px;"></div>


Unfortunately, both of these, especially the inversion significantly reduced the accuracy of my model leading me to believe that color is an important factor for this image classification model

## Model Testing
Like before, I trained my model with image flipping data augmentation on the whole dataset and then tested it with images found outside the dataset.

<div style="text-align:center; "><img src="./images/2021-07-23-13-07-32.png" style="max-height:400px;"></div>

<div style="text-align:center; "><img src="./images/2021-07-23-13-08-31.png" style="max-height:400px;"></div>

<div style="text-align:center; "><img src="./images/2021-07-23-13-09-47.png" style="max-height:400px;"></div>

### Try the 10 Food Model

As before, this model is hosted on a flask based api. 

```python
    classes = ['apple',
    'burger',
    'cookie',
    'fries',
    'ice-cream',
    'nuggets',
    'pasta',
    'pizza',
    'salad',
    'soda']
```

send the model an image's url from one of the above classes and see what it predicts!

<div id="model2" class="card shadow-lg" style="display:flex; justify-content:center; padding:20px; margin:40px">
    <div class="input-group mb-3">
        <input type="text" class="form-control" placeholder="image url here" aria-label="" aria-describedby="basic-addon1" id="modelurl2">
        <div class="input-group-prepend">
            <button class="btn btn-outline-secondary" type="button" id="submit2">Submit Image URL</button>
        </div>
    </div>
</div>
<div id="model2result">
</div>

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
<script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
<script type="text/javascript" src="requests.js">
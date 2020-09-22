<h1>web-scraping-challenge</h1>

<h2>Part One</h2>
The first part of the challenge was to scrape info about mars from four different websites.
To do this you will need to import the following:
<ul>
<li>import os</li>
<li>from bs4 import BeautifulSoup</li>
<li>import requests</li>
<li>from splinter import Browser</li>
<li>import pandas as pd</li>
</ul>

First, use BeautifulSoup to go to <a href="https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest">NASA Mars News Site</a> and pull the latest headline and paragraph text.

Next, use Splinter, to navigate the <a href="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars">JPL Space Images</a> and select the full size featured image. In order to use, Splinter you will need <a href="https://chromedriver.chromium.org/"> Web Chromedriver</a>

For the third scrape, use pandas to get the Mars Facts Table from <a href="https://space-facts.com/mars/">Mars Facts</a>

Last, pull the 4 hemisphere images and titles from <a href="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"> Astrogeology.usgs.gov</a>

<h2>Part Two</h2>
Use the scrape function to add the info that you scraped to MongoDB. Don't forget to open mongo in your terminal. 

Using Flask, create a route that will pass your Mars data from your MongoDB and display using HTML.
To do this you will need:
<ul>
<li>from flask import Flask, render_template, redirect, url_for</li>
<li>from flask_pymongo import PyMongo</li>
<li>from jinja2 import Environment, select_autoescape</li>
<li>import scrape_mars(your final scrape document)</li>
</ul>


You should end up with something that looks like this:
<img src="images/screenshot"


<h1>web-scraping-challenge</h1>

<h2>Part One</h2>
The first part of the challenge was to scrape info about mars from four different websites.
To do this you will need to import the following:
<ul>
<li>*import os</li>
*from bs4 import BeautifulSoup
*import requests
*from splinter import Browser
*import pandas as pd
</ul>

First, use BeautifulSoup to go to <a href="https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest">NASA Mars News Site</a> and pull the latest headline and paragraph text.



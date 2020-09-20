# Dependencies
import os
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import pandas as pd

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    mars_info = {}
    browser = init_browser()

    # visit NASA'a mars News Site and get the latest headline and paragrph text
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

    html = requests.get(url).text
    soup = bs(html, 'lxml')
    news_title = soup.find('div', class_="content_title").text.strip()
    news_p = soup.find("div", class_="rollover_description_inner").text.strip()
    mars_info["news_title"]=news_title
    mars_info["news_paragraph"]=news_p

    #go to JPL Space images and get the full size featured image
    url="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    image_element = browser.find_by_id("full_image")
    image_element.click()
    browser.is_element_present_by_text("more info", wait_time=2)
    more_info = browser.links.find_by_partial_text('more info')
    more_info.click()
    html = browser.html
    soup = bs(html, 'html.parser')
    result= soup.find("figure", class_="lede")
    for link in result("a"):
        image_url = link.get("href")
        featured_image_url = url+image_url
    
    mars_info["featured_image_url"]=featured_image_url
    
    #got to spacefacts/mars to get mars facts table
    url = "https://space-facts.com/mars/"
    mars_table = pd.read_html(url)
    mars_df = mars_table[0]
    mars_df.columns = ["Description","Mars"]
    mars_df.set_index('Description', inplace=True)
    mars_table=mars_df.to_html()
    mars_info["mars_table"]=mars_table
    
    #get full size images of mars hemispheres from USGS Astrogeology 
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    result= soup.find_all("a", class_="itemLink product-item")
    link_list = []
    base_url = "https://astrogeology.usgs.gov"
    for link in result:
        if link["href"] not in link_list:
            link_list.append(link["href"])
    image_links = [base_url + link for link in link_list]
    hemisphere_images = []
    for link in image_links:
        hemisphere_info = {}
        browser.visit(link)
        html = browser.html
        soup = bs(html, 'html.parser')
        image_url = soup.find("img", class_="wide-image")["src"]
        title = soup.find("h2", class_="title").text
        hemisphere_info["title"] = title
        hemisphere_info["image_url"] = base_url + image_url
        hemisphere_images.append(hemisphere_info)
        browser.back()
    
    mars_info["hemispheres"]=hemisphere_images 
    browser.quit()

    return mars_info
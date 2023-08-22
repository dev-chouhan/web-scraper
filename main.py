""" Web Scraper
We use 3 methods to scrap website data:
1 Get the HTML
    1.1 Find the URL that you want to scrape.
    1.2 Inspect the Page.
    1.3  Find the data you want to extract.
2 Parse the HTML
    2.1 Fetched data will be in string formate, we need to parse it to tree-transversal.
3 HTML tree tranversal
    3.1 Use beautifulsoup to transverse data to required tree structure and use as required/store it in any data file.

"""

#! Step 0: install all requirments
import requests
from bs4 import BeautifulSoup
url = "https://www.roumarcellus.com"

#! Step 1: Get the HTML
r = requests.get(url) #? to get request from url
htmlContent = r.content
# print(htmlContent) #? To view whole html file in console


#! Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify) #? To view whole html in pretty formate


#! Step 3: HTML tree transversal
title = soup.title #? Get the title of HTML page

# paras = soup.find_all("p") #? Get all the paragraphs from the page

# print(soup.find('p')['class']) #? Get class of first para element in HTML

# print(soup.find_all("p", class_="container")) #? Find all elements with class "container"

# print(soup.find('p').get_text()) #? Get text from tag/soup

#? Get all the links on the page
anchors = soup.find_all('a')
all_links = set()
for link in anchors:
    linkBack = link.get('href')
    if(linkBack != '#'):
        linkHeader = ""
        if(linkBack[:5] != "https"):
            linkHeader = url
        linkText = linkHeader + linkBack
        all_links.add(linkText)

for i in all_links:
    print(i)


#? Get all the elements from NavBar
navbarSupportesContent = soup.find(id="nav-content")
# for item in navbarSupportesContent.stripped_strings:
#     print(item)

# print(soup.select(".m-auto")) #? To select any id or class element from HTML
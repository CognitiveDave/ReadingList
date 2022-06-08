# -*- coding: utf-8 -*-
"""
Reading List exploration file
Exploring concepts and approaches to solving the problem
"""
#Step 1 - loading the browser and preparing for automation
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
chrome_options = webdriver.ChromeOptions()
# Comment the next line if you want to see what
# happens in the browser during the execution
# of selenium
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

#step 2 - add extra libraries bs4 and time for page interaction
from bs4 import BeautifulSoup
import time



#step 3 - define some key variables
urlSignIn = ""

url = "https://medium.com/@cognitivedave/list/reading-list" #url for the reading list

wd.get(urlSignIn) #Sign in first

time.sleep(10) #wait a few seconds to allow pre and post JS events and full page load

wd.get(url) #navigate to the reading list and wait
time.sleep(10)

# ------------------------------------------------------------
# get the max height and full scroll the page to get all articles
# https://medium.com/@dreamferus/how-to-scrape-code-from-medium-using-python-f51d68f91bd1
height = 0
latest_height = 1

# scroll through the page iteratively until we reach the max height
while (height < latest_height):
    latest_height = wd.execute_script('return document.body.scrollHeight')
    
    for y in range(height, latest_height, 200):
        wd.execute_script(f"window.scrollTo(0, {y})")
        # wait a little bit
        time.sleep(.5)
        
    height = latest_height
    
    latest_height = wd.execute_script('return document.body.scrollHeight')
# ------------------------------------------------------------

# provide the full html into beautifulsoup
soup = BeautifulSoup(wd.page_source, features="lxml")
articles = soup.find_all('article')
Removebuttons = soup.find_all('div','tv l tw')
print(f"There are {len(articles)} articles with {len(Removebuttons)} articles having been deleted for a total of {len(articles)+len(Removebuttons)}")
wd.close()


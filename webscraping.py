from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

import time


browser = webdriver.Chrome('chromedriver.exe')

url = "https://www.amazon.fr/"


def getHTML(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return(soup)

def openURL(url):
    browser.get(url)
    time.sleep(2)

openURL(url)

def search(keyword, browser):
    search = browser.find_element_by_id('twotabsearchtextbox')
    search.send_keys(keyword)
    search.send_keys(Keys.ENTER)
    time.sleep(3)


def getContent(browser):
    soup = getHTML(browser.current_url)
    mydivs = soup.findAll("div", {"class": "sg-col-inner"})
    return(mydivs)

search("the witcher", browser)
print(getContent(browser))


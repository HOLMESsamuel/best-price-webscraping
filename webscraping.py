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
header = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"} 


def getHTML(url, header):
    page = requests.get(url, headers=header)
    soup = BeautifulSoup(page.content, "html.parser")
    return(soup)

def openURL(url):
    browser.get(url)

openURL(url)

def search(keyword, browser):
    search = browser.find_element_by_id('twotabsearchtextbox')
    search.send_keys(keyword)
    search.send_keys(Keys.ENTER)


def getContent(browser, header, type, selector):
    soup = getHTML(browser.current_url, header)
    mydivs = soup.findAll(type, {"class": selector})
    return(mydivs)

search("the witcher", browser)
prices = getContent(browser, header, "span", "a-price-whole")
titles = getContent(browser, header, "span", "a-size-medium a-color-base a-text-normal")

for price, title in zip(prices, titles):
    print(price.text, title.text)

browser.quit()


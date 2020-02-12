from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time


browser = webdriver.Chrome('chromedriver.exe')

url = "https://www.oui.sncf/"
header = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"} 


def getHTML(url, header):
    page = requests.get(url, headers=header)
    soup = BeautifulSoup(page.content, "html.parser")
    return(soup)

def openURL(url):
    browser.get(url)



def search(origin, destination,age, browser):
    search = browser.find_element_by_id('vsb-origin-train-launch')
    search.send_keys(origin)
    time.sleep(3)
    search.send_keys(Keys.ENTER)
    search = browser.find_element_by_id('vsb-destination-train-launch')
    search.send_keys(destination)
    time.sleep(3)
    search.send_keys(Keys.ENTER)
    select = Select(browser.find_element_by_id('passenger_1_train-launch-typos-in-card-typology'))
    select.select_by_visible_text('12-25 ans')
    search = browser.find_element_by_id('passenger_1_train-launch-typos-in-card_age')
    search.send_keys(age)
    


def getContent(browser, header, type, selector):
    soup = getHTML(browser.current_url, header)
    mydivs = soup.findAll(type, {"class": selector})
    return(mydivs)



openURL(url)
search("Gare de l'Est (Paris) (Île-de-France)", "Metz Ville (Grand Est)","21", browser)



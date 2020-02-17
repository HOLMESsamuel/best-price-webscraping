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

#my favorite destinations
paris = "Gare de l'Est (Paris) (Île-de-France)"
metz = "Metz Ville (Grand Est)"
browser = webdriver.Chrome('chromedriver.exe')

url = "https://www.oui.sncf/"
header = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"} 


def getHTML(url, header):
    page = requests.get(url, headers=header)
    soup = BeautifulSoup(page.content, "html.parser")
    return(soup)

def click_on_button(browser, selector):
    try:
        button = browser.find_element_by_id(selector)
    except:
        button = browser.find_element_by_class_name(selector)
    button.click()

def fill_text_area(browser, selector, text, click=True):
    try:
        text_area = browser.find_element_by_id(selector)
    except:
        text_area = browser.find_element_by_class_name(selector)
    text_area.send_keys(text)
    time.sleep(1)
    if(click):
        text_area.send_keys(Keys.ENTER)

def select_option(browser, selector, option):
    try:
        select = Select(browser.find_element_by_id(selector))
    except:
        select = Select(browser.find_element_by_class_name(selector))
    select.select_by_visible_text(option)
    
  
def search(origin, destination, age, aller, browser):
    fill_text_area(browser, 'vsb-origin-train-launch', origin)
    fill_text_area(browser, 'vsb-destination-train-launch', destination)
    select_option(browser, 'passenger_1_train-launch-typos-in-card-typology', '12-25 ans')
    fill_text_area(browser,'passenger_1_train-launch-typos-in-card_age', age, False)
    click_on_button(browser, "vsb-dates-dialog-train-launch-aller-retour-1")
    time.sleep(1)
    click_on_button(browser, 'train-launch-d-'+aller)
    time.sleep(1)
    click_on_button(browser, 'vsb-datepicker-train-launch-aller-retour-submit')
    time.sleep(1)
    click_on_button(browser, 'vsb-passenger_1_train-launch-options-button')
    select_option(browser, 'passenger_1_train-launch-discount-card-type', 'TGVmax')
    time.sleep(1)
    fill_text_area(browser, 'passenger_1_train-launch-discount-card-dateofbirth', "06/03/1998")
    fill_text_area(browser, 'passenger_1_train-launch-discount-card-number', '500358789')
    click_on_button(browser, 'oui-modal__close-light___42122')
    time.sleep(1)
    click_on_button(browser, 'vsb-booking-train-launch-submit')
    
    
    

def getContent(browser, header, type, selector):
    soup = getHTML(browser.current_url, header)
    mydivs = soup.findAll(type, {"class": selector})
    return(mydivs)



browser.get(url)
browser.maximize_window()
search(paris, metz,"21","19-02-2020", browser)
time.sleep(20)
#browser.quit()


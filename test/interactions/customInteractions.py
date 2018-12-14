from selenium import webdriver
from userinterface.pages.googleMain import SEARCH_BUTTON
from userinterface.pages.googleMain import SEARCH_INPUT_BAR
from userinterface.pages.googleMain import SOURCE_LANGUAGE

def writeOnSearchBar(driver : webdriver.Chrome,theText) -> webdriver:
    driver.find_element_by_xpath(SEARCH_INPUT_BAR).send_keys(theText)

def clickOnSearchButton(driver : webdriver.Chrome) -> webdriver:
    driver.find_element_by_xpath(SEARCH_BUTTON).click()

def writeOnSourceLanguageInputThe(driver : webdriver.Chrome,text) -> webdriver:
    driver.find_element_by_id(SOURCE_LANGUAGE).send_keys(text)
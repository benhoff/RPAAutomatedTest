from selenium import webdriver
from interactions.customInteractions import clickOnSearchButton
from interactions.customInteractions import writeOnSearchBar
from interactions.customInteractions import writeOnSourceLanguageInputThe
from questions.googleTranslateQuestions import checkTheTranslation


def translate(driver : webdriver.Chrome,**kwargs) -> webdriver:
    writeOnSourceLanguageInputThe(driver,kwargs['The'])

def AsTranslation(driver : webdriver.Chrome,**kwargs) -> webdriver:
    checkTheTranslation(driver,kwargs['The'])

def  goToGoogleTranslate(driver : webdriver.Chrome,**kwargs) -> webdriver:
    writeOnSearchBar(driver,kwargs['SearchingBy'])
    clickOnSearchButton(driver)


if __name__=='__main__':
    writeOnSearchBar()
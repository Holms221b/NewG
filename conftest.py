import pytest
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.firefox.options import Options





@pytest.fixture()
def browser():
    # options = Options()
    # options.add_argument('--headless')
    ##browser = webdriver.Firefox(options=options)
    browser = webdriver.Chrome() #(options=options)
    wait = WebDriverWait(browser,timeout=10)
    # browser.maximize_window()
    #browser.implicitly_wait()wait(5) #неявное ожидание подождать(3 сек), не успевает кликнуть из-за быстрой подгрузки
    yield browser,wait

    #browser.close()
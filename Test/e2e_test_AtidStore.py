from selenium import webdriver
from selenium.webdriver.common.by import By
from BaseTest.locators import *
from test_AtidStore import *
from time import sleep


def test_search_product_Using_findElements():
    driver = webdriver.Chrome()
    driver.get(atidStore_WebAddress)
    driver.maximize_window()
    sleep(1)
    driver.find_element(By.XPATH, store_categoryHeader).click()  # click on "Store" Product Catagory button.
    ul_nav = driver.find_element(By.XPATH,Nav_Ul)
    li_nav = ul_nav.find_elements(By.TAG_NAME, Nav_Li)
    for i in li_nav:
        if i.text == "ATID Green Tshirt":
            i.click()
            break

from selenium import webdriver
from Locators.locators import *
from time import sleep
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class BaseTest:
    # In this test we can check the in two web drivers(Chrome & FireFox)
    driver = webdriver.Chrome()  # the web driver which we are going to use is Chrome
    # driver = webdriver.Firefox()  # the web driver which we are going to use is FireFox

    def initial(self):
        self.driver.get(atidStore_WebAddress)                                         # Get used to get the URL in the driver
        self.driver.maximize_window()                                                 # Maximize web window
        sleep(1)                                                                      # It is the page load timeout sec
        HomePage = self.driver.title                                                   # find AtidStore HomePage
        assert 'ATID Demo Store – ATID College Demo Store for Practicing QA Automation' == HomePage  # Check if AtidStoreHomePage displayed
        return self.driver

    def tear_down(self):
        self.driver.implicitly_wait(5)
        self.driver.close()

    def click(self, path_locators):
        return self.driver.find_element(By.XPATH, path_locators).click()

    def text_xpath(self, path_locators):
        return self.driver.find_element(By.XPATH, path_locators).text

    def text_tagName(self, path_locators):
        return self.driver.find_element(By.TAG_NAME, path_locators).text

    def send_key(self, path_locators, text):
        return self.driver.find_element(By.XPATH, path_locators).send_keys(text)

    def title(self, path_locators):
        return self.driver.find_element(By.XPATH,path_locators).text

    def title_display(self,text):
        try:
            return self.driver.find_element(By.TAG_NAME, text).text
        except NoSuchElementException:
            return ''

    def ul_(self, path_locators):
        return self.driver.find_element(By.XPATH, path_locators)

    def ul_elements(self, path_locators):
        return self.driver.find_elements(By.XPATH, path_locators)

    def li_(self,path_locators):
        return self.driver.find_elements(By.TAG_NAME, path_locators)


def is_element_exist(text, webElement):
    try:
        return webElement.find_element(By.CLASS_NAME, text).text
    except NoSuchElementException:
        return ''

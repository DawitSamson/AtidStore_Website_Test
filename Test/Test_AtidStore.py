from selenium import webdriver
from selenium.webdriver.common.by import By
from AtidStore_Website_Test.BaseTest.locators import *
from time import sleep


def test_Functionality_of_adding_Product_from_StoreCatagory_into_cart():
    driver = webdriver.Firefox()  # the web driver which we are going to use
    driver.get(atidStore_WebAddress)  # Get used to get the URL in the driver
    driver.maximize_window()  # Maximize web window
    sleep(2)  # It is the page load timeout sec
    driver.find_element(By.XPATH, store_categoryHeader).click()  # click on "Store" Product Catagory button
    sleep(2)
    driver.find_element(By.XPATH, store_SelectProductBody).click()  # click on the product "Black Hoodie"
    sleep(2)
    driver.find_element(By.XPATH, store_AddToCart).click()  # Click add to cart button
    sleep(2)
    driver.find_element(By.XPATH, store_ViewCart).click()  # View cart button
    sleep(2)
    product_name_element = driver.find_element(By.XPATH, store_ContainProductName).text  # find product name
    assert "ATID Black Shoes" == product_name_element
    sleep(5)
    driver.close()


def test_Functionality_of_adding_item_from_MenCatagory_into_cart():
    driver = webdriver.Firefox()  # the web driver which we are going to use
    driver.get(atidStore_WebAddress)  # Get used to get the URL in the driver
    driver.maximize_window()  # Maximize web window
    sleep(2)  # It is the page load timeout sec
    driver.find_element(By.XPATH, Men_categoryHeader).click()  # click on "Men" Product Catagory button
    sleep(2)
    driver.find_element(By.XPATH, Men_SelectProductBody).click()  # Click on the product "Dark Blue Denim Jeans"
    sleep(2)
    driver.find_element(By.XPATH, Men_AddToCart).click()  # Click add to cart button
    sleep(2)
    driver.find_element(By.XPATH, Men_ViewCart).click()  # View cart button
    sleep(2)
    product_name_element = driver.find_element(By.XPATH, Men_ContainProductName).text  # Find product name
    assert "Dark Blue Denim Jeans" == product_name_element
    sleep(5)
    driver.close()


def test_Functionality_of_adding_item_from_WomenCatagory_into_cart():
    driver = webdriver.Firefox()  # the web driver which we are going to use
    driver.get(atidStore_WebAddress)  # Get used to get the URL in the driver
    driver.maximize_window()  # Maximize web window
    sleep(2)  # It is the page load timeout sec
    driver.find_element(By.XPATH, Women_categoryHeader).click()  # click on "Women" Product Catagory button
    sleep(2)
    driver.find_element(By.XPATH, Women_SelectProductBody).click()  # click on the product "Blue Denim Shorts"
    sleep(2)
    driver.find_element(By.XPATH, Women_AddToCart).click()  # Click add to cart button
    sleep(2)
    driver.find_element(By.XPATH, Women_ViewCart).click()  # View cart button
    sleep(2)
    product_name_element = driver.find_element(By.XPATH, Women_ContainProductName).text  # Find product name
    assert "Blue Denim Shorts" == product_name_element
    sleep(5)
    driver.close()


def test_Functionality_of_adding_item_from_AccessoriesCatagory_into_cart():
    driver = webdriver.Firefox()  # the web driver which we are going to use
    driver.get(atidStore_WebAddress)  # Get used to get the URL in the driver
    driver.maximize_window()  # Maximize web window
    sleep(2)  # It is the page load timeout sec
    driver.find_element(By.XPATH, Accessories_categoryHeader).click()
    sleep(2)
    driver.find_element(By.XPATH, Accessories_SelectProductBody).click()  # Click on the product "Buddha Bracelet"
    sleep(2)
    driver.find_element(By.XPATH, Accessories_AddToCart).click()  # Click add to cart button
    sleep(2)
    driver.find_element(By.XPATH, Accessories_ViewCart).click()  # View cart button
    sleep(2)
    product_name_element = driver.find_element(By.XPATH, Accessories_ContainProductName).text  # Find product name
    assert "Buddha Bracelet" == product_name_element
    sleep(5)
    driver.close()


def test_Functionality_of_inserting_CouponCode_Work_Properly():
    driver = webdriver.Firefox()  # the web driver which we are going to use
    driver.get(atidStore_WebAddress)  # Get used to get the URL in the driver
    driver.maximize_window()  # Maximize web window
    sleep(2)  # It is the page load timeout sec
    driver.find_element(By.XPATH, Coupons_categoryHeader).click()  # click on "Store" Product Catagory button
    sleep(2)
    driver.find_element(By.XPATH, Coupons_SelectProductBody).click()  # click on the product "Anchor Bracelet"
    sleep(2)
    driver.find_element(By.XPATH, Coupons_AddToCart).click()  # Click add to cart button
    sleep(2)
    driver.find_element(By.XPATH, Coupons_ViewCart).click()  # View cart button
    sleep(2)
    product_name_element = driver.find_element(By.XPATH, Coupons_ContainProductName).text  # find product name
    assert "Anchor Bracelet" == product_name_element
    coupon_code = driver.find_element(By.XPATH, Coupons_InsertCode)
    sleep(2)
    coupon_code.clear()
    coupon_code.send_keys("123")
    sleep(2)
    driver.find_element(By.XPATH, Apply_CouponCode).click()
    errorText_element = driver.find_element(By.XPATH, Error_Message_Xpath).text
    assert 'Coupon "123" does not exist!' == errorText_element
    sleep(5)
    driver.close()

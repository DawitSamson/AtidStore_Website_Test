from Test.BaseTest.base import *
from Test.Web.Contact_Us.test_Atidstore_contactUs import Test_ContactUs_Message


# E2E(end to end) process checking on Atid Demo store
class Test_E2E(BaseTest):
    def test_E2E_Process_of_Sending_message_To_admin_via_contact_us_screen(self):
        SEND_MESSAGE = Test_ContactUs_Message()
        SEND_MESSAGE.test_send_question_toThe_site_admin_via_contact_us_screen()

    def test_E2E_Process_of_SearchProduct_and_Display(self):
        SEARCH = super()
        SEARCH.initial()                                                       # Initial Web address
        SEARCH.click(Search_Path)                                               # Click on the search button
        SEARCH.send_key(INPUT_onSearch_Box, 'Bright Red Bag')                   # enter Firstname
        SEARCH.click(Search_Path)                                               # Click on the search button
        search_result = SEARCH.text_xpath(Search_Display)                       # find the Search product page
        assert 'Bright Red Bag' == search_result                                # Display search result
        SEARCH.tear_down()

    def test_E2E_Process_of_Enter_Coupon_Code(self):
        COUPONCODE = super()
        COUPONCODE.initial()                                       # Initial Web address
        COUPONCODE.click(Store_categoryPage)                       # Click on "Store" Product Catagory button.
        COUPONCODE.click(Black_Hoodie)                             # Click on the product "Black Hoodie"
        COUPONCODE.click(AddToCart)                                # Click add to cart button
        COUPONCODE.click(ViewCart)                                 # Click cart view
        product_name = COUPONCODE.text_xpath(Product_blackHoodie)        # Find product name
        assert 'Black Hoodie' == product_name                      # Display The product in cart view page
        COUPONCODE.click(Process_ToCheckOut)                       # Click Process to check out
        checkout_page = COUPONCODE.driver.title                     # Find the checkout page
        assert checkout_page == "Checkout – ATID Demo Store"           # Display  Check out page
        COUPONCODE.click(Coupons_Link)                                # Click Coupon box
        COUPONCODE.send_key(Coupons_Enter,"dawit123")                 # Enter Coupon Code
        COUPONCODE.click(Apply_Coupon_Button)                          # Click Apply Coupon Button
        errorText_element = COUPONCODE.text_xpath(Coupons_Enter_Error_text)    # Find error message
        assert 'Coupon "dawit123" does not exist!' == errorText_element  # DISPLAY error message
        COUPONCODE.tear_down()

    def test_E2E_Process_of_Login(self):
        LOGIN = super()
        LOGIN.initial()                                            # Initial Web address
        LOGIN.click(Store_categoryPage)                            # Click on "Store" Product Catagory button.
        LOGIN.click(Store_SelectProductBody)                       # Click on the product "ATID Black Shoes"
        LOGIN.click(AddToCart)                                     # Click add to cart button
        LOGIN.click(ViewCart)                                      # Click cart view
        product_name = LOGIN.text_xpath(Store_ContainProductName)         # Find product name
        assert "ATID Black Shoes" == product_name                  # Display The product in cart view page
        LOGIN.click(Process_ToCheckOut)                            # Click Process to check out
        checkout_page = LOGIN.driver.title                         # Find the checkout page
        assert checkout_page == "Checkout – ATID Demo Store"       # Display Check out page
        LOGIN.click(Login_Link)                                   # Click Login link
        LOGIN.send_key(UserName_Input,"dada1999@gmail.com")        # Enter Username or email address
        LOGIN.send_key(Password_Input, "password12345")            # Enter Password
        LOGIN.click(Login_Button)                                   # Click Login Button
        Unknown_email_address_error = LOGIN.text_xpath(Unknown_email_address)  # Find error text
        assert 'Unknown email address. Check again or try your username.' == Unknown_email_address_error  # Display error text
        LOGIN.tear_down()

    def test_E2E_Process_of_ForgetPassword(self):
        FORGETPASSWORD = super()
        FORGETPASSWORD.initial()                                   # Initial Web address
        FORGETPASSWORD.click(Store_categoryPage)                   # click on "Store" Product Catagory button.
        FORGETPASSWORD.click(Store_SelectProductBody)               # click on the product "ATID Black Shoes"
        FORGETPASSWORD.click(AddToCart)                             # Click add to cart button
        FORGETPASSWORD.click(ViewCart)                              # Click cart view
        product_name = FORGETPASSWORD.text_xpath(Store_ContainProductName)  # find product name
        assert "ATID Black Shoes" == product_name                    # Display The product in cart view page
        FORGETPASSWORD.click(Process_ToCheckOut)                     # Click Process to check out
        checkout_page = FORGETPASSWORD.driver.title                 # Find the checkout page
        assert checkout_page == "Checkout – ATID Demo Store"         # Display Check out page
        FORGETPASSWORD.click(Login_Link)                            # Click Login link
        FORGETPASSWORD.click(Lost_Password_Link)                       # Click Lost your ForgetPassword? link
        myAccount_page = FORGETPASSWORD.driver.title                                # find My Account Page
        assert "My account – ATID Demo Store" == myAccount_page           # Display My Account page
        FORGETPASSWORD.send_key(MyAccount_email_Input,"dada1999@gmail.com")  # enter Username or email address
        FORGETPASSWORD.click(ResetPassword_Button)                            # Click ResetPassword Button
        forgetPassword_email_error = FORGETPASSWORD.text_xpath(ForgetPassword_invalid_error)         # Find error text
        assert 'Invalid username or email.' == forgetPassword_email_error               # display error message
        FORGETPASSWORD.tear_down()

    def test_E2E_Process_of_MenCatagory_from_Product_Selection_to_PlaceOrder(self):
        ORDER = super()
        ORDER.initial()                                                 # Initial Web address
        ORDER.click(Men_categoryPage)                                   # Click on "Men" Product Catagory button
        ORDER.click(AtidBlueShoes_Path)                                 # Click on the product "ATID Blue Shoes'"
        ORDER.click(AddToCart)                                          # Click add to cart button
        ORDER.click(ViewCart)                                           # Click cart view
        product_name_element = ORDER.text_xpath(AtidBlueShoes_Name)            # Find product name
        assert 'ATID Blue Shoes' == product_name_element                 # Display The product in cart view page
        ORDER.click(Process_ToCheckOut)                                  # Click Process to check out
        checkout_page = ORDER.driver.title                               # Find the checkout page
        assert checkout_page == "Checkout – ATID Demo Store"             # Display Check out page
        # Billing details form
        ORDER.send_key(Firstname,"david")                                     # enter Firstname
        ORDER.send_key(Lastname, "belay")                                     # enter Lastname
        ORDER.send_key(Companyname,"david_Plc")                               # enter Company name
        ORDER.send_key(HouseAddress,"Beer-Sheva")                             # enter Home Address
        ORDER.send_key(Apartment,"105")                                       # enter Apartment number
        ORDER.send_key(ZipCode,"8420000")                                     # enter Country Zip Code
        ORDER.send_key(Town,"Beer Sheva")                                     # enter Town/City
        ORDER.send_key(PhoneNumber,"0567891236")                               # enter Phone number
        ORDER.send_key(EmailForShipment,"Example@gmail.com")                   # enter Email address
        ORDER.driver.implicitly_wait(3)                                        # It is the page load timeout 3 sec
        ORDER.click(Place_Order_Button)                                         # Click on Place Order
        invalid_PaymentMethod = ORDER.text_xpath(Invalid_Payment_Error)               # Find Payment error message
        assert 'Invalid payment method.' == invalid_PaymentMethod         # Display invalid payment method error message
        ORDER.tear_down()

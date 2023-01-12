from Test.BaseTest.base import *


# Send Question to the site admin via Contact Us screen (Bonus)
class Test_ContactUs_Message(BaseTest):
    def test_send_question_toThe_site_admin_via_contact_us_screen(self):
        CONTACTUS = super()
        CONTACTUS.initial()                                 # Initial Web address
        CONTACTUS.click(ContactUs_Path)                     # Click on contact us page
        thanksMessage = CONTACTUS.text_xpath(ContactUs_Page)      # find ContactUs page
        assert "Contact Us" == thanksMessage                 # Check if contact us page displayed
        CONTACTUS.send_key(Questionar_Name_Input,"david")      # Enter name of the questioner
        CONTACTUS.send_key(Questionar_Subject_Input,"How to apply Coupon")   # Enter Subject of the questioner
        CONTACTUS.send_key(Questionar_Email_Input,"example@gmail.com")      # Enter Email of the questioner
        CONTACTUS.send_key(Questionar_Message_Input,"Hi AtidStore how to apply Coupon from the cart page")  # Enter SMS
        CONTACTUS.click(Send_Message)                                             # Click send message
        thanksMessage = CONTACTUS.text_xpath(Thanks_forContactingUs_text)              # Thanks for Contacting us text page
        assert 'Thanks for contacting us! We will be in touch with you shortly.' == thanksMessage  # Check if Thanks text displayed
        CONTACTUS.tear_down()

        # driver = super().initial()
        # driver.find_element(By.XPATH, ContactUs_Path).click()  # Click on contact us page
        # thanksMessage = driver.find_element(By.XPATH, ContactUs_Page).text  # find ContactUs page
        # assert "Contact Us" == thanksMessage  # Check if contact us page displayed
        # questioner_Name = driver.find_element(By.XPATH, Questionar_Name_Input)
        # questioner_Name.send_keys("david")
        # questioner_Subject = driver.find_element(By.XPATH, Questionar_Subject_Input)
        # questioner_Subject.send_keys("How to apply Coupon")
        # questioner_Email = driver.find_element(By.XPATH, Questionar_Email_Input)
        # questioner_Email.send_keys("example@gmail.com")
        # questioner_Message = driver.find_element(By.XPATH, Questionar_Message_Input)
        # questioner_Message.send_keys("Hi AtidStore how to apply Coupon from the cart page")
        # driver.find_element(By.XPATH, Send_Message).click()
        # thanksMessage = driver.find_element(By.XPATH,
        #                                     Thanks_forContactingUs_text).text  # Thanks for Contacting us text page
        # assert 'Thanks for contacting us! We will be in touch with you shortly.' == thanksMessage  # Check if Thanks text displayed
        # super().tear_down()
        #
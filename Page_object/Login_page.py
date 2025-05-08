
#import all necessary dependencies
from selenium.webdriver.common.by import By
from Page_object.Home_page import BasePage
from Test_Locators.locators import Locators
from Test_Data.data import Data


#creating class for login page

class LoginPage(BasePage):
    # store all the locators
    username_input = (By.XPATH, Locators.username_input_locator)
    password_input = (By.XPATH, Locators.password_input_locator)
    login_button = (By.XPATH, Locators.login_button_locator)
    drop_down_button=(By.XPATH,Locators.drop_down_button_locator)
    logout_button=(By.XPATH,Locators.logout_button_locator)
    pop_up_box_button=(By.XPATH,Locators.pop_up_box)

    # creating enter_username function to enter the text in username textbox
    def enter_username(self, username):
        self.enter_text(self.username_input, username)

    # creating enter_password function to enter the text in password textbox
    def enter_password(self, password):
        self.enter_text(self.password_input, password)

    # creating click_login function to click the login button
    def click_login(self):
        self.click(self.login_button)
        self.Url_change(Data.dashboard_url)

    # creating validate_username function to validate the username in textbox
    def validate_username(self):
        return self.is_visible(self.username_input)

    # creating validate_password function to validate the password in textbox
    def validate_password(self):
        return self.is_visible(self.password_input)

    # creating click_dropdown function to click the profile drop_down button
    def click_dropdown(self):
        self.click(self.drop_down_button)

    # creating click_pop_up_box function to click the pop_up box close button
    def click_pop_up_box(self):
        self.click(self.pop_up_box_button)

    # creating click_logout_button function to click the logout button
    def click_logout_button(self):
        self.click(self.logout_button)

#import all necessary dependencies
from Page_object.Home_page import BasePage
from Page_object.Login_page import LoginPage
from Test_Data.data import Data
from Configuration.conftest import driver


#Creating test case to check the base url
def test_url(driver):
    driver.get(Data.url)
    base_page = BasePage(driver)
    assert base_page.fetch_url() == Data.url
    print("SUCCESS, URL is valid!")

#Creating test case to validate the username in text box

def test_validate_username_input(driver):
    driver.get(Data.url)
    login_page = LoginPage(driver)
    username_input_box = login_page.validate_username()
    assert username_input_box == True
    print("SUCCESS: Username input box is validated!")

#Creating test case to validate the password in text box

def test_validate_password_input(driver):
    driver.get(Data.url)
    login_page = LoginPage(driver)
    password_input_box = login_page.validate_password()
    assert password_input_box == True
    print("SUCCESS: Password input box is validated!")

#Creating test case for validate login button

def test_login(driver):
    driver.get(Data.url)
    login_page = LoginPage(driver)
    login_page.enter_username(Data.username)
    login_page.enter_password(Data.password)
    login_page.click_login()
    assert Data.dashboard_url == driver.current_url
    print("SUCCESS: Login Successful")

#Creating test case for validate logout button

def test_logout_button(driver):
    driver.get(Data.url)
    login_page = LoginPage(driver)
    login_page.enter_username(Data.username)
    login_page.enter_password(Data.password)
    login_page.click_login()
#Creating method to click the extra pop_up box in dashboard page
    login_page.click_pop_up_box()
    login_page.click_dropdown()
    login_page.click_logout_button()
    driver.get(Data.url)
    base_page = BasePage(driver)
    assert base_page.fetch_url() == Data.url
    print("SUCCESS, Account Logged out")
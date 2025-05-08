#import all necessary dependencies
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException

#Creating Class
class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15
#creating find element function
    def find_element(self, locator):
        try:
            web_element = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
            return web_element
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR")

# creating find elements function
    def find_elements(self, locator):
        try:
            web_elements = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_all_elements_located(locator))
            return web_elements
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR")

# creating enter_text function to enter text in textboxes
    def enter_text(self, locator, text):
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR")

# creating click function to click the buttons
    def click(self, locator):
        try:
            element = self.find_element(locator)
            element.click()
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR")

# creating is_visible function to check the textbox is visible or not

    def is_visible(self, locator):
        try:
            web_element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
            return web_element.is_displayed()
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR")

# creating is_enabled function to check the button is enabled or not

    def is_enabled(self, locator):
        try:
            web_element = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))
            return web_element.is_enabled()
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR")

# creating fetch_url function to fetch the current url

    def fetch_url(self):
        try:
            return self.driver.current_url
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR")

# creating Url_change function to get the changed url details

    def Url_change(self, changed_url):
        try:
            web_element = WebDriverWait(self.driver, self.timeout).until(EC.url_to_be(changed_url))
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR")
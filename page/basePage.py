from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def open_base_url(self, base_url):
        self.driver.get(base_url)

    def wait_element_present(self, locator):
        return WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(locator))
    
    def wait_for_element_clickable(self, locator):
        return WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(locator))


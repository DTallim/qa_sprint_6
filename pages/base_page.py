from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, driver, time=5):
        self.driver = driver
        self.time = time

    def format_to_locator(self, locator_1, num):  # Убедимся что метод здесь есть
        method, locator = locator_1
        locator = locator.format(num)
        return method, locator

    def find_element(self, locator):
        WebDriverWait(self.driver, self.time).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_element(self,locator):
        WebDriverWait(self.driver, self.time).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def add_text_to_element(self,locator,text):
        self.find_element(locator).send_keys(text)

    def get_text_from_element(self,locator):
        return self.find_element(locator).text

    def scroll_to_element(self,locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def get_url(self):
        return self.driver.current_url

    def open_page(self,url):
        self.driver.get(url)

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
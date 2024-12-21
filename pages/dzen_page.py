from locators.dzen_page_locators import Dzen_Page_Locators
from pages.base_page import BasePage
import allure

class DzenPage(BasePage):
    @allure.step('Проверка открытия страницы "Яндекс Дзен"')
    def check_dzen_logo(self):
        return self.find_element(Dzen_Page_Locators.LOGO_DZEN)
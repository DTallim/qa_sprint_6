from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure

class MainPage(BasePage):
    @allure.step('Получение текстов ответов')
    def check_answer_text(self, num):
        question = self.format_to_locator(MainPageLocators.QUESTION, num)  # добавляем self.
        answer = self.format_to_locator(MainPageLocators.ANSWER, num)  # добавляем self.
        self.scroll_to_element(MainPageLocators.QUESTION_8)
        self.click_element(MainPageLocators.BUTTON_COOKIE)
        self.click_element(question)
        return self.get_text_from_element(answer)

    @allure.step('Клик на логотип "Яндекс" для открытия нового окна "Яндекс Дзен"')
    def click_logo_yandex(self):
        self.click_element(MainPageLocators.BUTTON_COOKIE)
        self.click_element(MainPageLocators.LOGO_YANDEX)

    @allure.step('Клик на логотип "Самокат" для перехода на домашнюю страницу')
    def click_logo_scooter(self):
        self.click_element(MainPageLocators.LOGO_SCOOTER)

    @allure.step('Переход к форме для заказа с помощью кнопки "Заказать" вверху страницы')
    def check_button_order_top(self):
        self.click_element(MainPageLocators.BUTTON_COOKIE)
        self.click_element(MainPageLocators.BUTTON_ORDER_TOP)

    @allure.step('Переход к форме для заказа с помощью книпки "Заказать" по центру страницы')
    def check_button_to_order_center(self):
        self.scroll_to_element(MainPageLocators.BUTTON_ORDER_CENTER)
        self.click_element(MainPageLocators.BUTTON_COOKIE)
        self.click_element(MainPageLocators.BUTTON_ORDER_CENTER)

    @allure.step('Проверка открытия домашней страницы "Самокат"')
    def check_main_page_open(self):
        return self.find_element(MainPageLocators.TITLE_ABOUT_SCOOTER)

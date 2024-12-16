import allure
from conftest import driver
import pytest
from data import Url,Answer
from pages.main_page import MainPage
from pages.dzen_page import DzenPage
from pages.order_page import OrderPage

@allure.feature('Проверка соответствия текстов ответов')
class TestMainPage:
    @allure.title('Проверка соответствия текста ответа вопросу в разделе "Вопросы о важном"')
    @pytest.mark.parametrize(
        'num,answer',
        [
            (0, Answer.answer_0),
            (1, Answer.answer_1),
            (2, Answer.answer_2),
            (3, Answer.answer_3),
            (4, Answer.answer_4),
            (5, Answer.answer_5),
            (6, Answer.answer_6),
            (7, Answer.answer_7)
        ]
    )
    def test_check_questions_and_answer(self, driver, num, answer):
        driver.get(Url.main_page)
        main_page = MainPage(driver)
        assert main_page.check_answer_text(num) == answer

@allure.feature('Тестирование перехода по клику на логотипы Яндекс и Самокат')
class TestLogo:
    @allure.title('Проверка перехода на "Джен" по клику на логотип "Яндекс"')
    def test_check_logo_yandex_open_dzen(self,driver):
        driver.get(Url.main_page)
        main_page = MainPage(driver)
        dzen = DzenPage(driver)
        main_page.click_logo_yandex()
        main_page.switch_to_new_window()
        assert dzen.check_dzen_logo().is_displayed()

    @allure.title('Проверка перехода на страницу "Яндекс Самокат по клику на логотип "Самокат""')
    def test_check_logo_scooter_open_home_page(self,driver):
        driver.get(Url.order_page)
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.check_button_order_top()
        assert order_page.check_order_page_open().is_displayed()
        main_page.click_logo_scooter()
        assert main_page.check_main_page_open().is_displayed()

@allure.feature('Тестирование перехода по клику на кнопки оформления заказа')
class TestOrderButton:
    @allure.title('Переход к форме заказа с помощью кнопки "Заказать" вверху страницы')
    def test_check_button_to_order_top(self,driver):
        driver.get(Url.main_page)
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.check_main_page_open().is_displayed()
        main_page.check_button_order_top()
        assert order_page.check_order_page_open().is_displayed()

    @allure.title('Переход к форме для заказа с помощью кнопки "Заказать" по центру страницы')
    def test_check_button_to_order_center(self,driver):
        driver.get(Url.main_page)
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.check_main_page_open().is_displayed()
        main_page.check_button_to_order_center()
        assert order_page.check_order_page_open().is_displayed()




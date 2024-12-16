import allure
import pytest

from conftest import driver
from data import Url, OrderData
from pages.order_page import OrderPage
from pages.main_page import MainPage
from locators.order_page_locators import OrderPageLocators

@allure.suite('Оформление заказа')
class TestOrderPage:
    @allure.title('Оформление заказа с разными тестовыми данными')
    @pytest.mark.parametrize("name,last_name,address,metro,phone,date,rental_day,color,comment_for_courier",
                             [
                             (OrderData.name_1, OrderData.last_name_1, OrderData.address_1, OrderPageLocators.METRO_LUBANKA, OrderData.phone_1, OrderData.date_1, OrderPageLocators.RENT_1_DAY, OrderPageLocators.CHECKBOX_BLACK_COLOR, OrderData.comment_empty),
                             (OrderData.name_2, OrderData.last_name_2, OrderData.address_2, OrderPageLocators.METRO_SPORTINAY, OrderData.phone_2, OrderData.date_2, OrderPageLocators.RENT_2_DAY, OrderPageLocators.CHECKBOX_GREY_COLOR, OrderData.comment_for_courier_1)
                             ],
                             ids=['Оформление заказа с данными первого пользователя', 'Оформление заказа с данными второго пользователя'])
    def test_order_with_different_user_data(self, driver, name, last_name, address, metro, phone, date, rental_day, color, comment_for_courier):
        driver.get(Url.main_page)
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.check_button_order_top()
        order_page.add_user_data_to_form_order(name, last_name, address, metro, phone, date, rental_day, color, comment_for_courier)
        success_screen_text = order_page.check_window_successful_order()
        assert 'Заказ оформлен' in success_screen_text
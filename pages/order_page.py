from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure

class OrderPage(BasePage):
    @allure.step('заполнение формы для заказ')
    def add_user_data_to_form_order(self, name, last_name, address, metro, phone, date, rental_day, color,
                                    comment_for_courier=''):
        try:
            self.add_text_to_element(OrderPageLocators.NAME, name)
            self.add_text_to_element(OrderPageLocators.LAST_NAME, last_name)
            self.add_text_to_element(OrderPageLocators.ADDRESS, address)

            self.click_element(OrderPageLocators.METRO)
            self.click_element(metro)

            self.add_text_to_element(OrderPageLocators.PHONE, phone)
            self.click_element(OrderPageLocators.NEXT)

            self.add_text_to_element(OrderPageLocators.DATA_ORDER, date)
            self.click_element(OrderPageLocators.TITLE_ABOUT_RENT)

            self.click_element(OrderPageLocators.RENTAL_PERIOD)
            self.click_element(rental_day)

            self.click_element(color)

            if comment_for_courier:
                self.add_text_to_element(OrderPageLocators.COMMENT_FOR_COURIER, comment_for_courier)

            self.click_element(OrderPageLocators.BUTTON_TO_ORDER_IN_FORM)
            return self.find_element(OrderPageLocators.BUTTON_YES_ORDER)

        except Exception as e:
            allure.attach(str(e), name='Error', attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step('получение поп ап об успешном оформлении заказа')
    def check_window_successful_order(self):
        self.click_element(OrderPageLocators.BUTTON_YES_ORDER)
        return self.get_text_from_element(OrderPageLocators.POP_UP_WINDOW_SUCCESSFUL_ORDER)

    @allure.step('Проверка открытия формы заказа')
    def check_order_page_open(self):
        return self.find_element(OrderPageLocators.TITLE_ABOUT_RENT)
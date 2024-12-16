from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME = By.XPATH, "//input[@placeholder='* Имя']" # Поле ввода имени
    LAST_NAME = By.XPATH, "//input[@placeholder='* Фамилия']" # Поле ввода фамилии
    ADDRESS = By.XPATH, "//input[@placeholder = 'Адрес: куда привезти заказ ']" # Поле ввода адреса
    METRO = By.XPATH, "//input[@placeholder='*Станция метро']" # Поле выбора станции
    METRO_LUBANKA = By.XPATH, ".//*[contains(text(),'Лубянка')]" # Станция Лубянка
    METRO_SPORTINAY = By.XPATH, ".//*[contains(text(), 'Спортивная')]" #Станция Спортивная
    PHONE = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    NEXT = By.XPATH, "//button[@class='Button_Button__ra12g Button_middle_1CSJM']" #Кнопка далее
    TITLE_ABOUT_RENT = By.XPATH, "//*[@class='Order_Header__BZXOb']" #Заголовок формы заказа
    DATA_ORDER = By.XPATH, "//input[@placeholder='* Когда привезти заказ']" #Поле ввода даты доставки заказа
    RENTAL_PERIOD = By.XPATH, "//*[@class='Dropdown-placeholder']" #Поле выбора продолжительности аренды
    RENT_1_DAY = By.XPATH, "//*[contains(text(), 'сутки')]" # Сутки аренды
    RENT_2_DAY = By.XPATH, "//*[contains(text(),'двое суток')]" #Двое суток аренды
    CHECKBOX_BLACK_COLOR = By.XPATH, "//*[contains(@id, 'black')]" # выбор черного цвета
    CHECKBOX_GREY_COLOR = By.XPATH, "//*[contains(@id, 'grey')]" # выбор серого цвета
    COMMENT_FOR_COURIER = By.XPATH, "//input[@placeholder='комментарий для курьера']"
    BUTTON_TO_ORDER_IN_FORM = By.XPATH, "//button[contains(@class, 'Button_Button__ra12g Button_Button_middle__1CSJM')]"
    BUTTON_YES_ORDER = By.XPATH, "//*[contains(text(),'Да')]"
    POP_UP_WINDOW_SUCCESSFUL_ORDER = By.XPATH, "//*[contains(text(),'Заказ оформлен')]"
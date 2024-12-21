from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGO_YANDEX = By.XPATH, "//*[@class='Header_LogoYandex__3TSOI']" #Логотип Яндекс
    LOGO_SCOOTER = By.XPATH, "//*[@class='Header_LogoScooter--3lsAR']" #Логотип Самокат
    TITLE_ABOUT_SCOOTER = By.XPATH, "//*[@class='Home_Header__iJKdX']" #Заголовок главной страницы
    QUESTION = By.XPATH, "//*[@id='accordion__heading-{}']" #Локатор вопроса
    ANSWER = By.XPATH, "//*[@id='accordion__panel-{}']" #Локатор ответа
    QUESTION_8 = By.XPATH, "//*[@id='accordion__heading-7']" #Вопрос 8
    BUTTON_ORDER_TOP = By.XPATH, "//button[@class='Button_Button__ra12g']" #Книпка заказать вверх страницы
    BUTTON_ORDER_CENTER = By.XPATH, "//button[contains(@class, 'Button_Button__ra12g Button')]"
    BUTTON_COOKIE = By.XPATH, "//*[@id='rcc-confirm-button']" #Кнопка "Да все привыкли", cookie
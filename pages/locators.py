from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON_ADD_PRODUCT = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE_BASKET = (By.CSS_SELECTOR,".alert-info .alertinner > p > strong ")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "h1 + .price_color")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main > h1")
    NAME_NOTIFICATION_PRODUCT = (By.CSS_SELECTOR, "#messages > div > div > strong") 
    

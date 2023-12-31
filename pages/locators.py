from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[name=registration-email]")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name=registration-password1]")
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name=registration-password2]")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")
                       
class ProductPageLocators():
    BUTTON_ADD_PRODUCT = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE_BASKET = (By.CSS_SELECTOR,".alert-info .alertinner > p > strong ")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "h1 + .price_color")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main > h1")
    NAME_NOTIFICATION_PRODUCT = (By.CSS_SELECTOR, "#messages > div > div > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div > div > strong")

class BasketPageLocators():
    BASKET_BUTTON_SITE_HEADER = (By.CSS_SELECTOR, ".hidden-xs > strong + span > .btn-default")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > .basket-title > .row")

from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.click_add_button()           #Здесь мы вызываем методы
        self.price_product_correct()
        self.name_product_correct()
        

    def click_add_button(self):
        Click_add_button1 = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_PRODUCT)
        Click_add_button1.click()

    def price_product_correct(self):
        # находим элемент, содержащий текст
        price_product_el = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        # записываем в переменную price_product текст из элемента price_product_el
        price_product = price_product_el.text
        price_basket_el = self.browser.find_element(*ProductPageLocators.PRICE_BASKET)
        price_basket = price_basket_el.text
        try:
            assert  price_basket == price_product 
        except AssertionError:
            time.sleep(10)
            print("Цена в корзине не совпадает с ценой товара")

    def name_product_correct(self):
        name_product_el = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        name_product = name_product_el.text
        name_notification_el = self.browser.find_element(*ProductPageLocators.NAME_NOTIFICATION_PRODUCT)
        name_notification = name_notification_el.text
        try:
            assert  name_product == name_notification
        except AssertionError:
            time.sleep(10)
            print("Название товара в сообщении не совпадает с названием товара")

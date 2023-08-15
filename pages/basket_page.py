from .base_page import BasePage
from .locators import BasketPageLocators
import time


class BasketPage(BasePage):
    def cant_see_product_in_basket_opened_from_main_page(self):
        self.basket_should_be_empty()
        self.text_that_the_basket_empty()

    def basket_should_be_empty(self):
        pass
        


    def text_that_the_basket_empty(self):
        text_empty = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT)
        text_empty1 = text_empty.text
        try:
            assert  "Your basket is empty. Continue shopping" ==  text_empty1
        except AssertionError:
            print("Фактический текст:", text_empty1)
            time.sleep(10)
            print("Нет текста, что корзина не пуста")
            assert False
        else:
            print("Текст, что корзина пуста, найден успешно")

    def basket_should_be_empty(self):
        try:
            assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), \
               "В корзине не должно быть товаров"
        except AssertionError:
            print("В корзине не должно быть товаров")
        else:
            print("В корзине нет товаров")
            
        
        

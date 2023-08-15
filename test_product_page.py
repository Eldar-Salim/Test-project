import pytest
from selenium import webdriver
from pages.product_page import ProductPage
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import time

'''@pytest.mark.parametrize('link', ["0","1", "2", "3", "4", "5", "6",
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  "8", "9"])'''

#тест на добавление товара в корзину
'''def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()
    page.click_add_button()
    page.solve_quiz_and_get_code()
    page.price_product_correct()
    page.name_product_correct()'''
'''#тест на отсутствие сообщения об успешном добавлении товара при добавлении товара
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()
    page.click_add_button()
    page.should_not_be_success_message_after_adding_product_to_basket()

#тест на отсутствие сообщения об успешном добавлении товара при не добавленном товаре
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()
    page.should_not_be_success_message_before_adding_product_in_basket()
    
#тест на исчезновение сообщения об успешном добавлении товара при добавлении товара
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()
    page.click_add_button()
    page.should_disappear_success_message_after_adding_product_to_basket()'''

"""def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link) 
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = LoginPage(browser, link) 
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()"""

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link) 
    page.open()
    page.go_to_basket_page_from_site_header()
    page.basket_should_be_empty()
    page.text_that_the_basket_empty()
    
    
    
    




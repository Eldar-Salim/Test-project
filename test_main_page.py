import pytest
from selenium import webdriver
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.basket_page import BasketPage


@pytest.mark.login_guest
class TestLoginFromMainPage():
    # Тест, что при переходе на страницу логина попадаем именно на нее
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()    
        page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
        page.should_be_login_link()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    # Тест, что на главной странице есть ссылка на логин
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


# Тест на отсутствие товаров в корзине при открытии главной страницы гостем
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page_from_site_header()
    page.basket_should_be_empty()  # Проверяем, что корзина пуста
    page.text_that_the_basket_empty()  # Проверяем, что есть надпись о том, что корзина пуста

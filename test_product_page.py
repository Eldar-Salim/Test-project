import pytest
from selenium import webdriver
from pages.product_page import ProductPage
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


@pytest.mark.need_review
# Тест, что гость может перейти на страницу логина
def test_guest_can_go_to_login_page_from_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


# Тест на отсутствие товаров в корзине при открытии страницы товаров
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = BasketPage(browser, link)
        page.open()
        page.go_to_basket_page_from_site_header()
        page.basket_should_be_empty() # Проверяем, что корзина пуста
        page.text_that_the_basket_empty() # Проверяем, что есть надпись о том, что корзина пуста


# Тест на добавление товара в корзину гостем
@pytest.mark.need_review
def test_quest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.click_add_button()
    #page.solve_quiz_and_get_code() # т.к алерт не появляется, закомментил его
    page.price_product_correct() # Стоимость корзины совпадает с ценой товара
    page.name_product_correct() # Название товара в сообщении должно совпадать с тем товаром, который действительно добавлен


@pytest.mark.need_review
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    #Регистрация нового пользователя
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.register_new_user_email_password() # Регистрируем нового пользователя
        page.should_be_authorized_user() # Проверяем, что пользователь зарегистрировался


    # Тест на добавление товара в корзину авторизованным юзером
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.click_add_button()
        #page.solve_quiz_and_get_code() # т.к алерт не появляется, закомментил его
        page.price_product_correct() # Стоимость корзины совпадает с ценой товара
        page.name_product_correct() # Название товара в сообщении должно совпадать с тем товаром, который действительно добавлен


# Тест на отсутствие сообщения об успешном добавлении товара при добавлении товара
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_button()
    page.should_not_be_success_message_after_adding_product_to_basket() # Проверяем, что нет сообщения об успехе


# Тест на исчезновение сообщения об успешном добавлении товара при добавлении товара
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_button()
    page.should_disappear_success_message_after_adding_product_to_basket()


# Тест, что гость может ссылку на логин
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


# Тест на отсутствие сообщения об успешном добавлении товара при не добавленном товаре
def test_quest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message_before_adding_product_in_basket()

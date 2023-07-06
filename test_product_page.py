import pytest
from selenium import webdriver
from pages.product_page import ProductPage
import time

@pytest.mark.parametrize('link', ["0","1", "2", "3", "4", "5", "6",
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  "8", "9"])


def test_guest_can_add_product_to_basket(browser, link):
    link = link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()
    page.click_add_button()
    page.solve_quiz_and_get_code()
    page.price_product_correct()
    page.name_product_correct()
    




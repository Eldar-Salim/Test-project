import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    # Добавление опции командной строки для выбора языка.
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, en, etc")    


@pytest.fixture
# Фикстура для инициализации браузера с заданным языком.
def browser(request):
    language = request.config.getoption("language")
    if language is not None:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        print("\nstart chrome browser for test..")
    else:
        raise pytest.UsageError("--language should be specified")
    yield browser
    print("\nquit browser..")
    browser.quit()

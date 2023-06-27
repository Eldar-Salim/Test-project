from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()           #Здесь мы вызываем метод
        self.should_be_login_form()        #Здесь мы вызываем метод
        self.should_be_register_form()     #Здесь мы вызываем метод
  
        
    def should_be_login_url(self):
        
        current_url = self.browser.current_url
        assert "login" in current_url, "url does not contain the word Login" # реализуйте проверку на корректный url адрес
        

    def should_be_login_form(self):
        Login_form = self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"# реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        Register_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"# реализуйте проверку, что есть форма регистрации на странице
        assert True

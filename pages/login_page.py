from .base_page import BasePage
from .locators import LoginPageLocators
from mimesis import Generic
import random
import string
import time




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

    
    def  register_new_user_email_password(self):
        
        generic = Generic()
        email = generic.person.email()
        Email_address_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        Email_address_field.send_keys(email)

        # Генерим пароль
        password = generic.person.password(length=12)
        password1 = password
        
        Password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        Password_field.send_keys(password)
        Confirm_password_field = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD)
        Confirm_password_field.send_keys(password1) #password1 т.к пароль нужно повторить 
        
        Register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        Register_button.click()
        

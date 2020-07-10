from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "abfff" in self.driver.current_url, "No 'login' in the current url"


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "No login form on login page" #проверка на наличие формы логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_EMAIL_FIELD), "No email field on login form on login page"
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_PW_FIELD), "No password field on login form on login page "
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_FORGOT_PW_LINK), "No forgot password link on login form on login page"
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_SUBMIT_BTN), "No submit btn on login form on login page"




    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "No register form on login page" #проверка на наличие формы регистрации
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_EMAIL_FIELD), "No email field on register form"
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_PW_FIELD), "No password field on register form"
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_CONFIRM_PW_FIELD), "No confirmation pw field on register form"
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_REGISTER_BTN), "No register button on register field"


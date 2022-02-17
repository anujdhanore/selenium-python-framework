import utilities.custom_logger as cl
from pages.home.navigation_page import NavigationPage
from base.basepage import BasePage
import logging

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # locators
    _login_link = "//a[@href='/login']"
    _email_field = "//form[@role='form']//input[@id='email']"
    _pwd_field = "password"
    _login_btn = "//input[@value='Login']"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType="xpath")

    def enterPassword(self, password):
        self.sendKeys(password, self._pwd_field)

    def clickLoginBtn(self):
        self.elementClick(self._login_btn, locatorType="xpath")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginBtn()

    def verifyLoginSuccess(self):
        result = self.isElementPresent("dropdownMenu1", locatorType="id")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//span[contains(text(),'Your username or password is invalid.')]",
                                       locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("My Courses")

    def logout(self):
        self.nav.navToUserIcon()
        self.elementClick(locator="//button[@id='dropdownMenu1']//following-sibling::ul/li[3]/a", locatorType="xpath")

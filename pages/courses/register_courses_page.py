import utilities.custom_logger as cl
from base.basepage import BasePage
import logging

class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _search_box = ""
    _all_courses_link = "//div[@id='navbar-inverse-collapse']/ul/li[2]/a"
    _course = "//div[contains(@class,'zen-course-list')]//h4[contains(text(),'{0}')]"
    _enroll_button = "//button[text()='Enroll in Course']"
    _scroll_to_payment = "//h3[text()='Payment Information ']"
    _card_frame = "//div[@id='card-number']//iframe"
    _cc_num = "cardnumber"
    _expiry_frame = "//div[@id='card-expiry']//iframe"
    _cc_exp = "exp-date"
    _cvv_frame = "//div[@id='card-cvc']//iframe"
    _cc_cvv = "cvc"
    _submit_enroll = "//div[@class='stripe-outer ']/div[2]/div/button[1]"
    _enroll_error_message = "//span[contains(text(),'Your card was declined.')]"

    def selectCourseToEnroll(self, courseName):
        self.elementClick(self._course.format(courseName), locatorType="xpath")

    def clickToEnrollButton(self):
        self.scrollToElement(self._enroll_button, locatorType="xpath")
        self.elementClick(self._enroll_button, locatorType="xpath")

    def scrollToPayment(self):
        self.scrollToElement(self._scroll_to_payment, locatorType="xpath")

    def	enterCardNum(self, num):
        self.switchToiFrame(self._card_frame, locatorType="xpath")
        self.sendKeys(num, self._cc_num, locatorType="name")
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        self.switchToiFrame(self._expiry_frame, locatorType="xpath")
        self.sendKeys(exp, self._cc_exp, locatorType="name")
        self.switchToDefaultContent()

    def enterCardCVV(self, cvv):
        self.switchToiFrame(self._cvv_frame, locatorType="xpath")
        self.sendKeys(cvv, self._cc_cvv, locatorType="name")
        self.switchToDefaultContent()

    def clickEnrollSubmitButton(self):
        self.elementClick(self._submit_enroll, locatorType="xpath")

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)

    def	enrollCourse(self,	num="",	exp="",	cvv=""):
        self.clickToEnrollButton()
        self.scrollToPayment()
        self.enterCreditCardInformation(num, exp, cvv)
        self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        messageElement = self.waitForElement(locator=self._enroll_error_message, locatorType="xpath")
        result = self.isElementDisplayed(element=messageElement)
        return result

    def verifyTitle(self):
        return self.verifyPageTitle("Google")

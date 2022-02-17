import utilities.custom_logger as cl
from base.basepage import BasePage
import logging

class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _home = "HOME"
    _all_courses = "ALL COURSES"
    _my_courses = "MY COURSES"
    _support = "SUPPORT"
    _my_community = "MY COMMUNITY"
    _notification = "//a[@class='jqNotification']/i"
    _user_settings_icon = "dropdownMenu1"

    def navToHome(self):
        self.elementClick(self._home, locatorType="link")

    def navToAllCourses(self):
        self.elementClick(self._all_courses, locatorType="link")

    def navToMyCourses(self):
        self.elementClick(self._my_courses, locatorType="link")

    def navToSupport(self):
        self.elementClick(self._support, locatorType="link")

    def navToMyCommunity(self):
        self.elementClick(self._my_community, locatorType="link")

    def navToNotification(self):
        self.elementClick(self._notification, locatorType="xpath")

    def navToUserIcon(self):
        self.elementClick(self._user_settings_icon)


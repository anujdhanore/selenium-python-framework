from selenium.webdriver.common.by import By

from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesMultipleDataSet(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.rcp = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "378282246310005", "12 / 34", "1234"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV):
        self.rcp.clickAllCoursesLink()
        self.rcp.selectCourseToEnroll(courseName)
        self.rcp.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCVV)
        result = self.rcp.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment Failure Verification")

        self.driver.find_element(By.XPATH, "//div[@id='navbar-inverse-collapse']/ul/li[2]/a").click()



from pages.home.navigation_page import NavigationPage
from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.rcp = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navToAllCourses()

    @pytest.mark.run(order=1)
    @data(*getCSVData("C:\\Users\\Anuj.Dhanore\\PycharmProjects\\letskodeit\\testdata.csv"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV):
        self.rcp.selectCourseToEnroll(courseName)
        self.rcp.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCVV)
        result = self.rcp.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment Failure Verification")



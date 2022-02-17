from selenium import webdriver
from selenium.webdriver.common.by import By

class SearchCourse():

    def test(self):

        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://courses.letskodeit.com/")

        driver.find_element(By.XPATH, "//a[@href='/login']").click()
        driver.find_element(By.XPATH, "//form[@role='form']//input[@id='email']").send_keys("test@email.com")
        driver.find_element(By.ID, "password").send_keys("abcabc")
        driver.find_element(By.XPATH, "//input[@value='Login']").click()

        driver.find_element(By.XPATH, "//div[@id='navbar-inverse-collapse']/ul/li[2]/a").click()
        driver.find_element(By.XPATH, "//div[@id='course-list']/div[1]/div[@class='zen-course-list']").click()

        driver.find_element(By.XPATH, "//button[text()='Enroll in Course']").click()

        frames = driver.find_elements(By.TAG_NAME, "iframe")

        print("no of frames on the webpage: ", len(frames))

        payment = driver.find_element(By.XPATH, "//h3[text()='Payment Information ']")
        payment.location_once_scrolled_into_view

        iframe1 = driver.find_element(By.XPATH, "//div[@id='card-number']//iframe")
        driver.switch_to.frame(iframe1)
        driver.find_element(By.NAME, "cardnumber").send_keys("378282246310005")
        driver.switch_to.default_content()

        iframe2 = driver.find_element(By.XPATH, "//div[@id='card-expiry']//iframe")
        driver.switch_to.frame(iframe2)
        driver.find_element(By.NAME, "exp-date").send_keys("12 / 34")
        driver.switch_to.default_content()

        iframe3 = driver.find_element(By.XPATH, "//div[@id='card-cvc']//iframe")
        driver.switch_to.frame(iframe3)
        driver.find_element(By.NAME, "cvc").send_keys("1234")
        driver.switch_to.default_content()

        driver.find_element(By.XPATH, "//div[@class='stripe-outer ']/div[2]/div/button[1]").click()

        declined = driver.find_element(By.XPATH, "//span[contains(text(),'Your card was declined.')]")
        print("Declined message:", str(declined.text))

        driver.quit()


ff = SearchCourse()
ff.test()

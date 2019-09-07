from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Applications:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def deactivate(self):
        driver=self.driver
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, ".//a[contains(.,'SETTINGS')]")))
        if len(driver.find_elements_by_xpath(".//a[contains(text(),'SETTINGS')]")) > 0:
            driver.find_element_by_xpath(".//span[@class='links']//a[1]").click()
        assert driver.find_element_by_xpath("//button [@class='negative']").is_displayed()
        driver.find_element_by_xpath("//button [@class='negative']").click()
        driver.find_element_by_xpath("//div[contains(@class,'buttonRow')]//*[contains(text(),'NOW')]").click()
        wait.until(EC.presence_of_element_located((By.XPATH, ".//*[@id='header']//a[@class='signup']")))

    def open_home_page(self):
        driver=self.driver
        driver.get("https://www.slice.com/")

    def login(self, passw, user):
        driver = self.driver

        self.open_home_page()
        driver.find_element_by_xpath(".//a[contains(.,'LOGIN')]").click()
        driver.find_element_by_xpath(".//input[@type='text']").clear()
        driver.find_element_by_xpath(".//input[@type='text']").send_keys(user)
        driver.find_element_by_xpath(".//input[@type='password']").clear()
        driver.find_element_by_xpath(".//input[@type='password']").send_keys(passw)
        driver.find_element_by_xpath(".//button[contains(text(), 'LOG IN')]").click()

    def log_out(self):
        driver=self.driver
        driver.find_element_by_link_text("LOG OUT").click()

    def destroy(self):
        self.driver.quit()

    def sign_up(self, passw, passw_aol, user):
        driver=self.driver
        driver.find_element_by_link_text("SIGN UP").click()
        driver.find_element_by_xpath(".//input[@type='email']").clear()
        driver.find_element_by_xpath(".//input[@type='email']").send_keys(user)
        driver.find_element_by_id("agreeInput").click()
        driver.find_element_by_xpath(" //*[@type='button']").click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, ".//input[@type='password']")))
        driver.find_element_by_xpath(".//input[@type='password']").clear()
        driver.find_element_by_xpath(".//input[@type='password']").send_keys(passw_aol)
        driver.find_element_by_xpath("//*[@type='button']").click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='key']")))
        if driver.find_element_by_xpath("//div[@class='key']").is_displayed():
            driver.find_element_by_xpath(".//input[@type='password']").send_keys(passw)
            driver.find_element_by_xpath("//*[@type='button']").click()
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "LOG OUT")))
        return wait
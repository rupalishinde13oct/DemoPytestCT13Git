from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as ec, WebDriverWait


class OrangeHrm:

    def test_Login_001(self):
        d = webdriver.Chrome()
        d.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        d.maximize_window()

        # will apply explicite wait on username webelement
        wait = WebDriverWait(d, 10)
        wait.until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
        d.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        d.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        d.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

        # will apply explicite wait on username webelement
        wait.until(ec.presence_of_element_located((By.XPATH, "//p[@class='oxd-userdropdown-name']")))
        d.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
        d.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
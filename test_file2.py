import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as ec, WebDriverWait


class Test2:
    # @pytest.mark.skip
    def test_add_002(self):
        a = 10
        b = 2
        add = a + b
        if add == 12:
            assert True
        else:
            assert False

    @pytest.mark.GroupMultiply
    def test_mul_002(self):
        a = 10
        b = 2
        add = a * b
        if add == 20:
            assert True
        else:
            assert False

    def test_CredKart_Login(self):
        d = webdriver.Chrome()
        d.get("https://automation.credence.in/")
        d.find_element(By.LINK_TEXT, "Login").click()
        d.maximize_window()
        wait = WebDriverWait(d, 10)

        d.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("Rupalishinde13oct@gmail.com")
        d.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("rupali1323")
        d.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        d.implicitly_wait(20)

        msg = d.find_element(By.XPATH , "//h2[normalize-space()='CredKart']").text
        if msg == "CredKart":
            assert True
        else:
            assert False
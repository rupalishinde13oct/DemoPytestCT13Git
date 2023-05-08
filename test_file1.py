# To create report file enter this command in terminal
# pytest [folder name in which test cases presend] --html=[ReportFileName].html
# pytest Pytest/TestCases --html=reports1.html

import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test:
    # @pytest.mark.skip
    def test_add__001(self):
        a = 2
        b = 5
        sum = a + b
        if sum == 7:
           assert True
        else:
            assert False

    @pytest.mark.GroupMultiply
    def test_mul__001(self):
        a = 2
        b = 5
        sum = a * b
        if sum == 10:
            assert True
        else:
            assert False


    def test_Login__001(self):
        d = webdriver.Chrome()
        d.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        d.implicitly_wait(10)
        d.find_element(By.XPATH , "//input[@name='username']").send_keys("Admin")
        d.find_element(By.XPATH , "//input[@name='password']").send_keys("admin123")
        d.find_element(By.XPATH , "//button[@type='submit']").click()
        time.sleep(5)
        var = d.find_element(By.XPATH , "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']").text

        if var=='Dashboard':
            assert True
        else:
            False

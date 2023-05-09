import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait



class Test3:

    def test_div_003(self):
        a = 10
        b = 2
        add = a / b
        if add == 5:
            assert True
        else:
            assert False

    # @pytest.mark.skipif
    def test_square_003(self):
        a = 10
        add = a * a
        if add == 100:
            assert True
        else:
            assert False

    @pytest.mark.GroupMultiply
    def test_mul_003(self):
        a = 10
        b = 5
        add = a * b
        if add == 50:
            assert True
        else:
            assert False

    def test_Credence(self):
        d = webdriver.Chrome()
        d.get("https://credence.in/")
        time.sleep(2)
        d.find_element(By.XPATH , "//img[@src='/website/images/enquiry.png']").click()
        time.sleep(2)
        l = len(d.find_elements(By.XPATH , "//div[@class='quickfinder-description gem-text-output']//p//a"))
        print(l)
        list = []
        for i in range(1,l+1):
            no = d.find_element(By.XPATH , "//div[@class='quickfinder-description gem-text-output']//p//a["+str(i)+"]").text
            list.append(no)
        print(list)
        if "+91 9091929355" in list:
            assert True
            print("test_Credence is Passed")
        else:
            assert False
            print("test_Credence is Failed")

    def test_Login_001(self):
        d = webdriver.Chrome()
        d.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        d.maximize_window()
        time.sleep(2)
        # will apply explicite wait on username webelement
        # wait = WebDriverWait(d, 10)
        # wait.until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
        d.find_element(By.XPATH, "//input[@placeholder='username']").send_keys("Admin")
        d.find_element(By.XPATH, "//input[@placeholder='password']").send_keys("admin123")
        d.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)
        # wait.until(ec.presence_of_element_located((By.XPATH, "//span[normalize-space()='PIM']")))
        d.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
        time.sleep(2)
        d.find_element(By.XPATH, "//i[@class='oxd-icon bi-plus oxd-button-icon']").click()
        time.sleep(2)
        d.find_element(By.XPATH, "//input[@placeholder='First name']").send_keys("Rupali")
        d.find_element(By.XPATH, "//input[@placeholder='Middle name']").send_keys("P")
        d.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Pandit")
        d.find_element(By.XPATH, "//button[@type='submit']").click()
        # time.sleep(5)
        # print(d.find_element(By.XPATH , "//h6[@class='oxd-text oxd-text--h6 --strong']").text())


        # will apply explicite wait on username webelement
        # wait.until(ec.presence_of_element_located((By.XPATH, "//p[@class='oxd-userdropdown-name']")))
        d.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
        d.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()



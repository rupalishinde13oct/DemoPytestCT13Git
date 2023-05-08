import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test3:

    # def test_div_003(self):
    #     a = 10
    #     b = 2
    #     add = a / b
    #     if add == 5:
    #         assert True
    #     else:
    #         assert False
    #
    # # @pytest.mark.skipif
    # def test_square_003(self):
    #     a = 10
    #     add = a * a
    #     if add == 100:
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.GroupMultiply
    # def test_mul_003(self):
    #     a = 10
    #     b = 5
    #     add = a * b
    #     if add == 50:
    #         assert True
    #     else:
    #         assert False

    def test_Credence(self):
        d = webdriver.Chrome()
        d.get("https://credence.in/")

        d.find_element(By.XPATH , "//img[@src='/website/images/enquiry.png']").click()
        l = len(d.find_elements(By.XPATH , "//div[@class='quickfinder-description gem-text-output']//p//a"))
        print(l)
        list = []
        for i in range(1,l+1):
            no = d.find_element(By.XPATH , "//div[@class='quickfinder-description gem-text-output']//p//a["+str(i)+"]").text
            list.append(no)
        print(list)
        # if "+91 9091929355" in list:
        #     assert True
        # else:
        #     assert False

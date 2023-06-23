import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilites.readProperties import ReadConfig
from utilites.customLogger import LogGen
import string
import random


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("********************** Test_003_AddCustomer ***********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******************* Login Successful *****************")

        self.logger.info("******************* Starting Add Customer Test ******************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.addcust.clickOnAddnew()

        self.logger.info("**************** Providing Customer info ***************")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Nanda")
        self.addcust.setLastName("gopal")
        self.addcust.setDob("02/27/2000")
        self.addcust.setCompanyName("Msys")
        self.addcust.setAdminContent("This is for Testing.............")
        self.addcust.clickOnSave()

        self.logger.info("****************** Saving Customer Info ****************")

        self.logger.info("***************** Add customer validation started **************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("************ Add Customer Test Passed ******************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_src.png")
            self.logger.error("**************** Add Customer Test Failed ****************")
            assert False

        self.driver.close()
        self.logger.info("*************************** Ending Test_003_AddCustomer Test *************************")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

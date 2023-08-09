import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.deleteCustomer import DeleteCustomer
from pageObjects.editCustomer import EditCustomer
from pageObjects.exportCustomer import exportCustomer
from pageObjects.searchCustomerPage import SearchCustomer
from utilites.readProperties import ReadConfig
from utilites.customLogger import LogGen

class Test_DeleteCustomer_011:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.Delete
    def test_deleteCustomer(self, setup):
        self.logger.info("************* Deleting Customer Details *************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******************** Login Successful ******************")

        self.logger.info("****************** Delete Customer Details Start **********************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.deletecust = DeleteCustomer(self.driver)
        time.sleep(3)
        self.deletecust.clickOnSearchAngleUpIcon()
        time.sleep(3)
        self.deletecust.clickOnCustomerEditBtn()
        time.sleep(3)
        self.deletecust.clickOnCustomerDeleteBtn()
        time.sleep(3)
        self.deletecust.clickOnCustomerDeleteExtraBtn()

        self.logger.info("********************* Delete Customer Test Started ************************")
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        if "The customer has been deleted successfully." in self.msg:
            assert True
            self.logger.info("************ Delete Customer Test Passed ******************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_deleteCustomer_src.png")
            self.logger.error("**************** Delete Customer Test Failed ****************")
            assert False

        self.driver.close()
        self.logger.info("*************************** Ending Test_012_DeleteCustomer Test *************************")


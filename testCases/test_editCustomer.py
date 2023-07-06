import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.editCustomer import EditCustomer
from pageObjects.exportCustomer import exportCustomer
from pageObjects.searchCustomerPage import SearchCustomer
from utilites.readProperties import ReadConfig
from utilites.customLogger import LogGen

class Test_EditCustomer_011:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.Edit
    def test_editCustomer(self, setup):
        self.logger.info("************* Editing Customer Details *************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******************** Login Successful ******************")

        self.logger.info("****************** Edit Customer Details Start **********************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.editcust = EditCustomer(self.driver)
        time.sleep(3)
        self.editcust.clickOnSearchAngleUpIcon()
        time.sleep(3)
        self.editcust.clickOnCustomerEditBtn()
        time.sleep(3)
        self.editcust.renameFirstName("Nandagopal")
        self.editcust.renameLastName("D")
        self.editcust.renameCompanyName("Msys Technologies")
        self.editcust.clickOnSaveBtn()

        self.logger.info("********************* Edit Customer Test Started ************************")
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        if "The customer has been updated successfully." in self.msg:
            assert True
            self.logger.info("************ Edit Customer Test Passed ******************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_editCustomer_src.png")
            self.logger.error("**************** Edit Customer Test Failed ****************")
            assert False

        self.driver.close()
        self.logger.info("*************************** Ending Test_011_EditCustomer Test *************************")


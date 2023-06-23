import time

import pytest

from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.searchCustomerPage import SearchCustomer
from utilites.readProperties import ReadConfig
from utilites.customLogger import LogGen


class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("****************** Search Customer By Name **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************************* Login Successful ****************")

        self.logger.info("******** Starting Search Customer By Name ************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("************** Searching Customer By Name ****************")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByName("Victoria Terces")
        self.driver.close()
        assert True == status
        self.logger.info("***************  TC_SearchCustomerByName_005 Finished  *********** ")


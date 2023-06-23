import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilites.readProperties import ReadConfig
from utilites.customLogger import LogGen

class Test_001_Login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.driver = setup
        self.logger.info("************************* Home page Title Test ***************************")
        self.driver.get(self.baseUrl)
        actual_title = self.driver.title
        # self.driver.close()
        if actual_title == "Your store. Login":
            assert True
            self.logger.info("************************* Home page Title is Passed ***************************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.logger.error("************************* Home page Title is Failed ***************************")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.driver = setup
        self.logger.info("************************* Verifying Login Test ***************************")
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        # self.lp.driver.close()
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************************* Login Test is Passed ***************************")
            self.lp.driver.close()
        else:
            self.lp.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.logger.error("************************* Login Test is Failed ***************************")
            self.lp.driver.close()
            assert False

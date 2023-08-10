import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.add_customerRolePage import Add_customerRole
from pageObjects.LoginPage import LoginPage
from utilites.readProperties import ReadConfig
from utilites.customLogger import LogGen
import string
import random


class Test_AddCustomerRole_012:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.sanity
    def test_AddCustomerRole_1(self, setup):
        self.logger.info("*************************** Adding CustomerRole Test ************************* ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****************************** Login Successful *******************************")

        self.logger.info("****************************** Adding Customer Role Started ********************************")
        self.addcustrole = Add_customerRole(self.driver)
        self.addcustrole.clickOnCustomersMenu()
        self.addcustrole.clickOnCustomerRoleMenuItem()

        self.addcustrole.clickOnAddNew_Create()
        self.addcustrole.setName("Nandagopal")
        self.addcustrole.clickOnCheckbox_FreeShipping()
        self.addcustrole.clickOnCheckbox_TaxExempt()
        self.addcustrole.setSystemName("HP")
        self.addcustrole.clickOnSaveBtn()

        self.logger.info("****************** Saving Customer Role Info ****************")

        self.logger.info("****************** Add Customer Role Validation Started *********************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        print(self.msg)
        if 'The new customer role has been added successfully.' in self.msg:
            assert True
            self.logger.info("*************************** Add Customer Role Test Passed ****************************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\CustomerRole\\" + "test_addCustomerRole_src1.png")
            self.logger.info("*************************** Add Customer Role Test Failed ***********************")
            assert False

        self.driver.close()
        self.logger.info("***************************** Ending test_AddCustomerRole_1 **************************")

    @pytest.mark.sanity
    def test_AddCustomerRole_2(self, setup):
        self.logger.info("*************************** Checking Name Present CustomerRole Test 1 ************************* ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****************************** Login Successful *******************************")

        self.logger.info("******************************  Checking Name Present CustomerRole Test 1 Started ********************************")
        self.addcustrole = Add_customerRole(self.driver)
        self.addcustrole.clickOnCustomersMenu()
        self.addcustrole.clickOnCustomerRoleMenuItem()

        NewRole = self.addcustrole.selectTable1stColumn()
        if "Nandagopal" in NewRole:
            assert True
            time.sleep(3)
            print(NewRole)
        else:
            self.driver.save_screenshot(".\\Screenshots\\CustomerRole\\" + "test_addCustomerRole_src2.png")
            assert False

        self.driver.close()
        self.logger.info("***************************** Ending test_AddCustomerRole_2 **************************")

    @pytest.mark.sanity
    def test_AddCustomerRole_3(self, setup):
        self.logger.info("*************************** Checking Name Present CustomerRole Test 2 ************************* ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****************************** Login Successful *******************************")

        self.logger.info("****************************** Checking Name Present CustomerRole Test 2 Started ********************************")
        self.addcustrole = Add_customerRole(self.driver)
        self.addcustrole.clickOnCustomersMenu()
        self.addcustrole.clickOnCustomerRoleMenuItem()

        NewRole = self.addcustrole.selectTable1stColumn()
        if "Administrators" in NewRole:
            assert True
            time.sleep(3)
            print(NewRole)
        else:
            self.driver.save_screenshot("\\Screenshots\\" + "test_addCustomerRole_src2.png")
            assert False

        self.driver.close()
        self.logger.info("***************************** Ending test_AddCustomerRole_3 **************************")

    @pytest.mark.sanity
    def test_AddCustomerRole_4(self, setup):
        self.logger.info("*************************** Checking Name Present CustomerRole Test 3 ************************* ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****************************** Login Successful *******************************")

        self.logger.info("****************************** Checking Name Present CustomerRole Test 3 Started ********************************")
        self.addcustrole = Add_customerRole(self.driver)
        self.addcustrole.clickOnCustomersMenu()
        self.addcustrole.clickOnCustomerRoleMenuItem()

        NewRole = self.addcustrole.selectTable1stColumn()
        if "Forum Moderators" in NewRole:
            assert True
            time.sleep(3)
            print(NewRole)
        else:
            self.driver.save_screenshot(".\\Screenshots\\CustomerRole\\" + "test_addCustomerRole_src2.png")
            assert False

        self.driver.close()
        self.logger.info("***************************** Ending test_AddCustomerRole_4 **************************")

    @pytest.mark.sanity
    def test_AddCustomerRole_5(self, setup):
        self.logger.info("*************************** Checking Name Present CustomerRole Test 4 ************************* ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****************************** Login Successful *******************************")

        self.logger.info("****************************** Checking Name Present CustomerRole Test 4 Started ********************************")
        self.addcustrole = Add_customerRole(self.driver)
        self.addcustrole.clickOnCustomersMenu()
        self.addcustrole.clickOnCustomerRoleMenuItem()

        NewRole = self.addcustrole.selectTable1stColumn()
        if "Guests" in NewRole:
            assert True
            time.sleep(3)
            print(NewRole)
        else:
            self.driver.save_screenshot(".\\Screenshots\\CustomerRole\\" + "test_addCustomerRole_src2.png")
            assert False

        self.driver.close()
        self.logger.info("***************************** Ending test_AddCustomerRole_4 **************************")

    @pytest.mark.sanity
    def test_AddCustomerRole_6(self, setup):
        self.logger.info("*************************** Checking Name Present CustomerRole Test 5 ************************* ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****************************** Login Successful *******************************")

        self.logger.info("****************************** Checking Name Present CustomerRole Test 5 Started ********************************")
        self.addcustrole = Add_customerRole(self.driver)
        self.addcustrole.clickOnCustomersMenu()
        self.addcustrole.clickOnCustomerRoleMenuItem()

        NewRole = self.addcustrole.selectTable1stColumn()
        if "Registered" in NewRole:
            assert True
            time.sleep(3)
            print(NewRole)
        else:
            self.driver.save_screenshot(".\\Screenshots\\CustomerRole\\" + "test_addCustomerRole_src2.png")
            assert False

        self.driver.close()
        self.logger.info("***************************** Ending test_AddCustomerRole_4 **************************")

    @pytest.mark.sanity
    def test_AddCustomerRole_7(self, setup):
        self.logger.info("*************************** Checking Name Present CustomerRole Test 6 ************************* ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****************************** Login Successful *******************************")

        self.logger.info("****************************** Checking Name Present CustomerRole Test 6 Started ********************************")
        self.addcustrole = Add_customerRole(self.driver)
        self.addcustrole.clickOnCustomersMenu()
        self.addcustrole.clickOnCustomerRoleMenuItem()

        NewRole = self.addcustrole.selectTable1stColumn()
        if "Vendors" in NewRole:
            assert True
            time.sleep(3)
            print(NewRole)
        else:
            self.driver.save_screenshot(".\\Screenshots\\CustomerRole\\" + "test_addCustomerRole_src2.png")
            assert False

        self.driver.close()
        self.logger.info("***************************** Ending test_AddCustomerRole_4 **************************")



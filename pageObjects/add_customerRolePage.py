import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Add_customerRole:
    # adding customer role
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomerRole_menuitem_xpath = "//ul/li/a[@href='/Admin/CustomerRole/List']"
    lnkAddNew_Create_xpath = "//div/a[@href='/Admin/CustomerRole/Create']"
    inputName_xpath = "//div/input[@id='Name']"
    chkboxFreeshipping_xpath = "//div/input[@name='FreeShipping']"
    chkboxTaxExempt_xpath = "//div/input[@name='TaxExempt']"
    inputSystemName_xpath = "//div/input[@name='SystemName']"
    btnSave_xpath = "//div/button[@name='save']"
    table_xpath = "//table[@id='customerroles-grid']"
    # tableRows = "tr"
    # table1stColumn_xpath = "//table/tbody/tr/td[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickOnCustomerRoleMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomerRole_menuitem_xpath).click()

    def clickOnAddNew_Create(self):
        self.driver.find_element(By.XPATH, self.lnkAddNew_Create_xpath).click()

    def setName(self, Name):
        self.driver.find_element(By.XPATH, self.inputName_xpath).send_keys(Name)

    def clickOnCheckbox_FreeShipping(self):
        self.driver.find_element(By.XPATH, self.chkboxFreeshipping_xpath).click()

    def clickOnCheckbox_TaxExempt(self):
        self.driver.find_element(By.XPATH, self.chkboxTaxExempt_xpath).click()

    def setSystemName(self, SystemName):
        self.driver.find_element(By.XPATH, self.inputSystemName_xpath).send_keys(SystemName)

    def clickOnSaveBtn(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()

    def selectTable1stColumn(self):
        RoleName = self.driver.find_element(By.TAG_NAME, "tbody").text
        return RoleName







import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class exportCustomer:
    # Export customer
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']"
    tblMainCheckbox1_xpath = "//tbody/tr/td/input[@value='6']"
    tblMainCheckbox2_xpath = "//tbody/tr/td/input[@value='5']"
    tblMainCheckbox3_xpath = "//tbody/tr/td/input[@value='4']"
    drpdownButton_export_xpath = "//div[@class='btn-group']//button[@data-toggle='dropdown']"
    btnExport_XML_Selected_xpath = "//ul[@class='dropdown-menu show']//button[@id='exportxml-selected']"
    btnExport_XML_ALL_xpath = "//ul/li/button[@name='exportxml-all']"
    btnExport_Excel_Selected_xpath = "//ul/li/button[@id='exportexcel-selected']"
    btnExport_Excel_All_xpath = "//ul/li/button[@name='exportexcel-all']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def clickOnTableMainCheckbox(self):
        self.driver.find_element(By.XPATH, self.tblMainCheckbox1_xpath).click()
        self.driver.find_element(By.XPATH, self.tblMainCheckbox2_xpath).click()
        self.driver.find_element(By.XPATH, self.tblMainCheckbox3_xpath).click()

    def clickOnExportDropdownBtn(self):
        self.driver.find_element(By.XPATH, self.drpdownButton_export_xpath).click()

    def clickOnExportXML_SelectedBtn(self):
        self.driver.find_element(By.XPATH, self.btnExport_XML_Selected_xpath).click()

    def clickOnExportXML_ALLBtn(self):
        self.driver.find_element(By.XPATH, self.btnExport_XML_ALL_xpath).click()

    def clickOnExportEXCEl_SelectedBtn(self):
        self.driver.find_element(By.XPATH, self.btnExport_Excel_Selected_xpath).click()

    def clickOnExportEXCEL_AllBtn(self):
        self.driver.find_element(By.XPATH, self.btnExport_Excel_All_xpath).click()


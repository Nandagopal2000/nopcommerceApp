import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class EditCustomer:
    # Editing the Customer details
    iconSearch_Click_Btn_xpath = "//div/div[@class='icon-collapse']"
    lnkCustomers_Edit_Btn_xpath = "//tbody/tr[@class='odd']//td/a[@href='Edit/5']"
    txtFirstName_Edit_xpath = "//div/input[@id='FirstName']"
    txtLastName_Edit_xpath = "//div/input[@id='LastName']"
    txtCompanyName_Edit_xpath = "//div/input[@id='Company']"
    btnSave_Edit_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnSearchAngleUpIcon(self):
        self.driver.find_element(By.XPATH, self.iconSearch_Click_Btn_xpath).click()

    def clickOnCustomerEditBtn(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_Edit_Btn_xpath).click()

    def renameFirstName(self, FirstName):
        self.driver.find_element(By.XPATH, self.txtFirstName_Edit_xpath).click()
        self.driver.find_element(By.XPATH, self.txtFirstName_Edit_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtFirstName_Edit_xpath).send_keys(FirstName)

    def renameLastName(self, LastName):
        self.driver.find_element(By.XPATH, self.txtLastName_Edit_xpath).click()
        self.driver.find_element(By.XPATH, self.txtLastName_Edit_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtLastName_Edit_xpath).send_keys(LastName)

    def renameCompanyName(self, CompanyName):
        self.driver.find_element(By.XPATH, self.txtCompanyName_Edit_xpath).click()
        self.driver.find_element(By.XPATH, self.txtCompanyName_Edit_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtCompanyName_Edit_xpath).send_keys(CompanyName)

    def clickOnSaveBtn(self):
        self.driver.find_element(By.XPATH, self.btnSave_Edit_xpath).click()


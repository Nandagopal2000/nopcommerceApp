import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class DeleteCustomer:
    # Editing the Customer details
    iconSearch_Click_Btn_xpath = "//div/div[@class='icon-collapse']"
    lnkCustomers_Edit_Btn_xpath = "//tbody/tr/td/a[@href='Edit/116']"
    btnCustomers_Delete_Btn_xpath = "//div/span[@id='customer-delete']"
    btnCustomers_Delete_ExtraBtn_xpath = "//button[@class='btn btn-danger float-right']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnSearchAngleUpIcon(self):
        self.driver.find_element(By.XPATH, self.iconSearch_Click_Btn_xpath).click()

    def clickOnCustomerEditBtn(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_Edit_Btn_xpath).click()

    def clickOnCustomerDeleteBtn(self):
        self.driver.find_element(By.XPATH, self.btnCustomers_Delete_Btn_xpath).click()

    def clickOnCustomerDeleteExtraBtn(self):
        self.driver.find_element(By.XPATH, self.btnCustomers_Delete_ExtraBtn_xpath).click()


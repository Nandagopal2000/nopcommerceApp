import pytest
from selenium import webdriver
# from pytest_metadata import plugin


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        print("Launching Chrome Browser.............")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        driver.implicitly_wait(30)
        print("Launching FireFox Browser............")
    elif browser == 'edge':
        driver = webdriver.Edge()
        driver.implicitly_wait(30)
        print("Launching Edge Browser...............")
    else:
        driver = webdriver.Ie()
        driver.implicitly_wait(30)

    return driver

def pytest_addoption(parser):  # This will get the value from CLI / hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):   # This will return the browser value to setup method
    return request.config.getoption("--browser")

##########################   PyTest HTML Report   ######################


# # It is hook for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config.metadata['Project Name'] = 'nop Commerce'
#     config.metadata['Module Name'] = 'Customers'
#     config.metadata['Tester'] = 'Nandu'
# #
# # # It is hook for delete/modify environment info to HTML report
# #
# @pytest.mark.optionalhook(tryfirst=True)
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)

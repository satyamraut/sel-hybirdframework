import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("******** SearchCustomerByName_005 ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******** Login Successful ********")
        self.logger.info("******** Starting Search Customer By Name ********")
        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomersMenu()
        self.addCust.clickOnCustomersMenuItem()
        self.logger.info("******** Searching Customer By Name ********")
        searchCust = SearchCustomer(self.driver)
        searchCust.setFirstName("Victoria")
        searchCust.setLastName("Terces")
        searchCust.clickSearch()
        time.sleep(5)
        status = searchCust.searchCustomerByName("Victoria Terces")
        self.driver.close()
        assert True == status
        self.logger.info("******** TC_SearchCustomerByName_005 Finished ********")



import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("******** SearchCustomerByEmail_004 ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******** Login Successful ********")
        self.logger.info("******** Starting Search Customer By Email ********")
        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomersMenu()
        self.addCust.clickOnCustomersMenuItem()
        self.logger.info("******** Searching Customer By Email ID ********")
        searchCust = SearchCustomer(self.driver)
        searchCust.setEmail("victoria_victoria@nopCommerce.com")
        searchCust.clickSearch()
        time.sleep(5)
        status = searchCust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("******** TC_SearchCustomerByEmail_004 Finished ********")
        self.driver.close()


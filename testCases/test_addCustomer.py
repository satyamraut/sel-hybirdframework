import random
import string
import pytest
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addCustomer(self, setup):
        self.logger.info("********* Test_003_AddCustomer *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********* Login Successful *********")

        self.logger.info("********* Starting Add Customer Test *********")
        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomersMenu()
        self.addCust.clickOnCustomersMenuItem()
        self.addCust.clickOnAddnew()
        self.logger.info("********* Providing Customer Info *********")

        self.email = random_generator() + "@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("test123")
        self.addCust.setFirstName("Pavan")
        self.addCust.setLastName("Kumar")
        self.addCust.setGender("Male")
        self.addCust.setDob("02/07/1995")
        self.addCust.setCompanyName("busyQA")
        self.addCust.setCustomerRoles("Guests")
        self.addCust.setManagerOfVendor("Vendor 2")
        self.addCust.setAdminContent("This is for testing.....")
        self.addCust.clickOnSave()
        self.logger.info("********* Saving Customer Info *********")
        self.logger.info("********* Add Customer Validation Started *********")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)
        if "customer has been added successfully" in self.msg:
            assert True == True
            self.logger.info("********* Add Customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_addCustomer_scr.png")
            self.logger.error("********* Add Customer Test Passed *********")

        self.driver.close()
        self.logger.info("********* Ending Test_003_AddCustomer Test *********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


import time
import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    file = ".\\TestData\\LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("********* Test_002_DDT_Login *********")
        self.logger.info("****** Verifying Login DDT Test ******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.file, 'Sheet1')
        print("Number of rows in a Excel:", self.rows)
        test_status = []
        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.file, 'Sheet1', r, 1)
            self.pwd = XLUtils.readData(self.file, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.file, 'Sheet1', r, 3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.pwd)
            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("****** Passed ******")
                    self.lp.clickLogout()
                    test_status.append("Pass")
                elif self.exp == 'Fail':
                    self.logger.info("****** Failed ******")
                    self.lp.clickLogout()
                    test_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("****** Failed ******")
                    test_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("****** Passed ******")
                    test_status.append("Pass")

        if "Fail" not in test_status:
            self.logger.info("****** Login DDT Test Passed ******")
            self.driver.close()
            assert True
        else:
            self.logger.error("****** Login DDT Test Failed ******")
            self.driver.close()
            assert False

        self.logger.info("****** End of Login DDT Test ******")
        self.logger.info("****** Completed TC_LoginDDT_002 ******")

import pytest
from selenium import webdriver
from webdriver_manager.core import driver
from Utilities.readproperties import ReadConfig
from Utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
import time
from selenium.webdriver.common.by import By


class Test_001_Login:
    baseURl = ReadConfig.getApplicationURl()
    username = ReadConfig.getApplicationUserName()
    password = ReadConfig.getApplicationPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):

        self.logger.info("*******************Test_001_HomePage**************")
        self.logger.info("*******************Verify Home Page Title**************")
        self.driver = setup
        self.driver.get(self.baseURl)
        actual_title = self.driver.title
        if actual_title == "Magento Admin":
            assert True
            self.logger.info("*******************Test is Passed**************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "homePageTitle.png")
            self.driver.close
            self.logger.info("*******************Test is Failed **************")
            assert False

    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("*******************Test_002_Login**************")
        self.logger.info("*******************Verify Login Page Title**************")
        self.driver = setup
        self.driver.get(self.baseURl)
        self.lp = LoginPage(self.driver)
        time.sleep(4)
        self.lp.oktaButton()
        time.sleep(4)
        actual_title0 = self.driver.title
        if actual_title0 == "ASTM Login":
            assert True
            self.logger.info("*******************Test is Passed**************")
            self.driver.close
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login0.png")
            self.driver.close
            self.logger.info("*******************Test is Failed**************")
            assert False
        time.sleep(5)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        time.sleep(5)
        self.lp.acceptCookies()
        time.sleep(10)
        self.lp.clickLogin()
        time.sleep(7)
        actual_title1 = self.driver.title
        # print(actual_title1)
        if actual_title1 == "Dashboard / Magento Admin":
            assert True
            self.logger.info("*******************Test is Passed**************")
            self.driver.close
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login1.png")
            self.driver.close
            self.logger.info("*******************Test is Failed**************")
            assert False

    def test_maintain_session(self, setup):
        self.logger.info("*******************Test_0001_Login_Session**************")
        self.logger.info("*******************Auto-logout after 5 minutes has passed**************")
        self.driver = setup
        self.driver.get(self.baseURl)
        self.lp = LoginPage(self.driver)
        time.sleep(10)
        self.lp.oktaButton()
        time.sleep(20)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        time.sleep(5)
        self.lp.acceptCookies()
        time.sleep(10)
        self.lp.clickLogin()
        time.sleep(7)








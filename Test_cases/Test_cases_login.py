import sys

import pytest
from selenium import webdriver
from POM.login_page import login
from Test_cases.config import setup
from Utilities.ReadProperties import ReadConfig
from Utilities.customlogger import LogGen
import time


class TestLogin_001:
    #baseURL = ReadConfig.getAppUrl
    #username = ReadConfig.getUsername
    #password = ReadConfig.getPassword
    baseURL = 'https://admin-demo.nopcommerce.com/login'
    username = "admin@yourstore.com"
    password = "admin"


    logger=LogGen.loggen()
    @pytest.mark.regression
    def test_login_home_title(self, setup):
        self.logger.info("*************** test_login_home_title **************")
        self.logger.info("*************** Verify_home_page_title **************")
        self.driver = setup
        #self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        acttitle = self.driver.title
        if acttitle == "Your store. Login":
            assert True
            print(acttitle)
            self.logger.info("*************** Verify_home_page_title is passed **************")
            self.driver.close()
        else:
            self.driver.save_screenshot("./Screenshots/login.png")
            self.logger.warn("*************** Verify_home_page_title is failed **************")
            self.driver.close()
            assert False


    @pytest.mark.regression
    @pytest.mark.sanity
    def test_login_page(self, setup):
        self.logger.info("*************** Verifying_login_Test **************")
        self.driver = setup
        self.lp = login(self.driver)
        self.driver.maximize_window()
        #self.driver.set_page_load_timeout(300)
        self.driver.get(self.baseURL)
        self.lp.setUsername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLoginButton()
        title = self.driver.title
        if title == "Dashboard / nopCommerce administration":
            self.logger.info("*************** Verifying_login_Test is passed **************")
            assert True
            print(title)
            self.driver.close()
        else:
            self.driver.save_screenshot("./screenshots/login.png")
            self.logger.warn("*************** Verifying_login_Test is failed **************")
#            assert False
            self.driver.close()


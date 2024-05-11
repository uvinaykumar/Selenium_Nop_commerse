import pytest

from POM.login_page import login
from Test_cases.config import setup
from POM.Search_customer import Search_customer
from Utilities.ReadProperties import ReadConfig
from Utilities.customlogger import LogGen
from POM.AddCustomer import AddCustomer
import time

class Test_003_search_customers:
    baseURL = 'https://admin-demo.nopcommerce.com/login'
    username = "admin@yourstore.com"
    password = "admin"

    logger = LogGen.loggen()
    @pytest.mark.regression
    def test_search_by_email(self, setup):
        self.logger.info('************ test_Search Customer ***************')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLoginButton()
        time.sleep(3)
        self.logger.info('***** login successful *****')
        self.driver.maximize_window()

        self.add_cust = AddCustomer(self.driver)
        self.add_cust.customer_main_menu()
        self.add_cust.customer_sub_menu()

        self.logger.info(" ***** Search cusromer by email is started ****** ")
        self.search_by_name = Search_customer(self.driver)
        time.sleep(3)
        self.search_by_name.SearchEmail("admin@yourStore.com")
        self.search_by_name.clck_search()
        status1=self.search_by_name.SearchEmail("admin@yourStore.com")
        if "admin@yourStore.com" == status1:
            self.logger.info("******* Search customer by email is finished and passed ******* ")
            self.driver.close()
        self.logger.info("******* Search customer by email is finished and passed ******* ")
        self.driver.close()

        #self.logger.info(" ***** Search cusromer by name is started ****** ")
        #self.search_by_name.search_customer_by_name("John")
        #self.search_by_name.clck_search()
        #status1 = self.search_by_name.search_customer_by_name("John")
        #if "John" == status1:
         #   self.logger.info(" ***** Search cusromer by name is finished ****** ")




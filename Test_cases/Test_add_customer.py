import pytest
import secrets
import string
import time
from selenium.webdriver.common.by import By
from POM.login_page import login
from POM.AddCustomer import AddCustomer
from Test_cases.config import setup
from Utilities.customlogger import LogGen
from Utilities.ReadProperties import ReadConfig


class Test_002_AddCustomer:
    baseURL = 'https://admin-demo.nopcommerce.com/login'
    username = "admin@yourstore.com"
    password = "admin"

    logger = LogGen.loggen()
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_AddCustomer_title(self,setup):
        self.logger.info(msg='************ test_AddCustomer ***************')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLoginButton()
        time.sleep(1)
        self.logger.info('***** login successful *****')
        self.driver.maximize_window()
        self.add_cust = AddCustomer(self.driver)
        self.add_cust.customer_main_menu()
        self.add_cust.customer_sub_menu()
        add_title = self.driver.title
        if add_title == "Add a new customer / nopCommerce administration":
            self.logger.info("***** Add new customer title get successfully *****")
            #assert True
        else:
            self.driver.get_screenshot_as_png()
            self.logger.warn("**** Add new customer title get failed *****")
            #assert True != False

    def test_add_customer(self,setup):
        self.logger.info("*************** Verifying_Add_customer_Test **************")
        self.driver = setup
        #Login code
        self.logger.info("******* loggin page initiated ******")
        self.lp = login(self.driver)
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp.setUsername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLoginButton()
        self.logger.info('***** login successful *****')
        time.sleep(3)
        #Add Customer
        self.logger.info("**** Providing customer Details ****")
        self.add_cust = AddCustomer(self.driver)
        self.add_cust.customer_main_menu()
        self.add_cust.customer_sub_menu()
        self.add_cust.add_customer()
        self.email = self.random_gr()
        self.add_cust.Email(self.email + "@vendor.com")
        self.add_cust.password("Test1234")
        self.add_cust.firstname("syam")
        self.add_cust.lastname("kumar")
        self.add_cust.gender("Male")
        self.add_cust.dob("15/05/1999")
        self.add_cust.company_name("QA test")
        self.add_cust.tax()
        time.sleep(3)
        self.add_cust.m_vendor('Vendor 1')
        #self.add_cust.chk_box()
        #time.sleep(3)
        self.add_cust.customer_roles("Guests")
        self.add_cust.save()

        self.logger.info("***** saving customer info *****")

        self.logger.info("**** Test Add customer Inetiated ****")

        self.msg = self.driver.find_element(by=By.TAG_NAME, value="body").text
        if 'The new customer has been added successfully' in self.msg:
            self.logger.info("***** Test add customer passed *****")
            self.driver.close()
        else:
            self.driver.get_screenshot_as_file("D:\Local_Disk\Selenium_practice_v4\Selenium_Nop_commerse\Screen_Shots\Add_customer_failed.png")
            self.logger.error('***** Add customer test case failed *****')
            self.driver.close()
            #assert False

    def random_gr(char=8):
        return "".join(secrets.choice(string.ascii_lowercase+string.digits) for _ in range(8))

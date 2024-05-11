import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:
    link_customer_main_menu_xpath ='//body/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]'
    link_customer_sub_menu_xpath = '/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p'
    btn_add_customer_xpath = "//a[@class='btn btn-primary']"
    txtbox_email_id = "Email"
    txtbox_password_id = "Password"
    txtbox_first_name_id = "FirstName"
    txtbox_last_name_name = "LastName"
    rd_male_id = "Gender_Male"
    rd_female_id = "Gender_Female"
    txtbox_dob_xpath = "//input[@name='DateOfBirth']"
    txtbox_company_name_id = "Company"
    chkbox_is_tax_exempt_id = "IsTaxExempt"
    txtbox_newsletter_store_name_xpath = "//li[@title='Your store name']"
    txtbox_newsletter_test_store_xpath = "//li[@title='Test store 2']"
    del_store_name_xpath = "//li[@title='Your store name']//span[@role='presentation'][normalize-space()='×']"
    del_test_store_xpath = "//li[@title='Test store 2']//span[@role='presentation'][normalize-space()='×']"
    lstcustomer_role_xpath = "//span[@aria-expanded='true']//input[@role='searchbox']"
    lst_cutomer_roles_registered_xpath = "//li[contains(text(),'Registered')]"
    lst_cutomer_roles_Administrator_xpath = "//li[contains(text(),'Administrators')]"
    lst_cutomer_roles_vendor_xpath = "//li[contains(text(),'Vendors')]"
    lst_cutomer_roles_guest_xpath = "//li[contains(text(),'Guests')]"
    lst_cutomer_roles_ForumModerators_xpath = "//li[contains(text(),'Forum Moderators')]"
    del_regestired_xpath = "//li[@title='Registered']//span[@role='presentation'][normalize-space()='×']"
    del_Administrators_xpath = "//li[@title='Administrators']//span[@role='presentation'][normalize-space()='×']"
    del_Vendors_xpath = "//li[@title='Vendors']//span[@role='presentation'][normalize-space()='×']"
    del_Guests_xpath = "//li[@title='Guests']//span[@role='presentation'][normalize-space()='×']"
    del_Forum_Moderators_xpath = "//li[@title='Forum Moderators']//span[@role='presentation'][normalize-space()='×']"
    list_manage_vendor_id = "VendorId"
    chkbox_active_xpath = "//input[@id='Active']"
    btn_save_xpath = "//button[@name='save']"


    def __init__(self,driver):
        self.driver = driver

    def customer_main_menu(self):
        self.driver.find_element(by=By.XPATH,value=self.link_customer_main_menu_xpath).click()
        #self.driver.find_element(by=By.XPATH,value=self.link_customer_main_menu_xpath).send_keys()

    def customer_sub_menu(self):
        self.driver.find_element(by=By.XPATH, value=self.link_customer_sub_menu_xpath).click()

    def add_customer(self):
        self.driver.find_element(by=By.XPATH, value=self.btn_add_customer_xpath).click()

    def Email(self, Email):
        self.driver.find_element(by=By.ID, value=self.txtbox_email_id).clear()
        self.driver.find_element(by=By.ID, value=self.txtbox_email_id).send_keys(Email)
    def password(self,password):
        self.driver.find_element(by=By.ID, value=self.txtbox_password_id).clear()
        self.driver.find_element(by=By.ID, value=self.txtbox_password_id).send_keys(password)

    def firstname(self,first_name):
        self.driver.find_element(by=By.ID, value=self.txtbox_first_name_id).clear()
        self.driver.find_element(by=By.ID, value=self.txtbox_first_name_id).send_keys(first_name)

    def lastname(self,last_name):
        self.driver.find_element(by=By.ID, value=self.txtbox_last_name_name).clear()
        self.driver.find_element(by=By.ID, value=self.txtbox_last_name_name).send_keys(last_name)

    def gender(self,gender):
        if gender =='Male':
            self.driver.find_element(by=By.ID, value=self.rd_male_id).click()
        elif gender =='Female':
            self.driver.find_element(by=By.ID, value=self.rd_female_id).click()
        else:
            self.driver.find_element(by=By.ID, value=self.rd_male_id).click()

    def dob(self,dob):
        self.driver.find_element(by=By.XPATH, value=self.txtbox_dob_xpath).send_keys(dob)

    def company_name(self,company_name):
        self.driver.find_element(by=By.ID, value=self.txtbox_company_name_id).clear()
        self.driver.find_element(by=By.ID, value=self.txtbox_company_name_id).send_keys(company_name)

    def tax(self):
        self.driver.find_element(by=By.ID, value=self.chkbox_is_tax_exempt_id).click()
    #def news_letter(self,storename):
     #   self.driver.find_element(by=By.XPATH, value=self.txtbox_newsletter_store_name_xpath).click()
      #  if storename == "Test store":
       #     self.driver.find_element(by=By.XPATH, value=self.del_test_store_xpath).click()
        #    self.driver.find_element(by=By.XPATH, value=self.txtbox_newsletter_store_name_xpath)
        #else:
         #   self.driver.find_element(by=By.XPATH, value=self.txtbox_newsletter_store_name_xpath).click()

    def customer_roles(self,role):
        #self.driver.find_element(by=By.XPATH, value=self.lstcustomer_role_xpath).click()
        time.sleep(3)
        if role == "Registered":
            self.lstroles = self.driver.find_element(by=By.XPATH, value=self.lst_cutomer_roles_registered_xpath)
        elif role == 'Administartors':
            self.driver.find_element(by=By.XPATH, value=self.del_regestired_xpath).click()
            self.lstroles = self.driver.find_element(by=By.XPATH, value=self.lst_cutomer_roles_Administrator_xpath)
        elif role == "Guests":
            time.sleep(3)
            self.driver.find_element(by=By.XPATH, value=self.del_regestired_xpath).click()
            self.lstroles = self.driver.find_element(by=By.XPATH, value=self.lst_cutomer_roles_guest_xpath)
        elif role == 'Vendors':
            self.driver.find_element(by=By.XPATH, value=self.del_regestired_xpath).click()
            self.lstroles = self.driver.find_element(by=By.XPATH, value=self.lst_cutomer_roles_vendor_xpath)
        else:
            self.lstroles = self.driver.find_element(by=By.XPATH, value=self.lst_cutomer_roles_guest_xpath)
        time.sleep(3)
        self.lstroles.click()
        #self.driver.execuite_scripts("argument[0].click();", self.lstroles)

    def m_vendor(self,vendor):
        vdr = Select(self.driver.find_element(by=By.ID, value=self.list_manage_vendor_id))
        vdr.select_by_visible_text(vendor)

    def chk_box(self):
        self.driver.find_element(by=By.XPATH, value=self.chkbox_active_xpath).click()

    def save(self):
        self.driver.find_element(by=By.XPATH, value=self.btn_save_xpath).click()



































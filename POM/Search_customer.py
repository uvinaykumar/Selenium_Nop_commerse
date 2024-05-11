from selenium.webdriver.common.by import By
import pytest

class Search_customer():
    txtbox_email_id = 'SearchEmail'
    txtbox_name_id = 'SearchFirstName'
    txtbox_last_name_id = 'SearchLastName'
    btn_search_id = 'search-customers'
    #search expand
    btn_search_expand_xpath = "//div[@class='row search-row']"

    table_result_customers_xpath = "//table[@id='customers-grid']"
    #table_xpath = "//div[@id='customers-grid_wrapper']"
    table_row_xpath = "//table[@id='customers-grid']//tbody/tr"
    table_column_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver = driver
    def SearchEmail(self,Email):
        if self.driver.find_element(by=By.ID, value=self.txtbox_email_id).is_displayed() == True:
            self.driver.find_element(by=By.ID, value=self.txtbox_email_id).clear()
            self.driver.find_element(by=By.ID, value=self.txtbox_email_id).send_keys(Email)
        else:
            self.driver.find_element(by=By.XPATH, value=self.btn_search_expand_xpath).click()
            self.driver.find_element(by=By.ID, value=self.txtbox_email_id).clear()
            self.driver.find_element(by=By.ID, value=self.txtbox_email_id).send_keys(Email)
    def search_first_name(self,Fname):
        self.driver.find_element(by=By.ID, value=self.txtbox_name_id).clear()
        self.driver.find_element(by=By.ID, value=self.txtbox_name_id).send_keys(Fname)
    def search_last_name(self,Lname):
        self.driver.find_element(by=By.ID, value=self.txtbox_last_name_id).clear()
        self.driver.find_element(by=By.ID, value=self.txtbox_last_name_id).send_keys(Lname)
    def clck_search(self):
        self.driver.find_element(by=By.ID, value=self.btn_search_id).click()
    def get_row_count(self):
        rows = self.driver.find_element(by=By.ID, value=self.table_row_xpath)
        return len(rows)

    def get_colomn_count(self):
        return len(self.driver.find_element(by=By.ID, value=self.table_column_xpath))
    def search_customer_by_email(self, email, table1=None):
        flag = False
        for i in range(1,self.get_row_count()+1):
            table1 = self.driver.find_element(by=By.XPATH, value=self.table_result_customers_xpath)
            emailid = table1.find_element(by=By.XPATH, value="//table[@id='customers-grid']//tbody/tr["+str(i)+"]/td[2]").text()
            if emailid == email:
                flag = True
                break
        return flag



    def search_customer_by_name(self,firstname):
        flag = False
        for i in range(1,self.get_row_count()+1):
            table2 = self.driver.find_element(by=By.XPATH, value=self.table_result_customers_xpath)
            fname = table2.find_element(by=By.XPATH, value="//table[@id='customers-grid']//tbody/tr["+str(i)+"/td[3]").text()
            if fname == firstname:
                flag = True
                break
        return flag




























import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class CompareAndSwitchTestCase(unittest.TestCase):
    site = 'https://sparkenergy.co.uk/compare'
    siteTitle = 'Price comparison'

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(15)
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get(self.site)
        self.assertIn(self.siteTitle, self.browser.title)

 #       self.browser.implicitly_wait(15)
        # close cookies notice
#        self.browser.find_element_by_xpath("//div[1]/div/a[1]").click()
        # self.browser.find_element_by_css_selector(".cc_btn").click()
        # self.browser.find_element_by_xpath("//a[contains(@class,'cc_btn_accept_all')]").click()

#        dismiss = self.browser.findElement();

#css=a.cc_btn.cc_btn_accept_all

        wait = WebDriverWait(self.browser, 30)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@class='cc_btn cc_btn_accept_all']")))
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='cc_btn cc_btn_accept_all']")))
        time.sleep(2)
        element.click()
        # "before we start -- do you have a spark account?" --> No
        self.browser.find_element_by_xpath("//div[@id='beforeWeStart']/div/div/label[2]").click()
#        self.browser.find_element_by_xpath("//input[@id='isCustomerN']").click()

        # Enter post code
        self.browser.find_element_by_xpath("//input[@id='userInitialPostcode']").send_keys("EH49 7JJ")
        # xpath: //*[@id='userInitialPostcode']

        # "do you already live here?" --> yes (default selected)

        # "What type of quote?" --> Gas + electric
#        self.browser.find_element_by_xpath("//input[@id='quoteType3']").click()
        self.browser.find_element_by_xpath("//label[@class='spark-icon-radio-label both large']").click()
#        self.browser.find_element_by_xpath("//div[@id='wizard-p-0']/div[7]/div/div[2]/label[3]").click()

        # payment method --> monthly direct debit (default selected)

        # Click next to continue
#        self.browser.find_element_by_xpath("//main/div[1]/ul/li[2]").click()
        self.browser.find_element_by_xpath("//li[contains(@class, 'next') and contains(@class, 'button')]/span").click()
        # self.browser.find_element_by_xpath("//div[@id='wizard-p-1']/div[2]/div/div[3]/label[2]").click()


        # "do you know your current supplier?" --> No

        self.browser.find_element_by_xpath("//div[@id='wizard-p-1']/div[2]/div/div[3]/label[2]").click()
#        self.browser.find_element_by_xpath("//div[@id='dontKnowCurrentSupplierRow']/div/div[2]/div/div[3]/ul/li[4]").click()
        # choose number of bedrooms --> 3 (drop-down)
#        self.browser.find_element_by_xpath("//div[@id='dontKnowCurrentSupplierRow']/div/div[2]/div/div[3]/ul/li[4]").click()
        self.browser.find_element_by_xpath("//div[contains(@class, 'selectricWrapper')]").click()
#        self.browser.find_element_by_xpath("//div[@class='selectric']/p[@class='label']").click()
        self.browser.find_element_by_xpath("//div[@class='selectricItems']/ul/li[4]").click()

        # economy 7 meter installed? --> no (default selected)

        # click next to continue
        self.browser.find_element_by_xpath("//main/div/ul/li[2]").click()
        #self.browser.find_element_by_xpath("//li[contains(@class, 'next') and contains(@class, 'button')]").click()


        ### VERIFICATION
#        tariffs = self.browser.find_elements_by_xpath("//div[@id=type-1]/div[@class='tariff-block']")
        tariffs = self.browser.find_elements_by_xpath("//div[@class='tariff-block']")
#        assert len(tariffs) is 5
        self.assertEqual(5, len(tariffs))
        print("Passed")


if __name__ == '__main__':
    unittest.main(verbosity=2)

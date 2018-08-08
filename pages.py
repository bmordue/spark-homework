from locators import Locators

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


class ComparePage():
    site = 'https://sparkenergy.co.uk/compare'

    def __init__(self, browser):
        self.browser = browser

    def click(self, locator):
        self.browser.find_element(*locator).click()

    def click_accept_cookies(self):
        wait = WebDriverWait(self.browser, 30)
        element = wait.until(EC.visibility_of_element_located(Locators.ACCEPT_COOKIES_BTN))
        element = wait.until(EC.element_to_be_clickable(Locators.ACCEPT_COOKIES_BTN))
        time.sleep(2)
        element.click()

    def click_no_spark_account(self):
        self.browser.find_element(*Locators.NO_SPARK_ACCOUNT_RADIO).click()

    def enter_postcode(self, postcode):
        el = self.browser.find_element(*Locators.POSTCODE_TEXT_FIELD)
        el.send_keys(postcode)

    def click_combined_quote(self):
        self.click(Locators.COMBINED_QUOTE_BTN)

    def click_next(self):
        self.click(Locators.NEXT_BTN)

    def click_supplier_not_known(self):
        self.click(Locators.SUPPLIER_NOT_KNOWN_RADIO)

    def pick_bedrooms(self, num_bedrooms):
        self.click(Locators.BEDROOMS_DROP_DOWN)
        self.click(Locators.bedroom_number_selection(num_bedrooms))

    def extract_tariffs(self):
        time.sleep(2)
        elements = self.browser.find_elements(*Locators.TARIFF_ELEMENTS)
        extracted = []
        for el in elements:
            tariff_name_el = el.find_element_by_xpath("//h3/span[1]")
            tariff_name = tariff_name_el.text
            tariff_projection = el.find_element_by_xpath("//span[@class='dynamic tariff-projection']").text
            extracted.append([tariff_name, tariff_projection])
        return extracted

    def extract_tariff_names(self):
        time.sleep(2)
        elements = self.browser.find_elements_by_xpath("//span[@class='dynamic tariff-name']")
        results = []
        for el in elements:
            if el.text:
                results.append(el.text)
        return results

    def extract_tariff_projections(self):
        elements = self.browser.find_elements_by_xpath("//span[@class='dynamic tariff-projection']")
        results = []
        for el in elements:
            if el.text:
                results.append(el.text)
        return results

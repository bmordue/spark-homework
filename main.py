import pages
import unittest
from selenium import webdriver


# Test scenario: get tariffs for a user without a current Spark account,
# combined quote, no smart meter, based on size of house (current supplier not known)
# Verify tariff names offered and projections.
class ComparePageTestCaseOne(unittest.TestCase):
    site = 'https://sparkenergy.co.uk/compare'

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get(self.site)

    def runTest(self):

        compare_page = pages.ComparePage(self.browser)

        compare_page.click_accept_cookies()

        compare_page.click_no_spark_account()

        compare_page.enter_postcode("EH49 7JJ")

        # "do you already live here?" --> yes (default selected)

        compare_page.click_combined_quote()

        # payment method --> monthly direct debit (default selected)

        compare_page.click_next()

        compare_page.click_supplier_not_known()

        compare_page.pick_bedrooms(3)

        # economy 7 meter installed? --> no (default selected)

        compare_page.click_next()

        ### VERIFICATION

        expected_tariffs = [["Simple Saver October 2019", "1087.11"],
          ["Simple Saver October 2019", "1111.11"],
          ["Super Tracker", "1139.8"],
          ["Digital Saver v1", "1141.06"],
          ["Comfort Saver November 2019", "1201.76"]]

        tariff_names = compare_page.extract_tariff_names()
        tariff_projections = compare_page.extract_tariff_projections()

        # arrange extracted tariff names and projects as the fixture data for easy comparison
        actual_tariffs = [[tariff_names[i], tariff_projections[i]] for i in range(len(tariff_names))]

        self.assertEqual(expected_tariffs, actual_tariffs)

    def tearDown(self):
        self.browser.close()

# Test scenario: as above, but get a quote for electricity only for a single bedroom in a different post code
class ComparePageTestCaseTwo(unittest.TestCase):
    site = 'https://sparkenergy.co.uk/compare'

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get(self.site)

    def runTest(self):

        compare_page = pages.ComparePage(self.browser)

        compare_page.click_accept_cookies()

        compare_page.click_no_spark_account()

        compare_page.enter_postcode("SW1E 5BA")

        # "do you already live here?" --> yes (default selected)

        compare_page.click_electricity_only()

        # payment method --> monthly direct debit (default selected)

        compare_page.click_next()

        compare_page.click_supplier_not_known()

        compare_page.pick_bedrooms(1)

        # economy 7 meter installed? --> no (default selected)

        compare_page.click_next()

        ### VERIFICATION

        expected_tariffs =  [['Simple Saver October 2019', '343.16'],
            ['Simple Saver October 2019', '355.16'],
            ['Digital Saver v1', '360.2'],
            ['Super Tracker', '366.6'],
            ['Comfort Saver November 2019', '393.85']]

        tariff_names = compare_page.extract_tariff_names()
        tariff_projections = compare_page.extract_tariff_projections()

        # arrange extracted tariff names and projects as the fixture data for easy comparison
        actual_tariffs = [[tariff_names[i], tariff_projections[i]] for i in range(len(tariff_names))]

        self.assertEqual(expected_tariffs, actual_tariffs)

    def tearDown(self):
        self.browser.close()

# Test scenario: using the quote type and usage as above, select the 'Super Tracker'
# Verify that the details for tariff are shown.
class ComparePageTestCaseThree(unittest.TestCase):
    site = 'https://sparkenergy.co.uk/compare'

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get(self.site)

    def runTest(self):

        compare_page = pages.ComparePage(self.browser)

        compare_page.click_accept_cookies()

        compare_page.click_no_spark_account()

        compare_page.enter_postcode("SW1E 5BA")

        # "do you already live here?" --> yes (default selected)

        compare_page.click_electricity_only()

        # payment method --> monthly direct debit (default selected)

        compare_page.click_next()

        compare_page.click_supplier_not_known()

        compare_page.pick_bedrooms(1)

        # economy 7 meter installed? --> no (default selected)

        compare_page.click_next()

        new_tariff = 'Super Tracker'
        compare_page.select_tariff(new_tariff)

        ### VERIFICATION

        self.assertEqual(new_tariff, compare_page.extract_new_tariff())

    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)

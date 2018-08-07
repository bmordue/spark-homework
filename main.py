import pages
import unittest
from selenium import webdriver

class CompareAndSwitchTestCase(unittest.TestCase):
    site = 'https://sparkenergy.co.uk/compare'

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get(self.site)

    def testPageTitle(self):

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
        expected = 5
        actual = compare_page.count_tariffs()
        self.assertEqual(expected, actual)

        compare_page.verify_expected_tariff()

    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)

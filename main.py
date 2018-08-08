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

        expected_tariffs = [["Simple Saver October 2019", "1087.11"],
          ["Simple Saver October 2019", "1111.11"],
          ["Super Tracker", "1139.8"],
          ["Digital Saver v1", "1141.06"],
          ["Comfort Saver November 2019", "1201.76"]]

        tariff_names = compare_page.extract_tariff_names()
        tariff_projections = compare_page.extract_tariff_projections()

        actual_tariffs = [[tariff_names[i], tariff_projections[i]] for i in range(len(tariff_names))]
        # for i in len(tariff_names):
        #     actual_tariffs.append()


        # actual_tariffs = zip(tariff_names, tariff_projections)

        # if (expected_tariffs_tuples == actual_tariffs):
        #     print("tuple tariffs MATCH")
        # else:
        #     print("tuple tariffs DO NOT MATCH")



        # actual = list(map(list, actual_tariffs))

        self.assertEqual(expected_tariffs, actual_tariffs)

        # self.verify_tariffs(expected_tariffs, actual_tariffs)

    def tearDown(self):
        self.browser.close()

    # def verify_tariffs(expected, actual):
    #     self.assertEqual(len(expected_tariffs), len(actual_tariffs),
    #         'did not find the expected number of tariffs')

    #     for tariff in expected_tariffs:
    #         self.verify_tariff(tariff, actual_tariffs)

    # def verify_tariff()

if __name__ == '__main__':
    unittest.main(verbosity=2)

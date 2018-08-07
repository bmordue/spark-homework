from selenium.webdriver.common.by import By

class Locators(object):

    ACCEPT_COOKIES_BTN = (By.XPATH, "//a[@class='cc_btn cc_btn_accept_all']")

    NO_SPARK_ACCOUNT_RADIO = (By.XPATH, "//div[@id='beforeWeStart']/div/div/label[2]")

    POSTCODE_TEXT_FIELD = (By.XPATH, "//input[@id='userInitialPostcode']")

    COMBINED_QUOTE_BTN = (By.XPATH, "//label[@class='spark-icon-radio-label both large']")

    NEXT_BTN = (By.XPATH, "//li[contains(@class, 'next') and contains(@class, 'button')]/span")
#    NEXT_BTN = (By.XPATH, "//li[@class='button lime next']")

    SUPPLIER_NOT_KNOWN_RADIO = (By.XPATH, "//div[@id='wizard-p-1']/div[2]/div/div[3]/label[2]")

    BEDROOMS_DROP_DOWN = (By.XPATH, "//div[contains(@class, 'selectricWrapper')]")

    TARIFF_ELEMENTS = (By.XPATH, "//div[@class='tariff-block']")
#    TARIFF_ELEMENTS = (By.XPATH, "//div")

    def bedroom_number_selection(num):
    	xpath = "//div[@class='selectricItems']/ul/li[{}]".format(num + 1)
    	return (By.XPATH, xpath)

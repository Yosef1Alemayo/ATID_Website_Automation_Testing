from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from Web.Locators.website_locators import Website_Locators

class Website_Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        self.searchLink = Website_Locators.SEARCH_LINK
        self.validationForSearchLink = Website_Locators.VALIDATION_FOR_SEARCH_LINK
        self.searchInput = Website_Locators.SEARCH_INPUT
        self.prodsLength = Website_Locators.PRODS_LENGTH

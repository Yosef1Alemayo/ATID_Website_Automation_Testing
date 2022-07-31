from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Web.Locators.website_locators import Website_Locators


class Website_Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        self.listOfLinks = Website_Locators.LINKS
        self.logoLink = Website_Locators.LOGO_LINK

    def click_navbar_link(self, number: int):
        locator = f'//nav[1]/div[1]/ul[1]/li[{number}]/a'
        link = self.driver.find_element(By.XPATH, locator)
        link.click()
        assert link.is_selected() == True
        return locator

    def click_on_logo_link(self):
        link = self.driver.find_element(By.XPATH, self.logoLink)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.logoLink)))
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.logoLink)))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.logoLink)))
        link.click()
        assert link.is_selected() == True

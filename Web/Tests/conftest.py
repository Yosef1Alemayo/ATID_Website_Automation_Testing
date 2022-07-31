import os.path
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from Web.Pages.website_page import Website_Page
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

class Fixtures:
    @pytest.fixture(autouse=True)
    def set_up(self, browser):
        if browser == 'chrome':
            print('\n------------------------------')
            print('Initialing Chrome Driver')
            print('------------------------------')
            path = 'C://Users/yossi/PycharmProjects/python_Lessons/Selenium/Drivers/ChromeWebDriver/chromedriver.exe'
            self.driver = webdriver.Chrome(executable_path=path)
            print('\n------------------------------')
            print('Test is Started')
            print('------------------------------')
            self.driver.implicitly_wait(25)
            self.driver.maximize_window()
            yield self.driver
            if self.driver is not None:
                print("\n----------------------------")
                print("Tests is finished")
                print('----------------------------')
                self.driver.close()
                self.driver.quit()
        elif browser == 'firefox':
            print('\n------------------------------')
            print('Initialing FireFox Driver')
            print('------------------------------')
            path = 'C://Users/yossi/PycharmProjects/python_Lessons/Selenium/Drivers/FireFoxWebDriver/geckodriver.exe'
            self.driver = webdriver.Firefox(service_log_path=os.path.devnull, executable_path=path)
            print('\n------------------------------')
            print('Test is Started')
            print('------------------------------')
            self.driver.implicitly_wait(25)
            self.driver.maximize_window()
            yield self.driver
            if self.driver is not None:
                print("\n----------------------------")
                print("Tests is finished")
                print('----------------------------')
                self.driver.close()
                self.driver.quit()
        else:
            raise ValueError('No Driver')

    @pytest.fixture()
    def url_navigation(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(25)
        assert url == self.driver.current_url

    @pytest.fixture()
    def click_nav_bar_links(self):
        s = Website_Page(self.driver)
        self.wait = WebDriverWait(self.driver, 30)
        counter = 1
        locator = f'//nav[1]/div[1]/ul[1]/li[{counter}]/a'
        while counter <= 7:
            try:
                self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
                self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
                s.click_navbar_link(counter)
                counter += 1
            except StaleElementReferenceException:
                counter += 1


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="my option: chrome or firefox"
                    )
@pytest.fixture(autouse=True)
def browser(request):
    return request.config.getoption("--browser")

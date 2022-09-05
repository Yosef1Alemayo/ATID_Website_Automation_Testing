import os.path
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Fixtures:
    @staticmethod
    def gh_token():
        path = 'C://Users//yossi//PycharmProjects//python_Lessons/gh_token.txt'
        token = open(path).read()
        return token

    @pytest.fixture(autouse=True)
    def set_up(self, browser):
        if browser == 'chrome':
            print('\n------------------------------')
            print('Initialing Chrome Driver')
            print('------------------------------')
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
            print('\n------------------------------')
            print('Test is Started')
            print('------------------------------')
        elif browser == 'firefox':
            print('\n------------------------------')
            os.environ['GH_TOKEN'] = self.gh_token()
            print('Initialing FireFox Driver')
            print('------------------------------')
            self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
            print('\n------------------------------')
            print('Test is Started')
            print('------------------------------')
        else:
            raise ValueError('No Driver')
        self.driver.implicitly_wait(25)
        self.driver.maximize_window()
        yield self.driver
        if self.driver is not None:
            print("\n----------------------------")
            print("Tests is finished")
            print('----------------------------')
            self.driver.close()
            self.driver.quit()

    @pytest.fixture()
    def url_navigation(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(25)
        assert url == self.driver.current_url


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="my option: chrome or firefox"
                    )

@pytest.fixture(autouse=True)
def browser(request):
    return request.config.getoption("--browser")

import os.path

import pytest
from selenium import webdriver

class Fixtures:
    @pytest.fixture(autouse=True)
    def set_up(self, browser):
        if browser == 'chrome':
            print('\n------------------------------')
            print('Initialing Chrome Driver')
            print('------------------------------')
            self.driver = webdriver.Chrome()
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
            self.driver = webdriver.Firefox(service_log_path=os.path.devnull)
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



def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="my option: chrome or firefox"
                    )
@pytest.fixture(autouse=True)
def browser(request):
    return request.config.getoption("--browser")

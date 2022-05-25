import pytest
from selenium import webdriver

class Base:
    @pytest.fixture(autouse=True)
    def set_up(self):
        print('Initialing Chrome Driver')
        print('-------------------------')
        path = '..//Drivers/chromedriver.exe'
        self.driver = webdriver.Chrome(path)
        print('Test is Started')
        print('-------------------------')
        self.driver.implicitly_wait(25)
        self.driver.maximize_window()
        yield self.driver
        if self.driver is not None:
            print("----------------------------")
            print("Tests is finished")
            self.driver.close()
            self.driver.quit()


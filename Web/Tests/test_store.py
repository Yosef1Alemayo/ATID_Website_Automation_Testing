import pytest
from Web.Tests.conftest import Fixtures
from Web.Pages.website_page import Website_Page

@pytest.mark.usefixtures('url_navigation')
@pytest.mark.parametrize('url', ['https://atid.store/store/'])
class Test_Store(Fixtures):

    def test1(self, click_nav_bar_links):
        pass

    def test2(self):
        driver = self.driver
        web = Website_Page(driver)
        web.click_on_logo_link()

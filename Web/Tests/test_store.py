import pytest
from Web.Tests.conftest import Fixtures
from Web.Pages.website_page import Website_Page

@pytest.mark.usefixtures('url_navigation')
@pytest.mark.parametrize('url', ['https://atid.store/store/'])
class Test_Store(Fixtures):
    def test_1(self):
        web = Website_Page(self.driver)
        web.search('AviAvi')

    def test_2(self):
        pass

    def test_3(self):
        pass

    def test_4(self):
        pass


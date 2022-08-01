import pytest
from Web.Tests.conftest import Fixtures

@pytest.mark.usefixtures('url_navigation')
@pytest.mark.parametrize('url', ['https://atid.store/about/'])
class Test_AboutUS(Fixtures):
    def test_1(self):
        pass

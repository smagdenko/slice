import pytest
from application import Applications


@pytest.fixture
def app(request):
    fixture=Applications()
    # driver = webdriver.Chrome() # enter path to the webdriver
    # request.addfinalizer(driver.quit)
    request.addfinalizer(fixture.destroy)
    return fixture


def test_deactivate_account(app):

    app.login(passw='qwerty1234', user='testuser166@aol.com')
    app.deactivate()








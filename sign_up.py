import pytest
from application import Applications


@pytest.fixture
def app(request):
    fixture=Applications()
    # driver = webdriver.Chrome() # enter path to the webdriver
    # request.addfinalizer(driver.quit)
    request.addfinalizer(fixture.destroy)
    return fixture


def test_signup(app):

    app.open_home_page()
    app.sign_up(passw='qwerty1234', passw_aol='qwerty1234!', user='testuser166@aol.com')
    # assert driver.current_url=='https://www.slice.com/bootstrap'
    app.log_out()







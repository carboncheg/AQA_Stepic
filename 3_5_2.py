import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome('C:\\tools\\chromedriver2\\chromedriver.exe')
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.classTest
class TestMainPage1():

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

# Чтобы запустить тесть с нужной маркировкой,
# нужно передать в командной строке параметр -m и нужную метку:
#
# pytest -s -v -m smoke 3_5_2.py
#
# Таким образом мы запустим лишь тесты с меткой smoke

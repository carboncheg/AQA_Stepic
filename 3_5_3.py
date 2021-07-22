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


class TestMainPage1:

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

# Предположим, у нас есть smoke-тесты, которые нужно запускать только для определенной операционной системы,
# например, для Windows 10. Зарегистрируем метку win10 в файле pytest.ini,
# а также добавим к одному из тестов эту метку.
#
# pytest -s -v -m "smoke and win10" 3_5_3.py
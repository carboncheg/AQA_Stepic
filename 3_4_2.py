from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1():  # Браузер открывается, прогоняет все тесты, закрывается.
    # Данный способ быстрее, но данные и кэш оставшиеся после предудущего теста,
    # могут влиять на результаты выполнения следующего теста,
    # поэтому лучше всего запускать отдельный браузер для каждого теста,
    # как во втором способе, чтобы тесты были стабильнее

    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite 1 ..")
        self.browser = webdriver.Chrome('C:\\tools\\chromedriver2\\chromedriver.exe')

    @classmethod
    def teardown_class(self):
        print("quit browser for test suite 1 ..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print('start test link 1')
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print('start test basket 1')
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")


class TestMainPage2():

    def setup_method(self):
        print("start browser for test 2..")
        self.browser = webdriver.Chrome('C:\\tools\\chromedriver2\\chromedriver.exe')

    def teardown_method(self):
        print("quit browser for test 2..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print('start test link 2')
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print('start test basket 2')
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")

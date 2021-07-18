from selenium import webdriver
import time
import unittest

class TestReg1(unittest.TestCase):
    # 1
    def test_reg_1(self):

        link = "http://suninjuly.github.io/registration1.html"
        path = 'C:\\tools\\chromedriver2\\chromedriver.exe'
        browser = webdriver.Chrome(path)
        browser.get(link)

        first_name = browser.find_element_by_class_name('first')
        first_name.send_keys('Sergio')

        last_name = browser.find_element_by_class_name('second')
        last_name.send_keys('Garibzyani')

        email = browser.find_element_by_class_name('third')
        email.send_keys('sergio-g@mail.com')

        # Отправляем заполненную форму
        submit = browser.find_element_by_xpath('//button[@type="submit"]')
        submit.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(3)
        # закрываем браузер после всех манипуляций
        browser.quit()

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Should be successful registration")

    # 2
    def test_reg_2(self):

        link = "http://suninjuly.github.io/registration2.html"
        path = 'C:\\tools\\chromedriver2\\chromedriver.exe'
        browser = webdriver.Chrome(path)
        browser.get(link)

        first_name = browser.find_element_by_xpath("//form/div[1]/div[1]/input")
        first_name.send_keys('Sergio')

        last_name = browser.find_element_by_xpath("//form/div[1]/div[2]/input")
        last_name.send_keys('Garibzyani')

        email = browser.find_element_by_xpath("//form/div[1]/div[3]/input")
        email.send_keys('sergio-g@mail.com')

        time.sleep(10)

        # Отправляем заполненную форму
        submit = browser.find_element_by_xpath('//button[@type="submit"]')
        submit.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(3)
        # закрываем браузер после всех манипуляций
        browser.quit()

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Should be successful registration")

if __name__ == '__main__':
    unittest.main()

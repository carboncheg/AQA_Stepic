# from selenium import webdriver
#
# browser = webdriver.Chrome('C:\\tools\\chromedriver2\\chromedriver.exe')
# browser.get("http://suninjuly.github.io/simple_form_find_task.html")
# button = browser.find_element_by_id("submit_button")

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome('C:\\tools\\chromedriver2\\chromedriver.exe')
# browser.get("http://suninjuly.github.io/simple_form_find_task.html")
# button = browser.find_element(By.ID, "submit_button")

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
# browser = webdriver.Chrome('C:\\tools\\chromedriver2\\chromedriver.exe')
# browser.get(link)
# button = browser.find_element(By.ID, "submit_button")
# time.sleep(2)
# button.click()
#
# time.sleep(5)
# # закрываем браузер после всех манипуляций
# browser.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# path = 'C:\\tools\\chromedriver2\\chromedriver.exe'
# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     browser = webdriver.Chrome(path)
#     browser.get(link)
#     button = browser.find_element(By.ID, "submit_button")
#     time.sleep(2)
#     button.click()
#     time.sleep(4)
#
# finally:
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# Задание №1

# from selenium import webdriver
# import time
#
# path = 'C:\\tools\\chromedriver2\\chromedriver.exe'
# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     browser = webdriver.Chrome(path)
#     browser.get(link)
#
#     input1 = browser.find_element_by_tag_name('input')
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name('last_name')
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name('city')
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id('country')
#     input4.send_keys("Russia")
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# Задание №2

# from selenium import webdriver
# import math
# import time
#
# path = 'C:\\tools\\chromedriver2\\chromedriver.exe'
# link = "http://suninjuly.github.io/find_link_text"
# link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
#
# try:
#     browser = webdriver.Chrome(path)
#     browser.get(link)
#
#     link2 = browser.find_element_by_link_text(link_text)
#     link2.click()
#
#     input1 = browser.find_element_by_tag_name('input')
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name('last_name')
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name('city')
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id('country')
#     input4.send_keys("Russia")
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# Задание №3

# from selenium import webdriver
# import time
#
# path = 'C:\\tools\\chromedriver2\\chromedriver.exe'
#
# try:
#     browser = webdriver.Chrome(path)
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements_by_css_selector('input')
#     for element in elements:
#         element.send_keys("Мой ответ")
#
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# не забываем оставить пустую строку в конце файла


# Задание №4

# from selenium import webdriver
# import math
# import time
#
# path = 'C:\\tools\\chromedriver2\\chromedriver.exe'
# link = "http://suninjuly.github.io/find_xpath_form"
#
# try:
#     browser = webdriver.Chrome(path)
#     browser.get(link)
#
#     input1 = browser.find_element_by_tag_name('input')
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name('last_name')
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name('city')
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id('country')
#     input4.send_keys("Russia")
#     button = browser.find_element_by_xpath('//button[@type="submit"]')
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# Задание №5

# from selenium import webdriver
# import time
#
# try:
#     link = "http://suninjuly.github.io/registration1.html"
#     path = 'C:\\tools\\chromedriver2\\chromedriver.exe'
#     browser = webdriver.Chrome(path)
#     browser.get(link)
#
#     first_name = browser.find_element_by_class_name('first')
#     first_name.send_keys('Sergio')
#
#     last_name = browser.find_element_by_class_name('second')
#     last_name.send_keys('Garibzyani')
#
#     email = browser.find_element_by_class_name('third')
#     email.send_keys('sergio-g@mail.com')
#
#     # Отправляем заполненную форму
#     submit = browser.find_element_by_xpath('//button[@type="submit"]')
#     submit.click()
#
#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(1)
#
#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element_by_tag_name("h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text
#
#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(3)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# Задание №6

from selenium import webdriver
import time

try:
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

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

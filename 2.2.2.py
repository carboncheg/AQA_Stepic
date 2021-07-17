# from selenium import webdriver
# import time
#
# try:
#     link = 'http://suninjuly.github.io/selects1.html'
#     path = 'C:\\tools\\chromedriver2\\chromedriver.exe'
#     browser = webdriver.Chrome(path)
#     browser.get(link)
#     time.sleep(2)
#     browser.find_element_by_tag_name("select").click()
#     time.sleep(2)
#     # Если нужно выбрать второй элемент поп-апа
#     browser.find_element_by_css_selector("option:nth-child(2)").click()
#     time.sleep(2)
#     # Если нужно выбрать элемент с конкретным значением, в данном случае 1.
#     browser.find_element_by_css_selector("[value='1']").click()
#
# finally:
#     time.sleep(3)
#     browser.quit()


# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# import time
#
# try:
#     link = 'http://suninjuly.github.io/selects1.html'
#     path = 'C:\\tools\\chromedriver2\\chromedriver.exe'
#     browser = webdriver.Chrome(path)
#     browser.get(link)
#     time.sleep(1)
#     select = Select(browser.find_element_by_id("dropdown"))
#     select.select_by_value("1")  # выбор по конкретному значению, в данном случае 1
#     # select.select_by_index(1)  # выбор по индексу
#     # select.select_by_visible_text("45")  # поиск по видимому тексту
#
# finally:
#     time.sleep(4)
#     browser.quit()


# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# import time
#
# try:
#     link = 'http://suninjuly.github.io/selects2.html'
#     path = 'C:\\tools\\chromedriver2\\chromedriver.exe'
#     browser = webdriver.Chrome(path)
#     browser.get(link)
#     num1 = browser.find_element_by_id('num1').text
#     num2 = browser.find_element_by_id('num2').text
#     x = int(num1) + int(num2)
#     select = Select(browser.find_element_by_id('dropdown'))
#     select.select_by_value(str(x))
#     browser.find_element_by_css_selector('[type="submit"]').click()
# finally:
#     time.sleep(10)
#     browser.quit()



# from selenium import webdriver
# import time
#
# try:
#     link = 'http://suninjuly.github.io/selects2.html'
#     path = 'C:\\tools\\chromedriver2\\chromedriver.exe'
#     browser = webdriver.Chrome(path)
#     browser.get(link)
#     time.sleep(3)
#     # Можно выполнить скрипты по отдельности
#     # browser.execute_script("document.title='Script executing';")
#     # time.sleep(3)
#     # browser.execute_script("alert('Robots at work');")
#     # А можно вместе, перечислив их через ;
#     browser.execute_script("document.title='Script executing';alert('Robots at work');")
# finally:
#     time.sleep(3)
#     browser.quit()


# from selenium import webdriver
# import time
#
# browser = webdriver.Chrome('C:\\tools\\chromedriver2\\chromedriver.exe')
# link = "https://SunInJuly.github.io/execute_script.html"
# browser.get(link)
# print('Page loaded')
# time.sleep(2)
# button = browser.find_element_by_tag_name("button")
# print('Button found')
# time.sleep(2)
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# print('Page scrolled')
# time.sleep(2)
# button.click()
# print('Button clicked')
# time.sleep(2)


# from selenium import webdriver
# import math
# import time
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# try:
#     path = 'C:\\tools\\chromedriver2\\chromedriver.exe'
#     link = "https://SunInJuly.github.io/execute_script.html"
#     browser = webdriver.Chrome(path)
#
#     browser.get(link)
#     print('Page loaded')
#
#     x_element = browser.find_element_by_id('input_value').text
#     print('Value read')
#
#     x = x_element
#     y = calc(x)
#     print('Function calculated')
#
#     browser.execute_script("window.scrollBy(0, 100);")
#     print('Page scrolled')
#
#     # button = browser.find_element_by_tag_name("button")
#     # print('Button found')
#     # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#     # print('Scrolled to the button')
#
#     input_field = browser.find_element_by_id('answer')
#     input_field.send_keys(y)
#     print('Answer entered')
#
#     checkbox = browser.find_element_by_id('robotCheckbox')
#     checkbox.click()
#     print('Checkbox checked')
#
#     radiobutton = browser.find_element_by_id('robotsRule')
#     radiobutton.click()
#     print('Radiobutton switched')
#
#     button = browser.find_element_by_css_selector('[type="submit"]')
#     button.click()
#     print('Button clicked')
#
# finally:
#     time.sleep(15)
#     browser.quit()


from selenium import webdriver
import time
import os

try:
    path = 'C:\\tools\\chromedriver2\\chromedriver.exe'
    url = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome(path)

    browser.get(url)

    first_name = browser.find_element_by_css_selector('[name="firstname"]')
    first_name.send_keys('Sergio')
    last_name = browser.find_element_by_css_selector('[name="lastname"]')
    last_name.send_keys('Garibzyani')
    email = browser.find_element_by_css_selector('[name="email"]')
    email.send_keys('sergio-g@mail.com')

    # current_dir = os.path.abspath(os.path.dirname(__file__))  # файл для добавления на страницу лежит там же где и текущий исполняемый файл
    # print(os.path.abspath(os.path.dirname(__file__)))  # абсолютный путь до директории с добавляемым файлом
    # print(os.path.abspath(__file__))  # абсолютный путь до файла
    # print(os.path.dirname(__file__))  # абсолютный путь до директории с данным файлом
    # file_path = os.path.join(current_dir, 'file.txt')
    current_dir = os.path.abspath(os.path.dirname('D:\\Coding\\QA\\'))
    file_path = os.path.join(current_dir, 'pic.bmp')
    file_add_btn = browser.find_element_by_id('file')
    file_add_btn.send_keys(file_path)

    submit_btn = browser.find_element_by_css_selector('[type="submit"]')
    submit_btn.click()

finally:
    time.sleep(15)
    browser.quit()

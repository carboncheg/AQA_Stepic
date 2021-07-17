# from selenium import webdriver
# import math
# import time
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# try:
#     url = 'http://suninjuly.github.io/math.html'
#     path = 'C:\\tools\\chromedriver2\\chromedriver.exe'
#     driver = webdriver.Chrome(path)
#
#     driver.get(url)  #1
#     x_element = driver.find_element_by_id('input_value')
#     x = x_element.text  #2
#     y = calc(x)  #3
#     input_field = driver.find_element_by_id('answer')
#     input_field.send_keys(y)  #4
#     # checkbox = driver.find_element_by_css_selector('[for="robotCheckbox"]')  #5
#     # checkbox = driver.find_element_by_xpath('//label[@for="robotCheckbox"]')
#     checkbox = driver.find_element_by_id('robotCheckbox')
#     checkbox.click()
#     radiobutton = driver.find_element_by_css_selector('[for="robotsRule"]')  #6
#     radiobutton.click()
#     # radiobutton = driver.find_elements_by_id('robotsRule')
#     button = driver.find_element_by_css_selector('[type="submit"]')
#     button.click()  #7
#
# finally:
#     time.sleep(15)
#     driver.quit()


#
# from selenium import webdriver
# import time
#
# try:
#     path = "C:\\tools\\chromedriver2\\chromedriver.exe"
#     url = "http://suninjuly.github.io/math.html"
#     browser = webdriver.Chrome(path)
#
#     browser.get(url)
#
#     robot_checkbox = browser.find_element_by_id("robotCheckbox")
#     checkbox_required = robot_checkbox.get_attribute("required")
#     print(checkbox_required)
#     print("value of checkbox required: ", checkbox_required)
#     assert checkbox_required is not None
#
    # input_value = browser.find_element_by_id('input_value')  # проверка, что вернет метод .get_attribute
    # value = input_value.get_attribute('class')
    # print(value)

#     checkbox_checked = robot_checkbox.get_attribute('checked')
#     print(checkbox_checked)
#     print("value of checkbox checked: ", checkbox_checked)
#     assert checkbox_checked is None
#
#     people_radio = browser.find_element_by_id("peopleRule")
#     people_checked = people_radio.get_attribute("checked")
#     print("value of people radio: ", people_checked)
#     assert people_checked is not None, "People radio is not selected by default"
#
#     robots_radio = browser.find_element_by_id("robotsRule")
#     robots_checked = robots_radio.get_attribute("checked")
#     print("value of robots radio: ", robots_checked)
#     assert robots_checked is None
#
#     submit_button = browser.find_element_by_tag_name("button")
#     # submit_button = browser.find_element_by_class_name("btn")
#     btn_disabled = submit_button.get_attribute("disabled")
#     print("value of submit button: ", btn_disabled)
#     assert btn_disabled is None
#     time.sleep(10)
#
#     submit_button = browser.find_element_by_css_selector("[type='submit']")
#     btn_disabled = submit_button.get_attribute("disabled")
#     print("value of submit button after 10 sec: ", btn_disabled)
#     assert btn_disabled is not None
#
# finally:
#     time.sleep(2)
#     browser.quit()


from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    url = 'http://suninjuly.github.io/get_attribute.html'
    path = 'C:\\tools\\chromedriver2\\chromedriver.exe'
    driver = webdriver.Chrome(path)

    driver.get(url)  #1
    x_element = driver.find_element_by_id('treasure')  #2
    x = x_element.get_attribute('valuex')  #3
    y = calc(x)  #4
    input_field = driver.find_element_by_id('answer')
    input_field.send_keys(y)  #5
    checkbox = driver.find_element_by_id('robotCheckbox')
    checkbox.click()  #6
    radiobutton = driver.find_element_by_id('robotsRule')
    radiobutton.click()  #7
    button = driver.find_element_by_css_selector('[type="submit"]')
    button.click()  #8

finally:
    time.sleep(15)
    driver.quit()

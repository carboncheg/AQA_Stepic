# from selenium import webdriver
# import time
#
# path = 'C:\\tools\\chromedriver2\\chromedriver.exe'
# link = 'https://duckduckgo.com/'
#
# try:
#     browser = webdriver.Chrome(path)
#
#     browser.get(link)
#     print('Page loaded')
#     time.sleep(2)
#
#     browser.execute_script('alert("Hi! I\'m alert!")')
#     print('Alert shown')
#     time.sleep(2)
#
#     alert = browser.switch_to.alert
#     alert_text = alert.text
#     print(alert_text)
#     time.sleep(2)
#
#     alert.accept()
#     print('Alert accepted')
#     time.sleep(2)
#
#     browser.execute_script('confirm("Hi! I\'m confirm")')
#     print('Confirm shown')
#     time.sleep(2)
#
#     confirm = browser.switch_to.alert
#     confirm_text = confirm.text
#     print(confirm_text)
#     time.sleep(2)
#
#     confirm.accept()
#     print('Confirm accepted')
#     time.sleep(2)
#
#     browser.execute_script('confirm("Hi! I\'m confirm too")')
#     print('Confirm shown again')
#     time.sleep(2)
#
#     confirm = browser.switch_to.alert
#     confirm_text = confirm.text
#     print(confirm_text)
#     time.sleep(2)
#
#     confirm.dismiss()
#     print('Confirm dismissed')
#     time.sleep(2)
#
#     browser.execute_script('prompt("Hi! I\'m dismiss prompt")')
#     print('Dismiss prompt shown')
#     time.sleep(2)
#
#     prompt = browser.switch_to.alert
#     prompt.send_keys('o;etihji,jyp58$#**y61j7')
#     print('Abracadabra entered')
#     time.sleep(2)
#
#     prompt.dismiss()
#     print('Prompt dismissed')
#     time.sleep(2)
#
#     browser.execute_script('prompt("Hi! I\'m OK prompt")')
#     print('OK prompt shown')
#     time.sleep(2)
#
#     prompt = browser.switch_to.alert
#     prompt.send_keys('I like AQA')
#     print('Assertion entered')
#     time.sleep(2)
#
#     prompt.accept()
#     print('Prompt accepted')
#
# finally:
#     time.sleep(5)
#     browser.quit()



# from selenium import webdriver
# import math
# import time
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# try:
#     path = 'C:\\tools\\chromedriver2\\chromedriver.exe'
#     link = "http://suninjuly.github.io/alert_accept.html"
#     browser = webdriver.Chrome(path)
#
#     browser.get(link)
#
#     first_btn = browser.find_element_by_css_selector('[type="submit"]')
#     first_btn.click()
#
#     confirm = browser.switch_to.alert
#     confirm.accept()
#
#     x_element = browser.find_element_by_id('input_value').text
#     x = x_element
#     y = calc(x)
#
#     input_field = browser.find_element_by_id('answer')
#     input_field.send_keys(y)
#
#     button = browser.find_element_by_css_selector('[type="submit"]')
#     button.click()
#
# finally:
#     time.sleep(15)
#     browser.quit()


from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    path = 'C:\\tools\\chromedriver2\\chromedriver.exe'
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome(path)

    browser.get(link)

    first_btn = browser.find_element_by_css_selector('[type="submit"]')
    first_btn.click()

    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)

    x_element = browser.find_element_by_id('input_value').text
    x = x_element
    y = calc(x)

    input_field = browser.find_element_by_id('answer')
    input_field.send_keys(y)

    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()

finally:
    time.sleep(15)
    browser.quit()

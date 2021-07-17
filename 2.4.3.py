from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    path = 'C:\\tools\\chromedriver2\\chromedriver.exe'
    url = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome(path)
    browser.implicitly_wait(5)

    browser.get(url)

    price = WDW(browser, 12).until(  # указываем явное ожидание в 12 сек
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')  # до тех пор пока текст в элементе, который мы находим (By.ID, "price"), не будет равен $100
    )
    button = browser.find_element(By.ID, 'book')
    button.click()

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

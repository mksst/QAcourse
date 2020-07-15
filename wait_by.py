from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element_by_id("book")
    button.click()

    x_value = browser.find_element_by_id("input_value")
    x_text = x_value.text
    x = calc(x_text)

    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(x)
finally:
    submit = browser.find_element_by_id("solve")
    submit.click()

    time.sleep(5)
    browser.quit()



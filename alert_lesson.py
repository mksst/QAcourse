from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math



def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    submit = browser.find_element_by_css_selector(".btn")
    submit.click()
    confirm = browser.switch_to.alert
    confirm.accept()


    x_value = browser.find_element_by_id("input_value")
    x_text = x_value.text
    x = calc(x_text)

    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(x)


finally:
    submit = browser.find_element_by_css_selector(".btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()

    time.sleep(5)
    browser.quit()
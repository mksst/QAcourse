from selenium import webdriver
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    butt = browser.find_element_by_css_selector(".btn")
    butt.click()


    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)

    x_value = browser.find_element_by_id("input_value")
    x_text = x_value.text
    x = calc(x_text)

    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(x)
finally:
    submit = browser.find_element_by_css_selector(".btn")
    submit.click()

    time.sleep(5)
    browser.quit()
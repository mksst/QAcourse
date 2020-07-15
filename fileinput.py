from selenium import webdriver
import time, os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "file.txt")

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element_by_css_selector("[name = 'firstname'")
    name.send_keys("ko")
    scndname = browser.find_element_by_css_selector("[name = 'lastname']")
    scndname.send_keys("st")
    email = browser.find_element_by_css_selector("[name = 'email']")
    email.send_keys("a")

    file_input = browser.find_element_by_id("file")
    file_input.send_keys(file_path)

finally:

    submit = browser.find_element_by_css_selector(".btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()
    time.sleep(10)
    browser.quit()



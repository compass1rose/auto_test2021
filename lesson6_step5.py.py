import math
from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_link_text"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    pas = str(math.ceil(math.pow(math.pi, math.e)*10000))
    button = browser.find_element_by_link_text(pas)
    button.click()

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Nadia")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Panasiuk")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Vinnytsia")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Ukraine")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
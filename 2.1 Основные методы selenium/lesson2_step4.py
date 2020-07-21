from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Firefox()
browser.get(link)

x_e = browser.find_element_by_id('input_value')
x = x_e.text
y = calc(x)

input1 = browser.find_element_by_id('answer')
input1.send_keys(y)

ch = browser.find_element_by_id('robotCheckbox')
ch.click()

rad = browser.find_element_by_id('robotsRule')
rad.click()

but = browser.find_element_by_tag_name('button')
but.click()
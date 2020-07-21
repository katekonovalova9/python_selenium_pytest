from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Firefox()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

i = browser.find_element_by_tag_name('img')
im = i.get_attribute('valuex')

inp = browser.find_element_by_id('answer')
inp.send_keys(calc(im))

ch = browser.find_element_by_id('robotCheckbox')
ch.click()

rad = browser.find_element_by_id('robotsRule')
rad.click()

but = browser.find_element_by_tag_name('button')
but.click()

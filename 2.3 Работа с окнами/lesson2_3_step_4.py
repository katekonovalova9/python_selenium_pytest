from selenium import webdriver
import math
import time

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Firefox()
browser.get(link)

browser.find_element_by_tag_name('button').click()

confirm = browser.switch_to.alert
confirm.accept()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

time.sleep(2)
n = browser.find_element_by_id('input_value')
num = n.text
res = calc(num)
browser.find_element_by_tag_name('input').send_keys(res)
browser.find_element_by_tag_name('button').click()
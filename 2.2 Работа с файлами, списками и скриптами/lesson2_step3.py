from selenium import webdriver
import math

link = 'http://SunInJuly.github.io/execute_script.html'
browser = webdriver.Firefox()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


n = browser.find_element_by_id('input_value')
num = n.text

f = calc(num)

browser.find_element_by_id('answer').send_keys(f)
browser.find_element_by_id('robotCheckbox').click()
browser.execute_script("window.scrollBy(0,100);")
browser.find_element_by_id('robotsRule').click()
browser.find_element_by_tag_name('button').click()
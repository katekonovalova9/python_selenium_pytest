from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math
from selenium.webdriver.common.by import By


link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Firefox()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

num = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"100"))
browser.find_element_by_id('book').click()

browser.execute_script("window.scrollBy(0, 100);")
n = browser.find_element_by_id('input_value')
num = n.text
res = calc(num)
browser.find_element_by_tag_name('input').send_keys(res)
browser.find_element_by_id('solve').click()
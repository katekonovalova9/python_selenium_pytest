from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Firefox()
browser.get(link)

num1 = browser.find_element_by_id('num1')
num11 = num1.text

num2 = browser.find_element_by_id('num2')
num22 = num2.text

summ = int(num11) + int(num22)
print(summ)
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(summ))
browser.find_element_by_tag_name('button').click()
from selenium import webdriver
import os

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Firefox()
browser.get(link)

browser.find_element_by_name('firstname').send_keys('kate')
browser.find_element_by_name('lastname').send_keys('konovalova')
browser.find_element_by_name('email').send_keys('@mail.ru')

current_dir = os.path.abspath(os.path.dirname(__file__)) 
file_path = os.path.join(current_dir, 'file.txt')
browser.find_element_by_name('file').send_keys(file_path)
browser.find_element_by_tag_name('button').click()

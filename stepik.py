from selenium import webdriver
import sys
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

name = browser.find_element_by_class_name('first')
atr1 = name.get_attribute('required')
if atr1 == 'true':
    name.send_keys('Name')
else:
    browser.quit()
    sys.exit('Bug with "NAME"')

secondname = browser.find_element_by_class_name('second')
atr2 = secondname.get_attribute('required')
if atr2 == 'true':
    secondname.send_keys('Second name')
else:
    browser.quit()
    sys.exit('Bug with "Second Name"')
email = browser.find_element_by_class_name('third')
atr3 = email.get_attribute('required')
if atr3 == 'true':
    email.send_keys('email@ema.il')
else:
    browser.quit()
    sys.exit('Bug with "Email"')
button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(2)
welcome_text_elt = browser.find_element_by_tag_name("h1").text
print(welcome_text_elt)
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text_elt
browser.quit()
print('OK')
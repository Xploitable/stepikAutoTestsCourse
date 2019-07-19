from selenium import webdriver
import time
import math

# дефайним функцию для поиска значения
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# main script 
browser = webdriver.Chrome()
link = "https://suninjuly.github.io/alert_accept.html"
browser.get(link)

buttonFirst = browser.find_element_by_class_name("btn-primary")
buttonFirst.click()
time.sleep(5)

confirm = browser.switch_to.alert
confirm.accept()

inputValue = browser.find_element_by_xpath("//span[@id='input_value']")
x = inputValue.text
y = calc(x)

forResult = browser.find_element_by_xpath("//input[@id='answer']")
forResult.send_keys(y)

button = browser.find_element_by_css_selector("button.btn")
button.click()
assert True

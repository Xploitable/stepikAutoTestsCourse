from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

# дефайним функцию для поиска значения
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
booking = browser.find_element_by_id("book")
browser.execute_script("return arguments[0].scrollIntoView(true);", booking)
bookingText = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR"))
if bookingText:
    booking.click()

button = browser.find_element_by_id("solve")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

inputValue = browser.find_element_by_xpath("//span[@id='input_value']")
x = inputValue.text
y = calc(x)

forResult = browser.find_element_by_xpath("//input[@id='answer']")
forResult.send_keys(y)

button.click()
##assert "успешно" in message.text

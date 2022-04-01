from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    x_element = browser.find_element(By.ID,"input_value")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.ID,"answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(y)

    checkbox=browser.find_element(By.ID,'robotCheckbox')
    checkbox.click()

    radiobutton1=browser.find_element(By.ID,'peopleRule')
    radiobutton1=radiobutton1.get_attribute("checked")

    radiobutton2=browser.find_element(By.ID,'robotsRule')
    radiobutton2.click()

    button = browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
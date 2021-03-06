from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID,'treasure')
    x = x_element.get_attribute('valuex') #взяли у атрибута valuex его значение и присвоили значение x
    y = calc(x)

    answer=browser.find_element(By.ID,'answer')
    answer.send_keys(y)

    checkbox=browser.find_element(By.ID,'robotCheckbox')
    checkbox.click()

    radiobutton1=browser.find_element(By.ID,'peopleRule')
    radiobutton1=radiobutton1.get_attribute("checked")

    radiobutton2=browser.find_element(By.ID,'robotsRule')
    radiobutton2.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
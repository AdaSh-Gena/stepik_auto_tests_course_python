from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID,'num1')
    num1=num1.text #достать из текста число 1 строкой
    num2 = browser.find_element(By.ID,'num2')
    num2=num2.text #достать из текста число 2 строкой
    sum=str(int(num1)+int(num2)) #в сумму записать строку, состоящую из суммы двух чисел, переведенных в число из строки

    dropdowm=Select(browser.find_element(By.ID,"dropdown"))
    dropdowm.select_by_value(sum) 

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    linkTosmth = browser.find_element_by_partial_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    linkTosmth.click()

    input1 = browser.find_element(By.NAME,"first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME,"last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME,"city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR,"button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
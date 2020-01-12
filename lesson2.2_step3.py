
from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
    x1 = browser.find_element_by_id('num1')
    x = x1.text
    print(x)
    x2 = browser.find_element_by_id('num2')
    y = x2.text
    print(y)
        
    x = int(x)
    y = int(y)
        
    
    def calc(x, y):
            return x+y
    
    y = calc(x, y)
    print(y)
    y = str(y)
    
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(y) # ищем элемент с текстом "Python"

        # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
    time.sleep(1)

        
    
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

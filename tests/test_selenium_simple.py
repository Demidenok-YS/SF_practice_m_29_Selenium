import time

from selenium.webdriver.common.by import By

# python3 -m pytest -v --driver Chrome --driver-path /Users/demidenokys/chromedriver-mac-arm64/chromedriver tests/test_selenium_simple.py



def test_searh_example(selenium):

    #Открыть страницу https://google.com в браузере
    selenium.get("https://google.com")
    #задержка 5 сек
    time.sleep(5)

    #Находим поле для ввода текста
    #Создаем переменную search_input  и присваиваем ей путь элемента по его ID
    search_input = selenium.find_element(By.ID, "APjFqb")

    #полностью очищаем текстовое поле, на всякий случай
    search_input.clear()
    #указываем текст (my first selenium test for WEB UI), который нужно ввести в текстовое поле
    search_input.send_keys("my first selenium test for WEB UI")
    time.sleep(5)

    #Создаем переменную search_button и присваиваем ей путь элемента по его Name
    search_button = selenium.find_element(By.NAME, "btnK")
    #Кликаем ЛКМ
    search_button.submit()
    time.sleep(10)

    #Сделать скриншот и сохранить в файл result.png
    #selenium.get_screenshot_as_file('result.png')
    selenium.save_screenshot('result.png')





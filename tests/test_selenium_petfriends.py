import time

from selenium.webdriver.common.by import By
#запуск всех тестов
# python3 -m pytest -v --driver Chrome --driver-path /Users/demidenokys/chromedriver-mac-arm64/chromedriver tests/test_selenium_petfriends.py
#запуск конкретного теста
# python3 -m pytest -v --driver Chrome --driver-path /Users/demidenokys/chromedriver-mac-arm64/chromedriver tests/test_selenium_petfriends.py::test_show_all_pets
def test_petfriends(web_browser):
    #Открыть страницу https://petfriends.skillfactory.ru/
    web_browser.get("https://petfriends.skillfactory.ru/")
    time.sleep(5)

    #Находим кнопку Зарегистрироваться
    btn_newuser = web_browser.find_element(By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]")
    #Кликаем ЛКМ
    btn_newuser.click()
    time.sleep(5)

    #Находим ссылку с текстом "У меня уже есть аккаунт"
    btn_exist_acc = web_browser.find_element(By.LINK_TEXT, u"У меня уже есть аккаунт")
    #Кликаем ЛКМ
    btn_exist_acc.click()
    time.sleep(5)

    #Добавляем почту
    field_email = web_browser.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys("yan32615854@yandex.ru")
    time.sleep(5)

    #Добавляем пароль
    field_pass = web_browser.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys("123456")
    time.sleep(5)

    #Находим кнопку Войти
    btn_submit = web_browser.find_element(By.XPATH, "//button[@type='submit']")
    #Кликаем ЛКМ
    btn_submit.click()


    time.sleep(10)
    # #Если текущий URL совпадает с https://petfriends.skillfactory.ru/all_pets
    # if web_browser.current_url == 'https://petfriends.skillfactory.ru/all_pets':
    #     #Делаем скриншот
    #     web_browser.save_screenshot('results_petfriends.png')
    # #иначе ошибка логина
    # else:
    #     raise Exception("login error")

    assert web_browser.current_url == 'https://petfriends.skillfactory.ru/all_pets', "login error"

# Проверка всех питомцев пользователя на наличие фото, имени, вида и возраста
def test_show_all_pets(driver):
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('yan32615854@yandex.ru')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('123456')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()

    images = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0

# 1. Проверка присутствия всех питомцев пользователя
def test_presence_for_all_pets(driver):
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('yan32615854@yandex.ru')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('123456')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()

    pets_num = driver.find_element(By.XPATH, '//*[@class=".col-sm-4 left"]').text.split('\n')[1].split(': ')[1]
    pets_card = driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')
    assert int(pets_num) == len(pets_card)

# 2. Проверка того , что хотя бы у половины питомцев есть фото
def test_half_of_the_pets_with_photos(driver):
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('yan32615854@yandex.ru')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('123456')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()

    pets_num = driver.find_element(By.XPATH, '//*[@class=".col-sm-4 left"]').text.split('\n')[1].split(': ')[1]
    images = driver.find_elements(By.XPATH, '//img[starts-with(@src, "data:image")]')
    assert len(images) >= int(pets_num)/2

# 3. Проверка того, что у всех питомцев есть имя, возраст и порода.
def test_сheck_pets_for_name_age_breed(driver):
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('yan32615854@yandex.ru')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('123456')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()

    names = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    for i in range(len(names)):
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0

# 4. Проверка того, что у всех питомцев разные имена.
def test_different_names_pets(driver):
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('yan32615854@yandex.ru')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('123456')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
    names = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')

    name_my_pets = []
    for i in range(len(names)):
        name_my_pets.append(names[i].text)
    assert len(name_my_pets) == len(set(name_my_pets))

# 5. Проверка того, что в списке нет повторяющихся питомцев.
def test_no_duplicates_pets(driver):
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('yan32615854@yandex.ru')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('123456')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
    pets = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
    list_pets = []
    for i in range(len(pets)):
        list_data = pets[i].text.split("\n")
        list_pets.append(list_data[0])
    assert len(set(list_pets)) == len(pets)
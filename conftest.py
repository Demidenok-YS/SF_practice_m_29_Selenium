#content of file conftest.py

import pytest
import uuid
from selenium import webdriver


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # This function helps to detect that some test failed
    # and pass this information to teardown:

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture
def web_browser(request, selenium):

    browser = selenium
    browser.set_window_size(500, 1000)

    # Return browser instance to test case:
    yield browser

    # Этот код выполнится после отрабатывания теста:

    if request.node.rep_call.failed:

        try:
            # Сделать скриншот, если тест провалится:
            browser.execute_script("document.body.bgColor = 'black';")

            # Создаем папку screenshots(руками) и сохраняем туда скриншот с генерированным именем:
            browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')

            # Для дебагинга, печатаем информацию в консоль
            print('URL: ', browser.current_url)
            print('Browser logs:')
            for log in browser.get_log('browser'):
                print(log)

        except:
            pass # just ignore any errors here


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    # Переходим на страницу авторизации
    driver.get('https://petfriends.skillfactory.ru/login')

    yield driver

    driver.quit()
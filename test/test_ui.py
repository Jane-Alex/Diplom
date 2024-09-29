from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import allure 
import pytest
from time import sleep

@pytest.fixture 
def browser(): 
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 
    browser.maximize_window() 
    browser.implicitly_wait(10)
    yield browser 
    browser.quit()


#@allure.title("Поиск фильма по названию на кириллице") 
#@allure.description("Тест проверяет поиск фильма на кириллице") 
#@allure.severity("blocker")
def test_find_film(browser):
    browser.get("https://www.kinopoisk.ru/")
    with allure.step("Добавлены ожидания и открытие окна"): 
        browser.implicitly_wait(10)
        browser.maximize_window()
    with allure.step("Выполнение поиска фильма"): 
        browser.find_element(By.CSS_SELECTOR, "input[name=kp_query]").send_keys("экипаж")
        browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
    with allure.step("Проверяем результат по запросу"): 
        result = browser.find_element(By.CSS_SELECTOR, 'a[data-type="film"]').text
        assert result == "экипаж"
        #assert "" in browser.find_element(By.CSS_SELECTOR, 'p[class="name"]').text

        
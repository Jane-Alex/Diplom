from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import allure 
import pytest

@pytest.fixture 
def browser(): 
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 
    browser.maximize_window() 
    browser.implicitly_wait(10)
    yield browser 
    browser.quit()


@allure.title("Поиск фильма по названию на кириллице") 
@allure.description("Тест проверяет поиск фильма на кириллице")
@allure.id(1) 
@allure.severity("blocker")
def test_find_film_rus(browser):
    browser.get("https://www.kinopoisk.ru/")
    with allure.step("Добавлены ожидания и открытие окна"): 
        browser.implicitly_wait(10)
        browser.maximize_window()
    with allure.step("Выполнение поиска фильма"): 
        browser.find_element(By.CSS_SELECTOR, "input[name=kp_query]").send_keys("экипаж")
        browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
    with allure.step("Проверяем результат по запросу"): 
        result = browser.find_element(By.CSS_SELECTOR, 'a[data-type="film"]').text
        assert result, "экипаж"

@allure.title("Поиск фильма по названию на латинице") 
@allure.description("Тест проверяет поиск фильма на латинице")
@allure.id(2) 
@allure.severity("blocker")
def test_find_film_lat(browser):
    browser.get("https://www.kinopoisk.ru/")
    with allure.step("Добавлены ожидания и открытие окна"): 
        browser.implicitly_wait(10)
        browser.maximize_window()
    with allure.step("Выполнение поиска фильма"): 
        browser.find_element(By.CSS_SELECTOR, "input[name=kp_query]").send_keys("Titanic")
        browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
    with allure.step("Проверяем результат по запросу"): 
        result = browser.find_element(By.CSS_SELECTOR, 'span[class="gray"]').text
        assert result, "Titanic"

@allure.title("Поиск актера по имени") 
@allure.description("Тест проверяет поиск актера по имени")
@allure.id(3) 
@allure.severity("blocker")
def test_find_actor(browser):
    browser.get("https://www.kinopoisk.ru/")
    with allure.step("Добавлены ожидания и открытие окна"): 
        browser.implicitly_wait(10)
        browser.maximize_window()
    with allure.step("Выполнение поиска фильма"): 
        browser.find_element(By.CSS_SELECTOR, "input[name=kp_query]").send_keys("ДиКаприо")
        browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
    with allure.step("Проверяем результат по запросу"): 
        result = browser.find_element(By.CSS_SELECTOR, 'a[data-type="person"]').text
        assert result, "ДиКаприо"

@allure.title("Расширенный поиск фильмов по году")  
@allure.description("Тест проверяет поиск фильмов по году")
@allure.id(4) 
@allure.severity("blocker")
def test_find_film_by_id(browser):
    browser.get("https://www.kinopoisk.ru/")
    with allure.step("Добавлены ожидания и открытие окна"): 
        browser.implicitly_wait(10)
        browser.maximize_window()
    with allure.step("Открываем вкладку 'Расширенный поиск"): 
        browser.find_element(By.CSS_SELECTOR, 'a[aria-label="Расширенный поиск"]').click()
    with allure.step("Выполнение поиска фильма по году"):
        browser.find_element(By.CSS_SELECTOR, "#year").send_keys("2016")
        browser.find_element(By.CSS_SELECTOR, "input[type=button]").click()
    with allure.step("Проверяем результат по запросу"): 
        result = browser.find_element(By.CSS_SELECTOR, 'span[class="year"]').text
        assert result == "2016"
        
@allure.title("Поиск фильма по цифре") 
@allure.description("Тест проверяет поиск фильма при вводе цифры в поле поиска")
@allure.id(5) 
@allure.severity("blocker")
def test_find_film_figure(browser):
    browser.get("https://www.kinopoisk.ru/")
    with allure.step("Добавлены ожидания и открытие окна"): 
        browser.implicitly_wait(10)
        browser.maximize_window()
    with allure.step("Выполнение поиска фильма"): 
        browser.find_element(By.CSS_SELECTOR, "input[name=kp_query]").send_keys("7")
        browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
    with allure.step("Проверяем результат по запросу"): 
        result = browser.find_element(By.CSS_SELECTOR, 'a[data-type="film"]').text
        assert result, "7"
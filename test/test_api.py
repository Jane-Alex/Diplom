import requests
import allure

base_url = "https://api.kinopoisk.dev/v1.4"
key = "FFVW3FK-F6PMTZW-G52F6R6-179PNR9"

@allure.title("Поиск фильма по названию")
@allure.description("Выполнение теста на поиск фильма по его названию")
@allure.id(1)
@allure.severity("blocker")
def test_search_movie_by_title(): 
    headers = {
    "X-API-KEY" : key
    }
    with allure.step("Отправляем GET запрос с названием фильма"):
        response = requests.get(base_url+'/movie/search?page=1&limit=10&query=Экипаж', headers=headers)
        response_body = response.json()
        first_movie = response_body["docs"][0]['name']
    with allure.step("Проверяем статус ответа"):
        assert response.status_code == 200
    with allure.step("Проверяем нахождение запрашиваемого фильма по названию"):
        assert first_movie == "Экипаж"

@allure.title("Поиск фильма по id")
@allure.description("Выполнение теста на поиск фильма по его id")
@allure.id(2)
@allure.severity("blocker")
def test_search_movie_by_id():
    headers = {
    "X-API-KEY" : key
    }
    with allure.step("Отправляем GET запрос с указанием id фильма"):
        response = requests.get(base_url+'/movie/839818', headers=headers)
        response_body = response.json()
        id = response_body['id']
    with allure.step("Проверяем статус ответа"):
        assert response.status_code == 200
    with allure.step("Проверяем нахождение запрашиваемого фильма по id"):
        assert id == 839818

@allure.title("Поиск фильма по фильтру ")
@allure.description("Выполнение теста на поиск фильма по фильтру")
@allure.id(3)
@allure.severity("blocker")
def test_search_with_filters():
    headers = {
    "X-API-KEY" : key
    }
    with allure.step("Отправляем GET запрос с заполненными полями в фильтре"):
        response = requests.get(base_url+'/movie?page=1&limit=10&selectFields=names&type=movie&year=2016&genres.name=триллер&countries.name=Россия',
                                 headers=headers)
    with allure.step("Проверяем статус ответа"):
        assert response.status_code == 200

@allure.title("Поиск персоны по имени")
@allure.description("Выполнение теста на поиск персоны по имени")
@allure.id(4)
@allure.severity("blocker")
def test_search_person_by_name(): 
    headers = {
    "X-API-KEY" : key
    }
    with allure.step("Отправляем GET запрос с указанием имени персоны"):
        response = requests.get(base_url+'/person/search?page=1&limit=10&query=Данила Козловский', headers=headers)
        response_body = response.json()
        first_movie = response_body["docs"][0]['name']
    with allure.step("Проверяем статус ответа"):
        assert response.status_code == 200
    with allure.step("Проверяем нахождение запрашиваемой персоны по имени"):
        assert first_movie == "Данила Козловский"

@allure.title("Получение рандомного тайтла")
@allure.description("Выполнение теста на получение рандомного тайтла из базы")
@allure.id(5)
@allure.severity("blocker")
def test_get_random_title():
    headers = {
    "X-API-KEY" : key
    }
    with allure.step("Отправляем GET запрос на получение рандомного тайтла"):
        response = requests.get(base_url+'/movie/random?notNullFields=id&notNullFields=name', headers=headers)
    with allure.step("Проверяем статус ответа"):
        assert response.status_code == 200
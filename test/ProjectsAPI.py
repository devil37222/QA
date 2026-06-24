import requests
from config import API_KEY
import allure


class ProjectsAPI:

    # Инициализация
    def __init__(self, driver, url) -> None:
        """
        Конструктор класса ProjectsAPI.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.url = url

    @allure.step("Получение фильма по {id}")
    def get_film_byID(self, id):
        """
        Получение фильма по уникальному валидному id.

        :param id: int — Валидный идентификационный номер фильма.
        """
        my_headers = {
            "Content-Type": "application/json",
            'X-API-KEY': API_KEY
        }
        resp = requests.get(f'{self.url}/api/v2.2/films/{id}',
                            headers=my_headers)
        return resp

    @allure.step("Поиск фильма по ключевому слов {keyword"
                 "} и вывод результата в количестве страниц {page}")
    def search_film_byKeyword(self, keyword, page):
        """
        Поиск фильма по ключевому слову и вывод результата в страницах
        :param keyword: str — Ключевое слово в поиске,
        :param page: int — Количество страница в результате.
        """
        my_headers = {
            "Content-Type": "application/json",
            'X-API-KEY': API_KEY
        }
        resp = requests.get(f'{self.url
                               }/api/v2.1/films/search-by-keyword?keyword={
                                   keyword}&page={page}', headers=my_headers)
        return resp

    @allure.step("Получение информации о валидном ключе {apy_key}")
    def get_APIkey(self, apy_key):
        """
        Получение информации о валидном ключе
        :param apy_key: str — валидный ключ для авторизации
        """
        my_headers = {
            "Content-Type": "application/json",
            'X-API-KEY': API_KEY
        }
        resp = requests.get(
            f'{self.url}/api/v1/api_keys/{apy_key}', headers=my_headers)
        return resp

    @allure.step("Получение фильма с несуществующим {id}")
    def fakePost(self, id):
        """
        Получение фильма с несуществующим id.

        :param id: int — Невалидный идентификационный номер фильма.
        """
        my_headers = {
            "Content-Type": "application/json",
            'X-API-KEY': API_KEY
        }
        resp = requests.post(f'{self.url}/api/v2.2/films/{id}',
                             headers=my_headers)
        return resp

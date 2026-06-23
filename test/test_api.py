from ProjectsAPI import ProjectsAPI
from config import API_KEY
import allure

api = ProjectsAPI(None, "https://kinopoiskapiunofficial.tech")


@allure.title("Тестирование API запросов сайта 'КИНОПОИСК'")
@allure.description("Тесты проверяет корректность работы сайта "
                    "с различными операциями.")
@allure.feature("Позитивные API-запросы")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_film():
    """
    Получение фильма по уникальному валидному id.

    :param id: int — Валидный идентификационный номер фильма.
    """
    id = 435
    with allure.step(f"Поиск фильма по валидному {id}"):
        resp = api.get_film_byID(id)
    with allure.step("Проверка статус-кода"):
        assert resp.status_code == 200
    with allure.step("Вывод результата в формате json"):
        resp.json()


def test_search_film():
    """
    Поиск фильма по ключевому слову и вывод результата в страницах
    :param keyword: str — Ключевое слово в поиске,
    :param page: int — Количество страница в результате.
    """
    keyword = 'мстители'
    page = 1
    with allure.step(f"Поиск фильма по ключевому {keyword} "
                     " и вывод результата в {page} cтраницах(е)"):
        resp = api.search_film_byKeyword(keyword, page)
    with allure.step("Проверка статус-кода"):
        assert resp.status_code == 200
    with allure.step("Вывод результата в формате json"):
        resp.json()


def test_get_key():
    """
    Получение информации о валидном ключе
    :param apy_key: str — валидный ключ для авторизации
    """
    apy_key = API_KEY
    with allure.step(f"Получение информации о валидном {apy_key}"):
        resp = api.get_APIkey(apy_key)
    with allure.step("Проверка статус-кода"):
        assert resp.status_code == 200
    with allure.step("Вывод результата в формате json"):
        resp.json()


@allure.feature("Негативные API-запросы")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_film_byFakeID():
    """
    Получение фильма с несуществующим id.

    :param id: int — Невалидный идентификационный номер фильма.
    """
    id = 999999999
    with allure.step(f"Поиск фильма по невалидному {id}"):
        resp = api.get_film_byID(id)
    with allure.step("Проверка статус-кода"):
        assert resp.status_code == 400
    with allure.step("Вывод результата в формате json"):
        resp.json()


def test_fake_post():
    """
    Использование некорректного HTTP-метода при валидном id.

    :param id: int — Валидный идентификационный номер фильма.
    """
    id = 435
    with allure.step("Использование метода некорректного HTTP-метода(POST)"):
        resp = api.fakePost(id)
    with allure.step("Проверка статус-кода"):
        assert resp.status_code == 500
    with allure.step("Вывод результата в формате json"):
        resp.json()

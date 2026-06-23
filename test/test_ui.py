from selenium import webdriver
from KinopoiskPage import KinopoiskPage
import pytest
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации, открытия страницы и завершения работы драйвера.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://hd.kinopoisk.ru")
    yield driver
    driver.quit()


@allure.title("UI-Тестирование сайта hd.kinopoisk.ru")
@allure.description("Тесты проверяет "
                    "корректность работы сайта 'hd.kinopoisk.ru'.")
@allure.feature("КИНОПОИСК")
@allure.severity(allure.severity_level.CRITICAL)
def test_trailer(driver):
    """
    Тест проверяет функцию открытия трейлера фильма на полный экран.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    """
    page = KinopoiskPage(driver)
    with allure.step("Открытие страницы фильма"):
        page.open_film()
    with allure.step("Открытие трейлера фильма"):
        page.open_trailer()
    with allure.step("Открытие фильма в полноэкранном режиме"):
        page.open_maximize()


def test_shop(driver):
    """
    Тест проверяет функцию перехода
    на страницу “Магазин” и перехода на следующий фильм.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    """
    page = KinopoiskPage(driver)
    with allure.step("Открытие страницы магазина"):
        page.open_shop()
    with allure.step("Переход на следующий фильм"):
        page.scroll_film()


def test_favorite(driver):
    """
    Тест проверяет функцию добавления фильма в избранное.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    """
    page = KinopoiskPage(driver)
    with allure.step("Открытие страницы фильма"):
        page.open_film()
    with allure.step("Добавление фильма в избранное"):
        page.add_favourite()


def test_film(driver):
    """
    Тест проверяет функцию поиска фильма по ключевому слову.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    :param keyword: str — Ключевое слово в поиске
    """
    keyword = "Горничная"
    page = KinopoiskPage(driver)
    with allure.step("Поиск фильма по ключевому слову {keyword}"):
        page.search(keyword)
    with allure.step("Открытие страницы фильма"):
        page.page_film()


def test_channels(driver):
    """
    Тест проверяет функцию перехода
    на страницу “Каналы” и просмотр категорий каналов".

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    """
    page = KinopoiskPage(driver)
    with allure.step("Открытие страницы 'Каналы'"):
        page.open_channels()
    with allure.step("Переход к каналам раздела 'Федеральные'"):
        page.switch_federal()
    with allure.step("Переход к каналам раздела 'Спорт'"):
        page.switch_sport()
    with allure.step("Переход к каналам раздела 'Детские'"):
        page.switch_kids()

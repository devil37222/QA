from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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
@pytest.mark.ui
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
    with allure.step("Открытие трейлера в полноэкранном режиме"):
        page.open_maximize()
    with allure.step("Проверка трейлера на открытие в полноэкранном режиме"):
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            'button[aria-label="Выйти'
                                            ' из полноэкраного режима"]')))
        assert element is not None, "Элемент не найден на новой странице"


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
    with allure.step("Проверка перехода на следующий фильм"):
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, 'a[aria-label="Наследник"]')))
        assert element is not None, "Элемент не найден на новой странице"


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
    with allure.step("Проверка на добавление фильма в избранное"):
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, 'input[data-testid="text-field-input"]')))
        assert element is not None, "Элемент не найден на новой странице"


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
    with allure.step("Проверка на открытие страницы фильма"):
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, 'img[alt="Смотреть фильм Горничная, 2025"]')))
        assert element is not None, "Элемент не найден на новой странице"


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
    with allure.step("Проверка на то,что последним "
                     "разделом при переходе каналов является 'Детские'"):
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, 'div[aria-label="МУЛЬТ"]')))
        assert element is not None, "Элемент не найден на новой странице"

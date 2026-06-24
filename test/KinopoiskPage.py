from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class KinopoiskPage:

    def __init__(self, driver):
        """
        Конструктор класса KinopoiskPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.film = (By.CSS_SELECTOR, "[data-tid='TopSelectionCard']")
        self.trailer = (By.CSS_SELECTOR, 'button[name="Trailer"]')
        self.maximize = (By.CSS_SELECTOR, 'button['
                         'aria-label="Перейти в полноэкранный режим"]')
        self.shop = (By.CSS_SELECTOR, 'a[href="/buy"]')
        self.scroll = (By.CSS_SELECTOR, 'button['
                       'aria-label="Следующий слайд"]')
        self.button_favourite = (By.CSS_SELECTOR,
                                 'button[aria-label="Буду смотреть"]')
        self.search_button = (By.CSS_SELECTOR, 'svg['
                              'class="styles_icon__YXFtB'
                              ' SearchButton_search-icon__WqSQ7"]')
        self.input = (By.CSS_SELECTOR, 'input')
        self.result_film = (By.CSS_SELECTOR, 'a[id="suggest-item-0"]')
        self.img_film = (By.CSS_SELECTOR, 'img['
                         'alt="Смотреть фильм Горничная, 2025"]')
        self.channels = (By.CSS_SELECTOR, 'a[id="channels"]')
        self.watch_channels = (By.CSS_SELECTOR, 'h1[data-tid="Text"]')
        self.federal = (By.XPATH, "//button[text()='Федеральные']")
        self.first_channel = (By.CSS_SELECTOR, 'button[title="Первый канал"]')
        self.sport = (By.XPATH, "//button[text()='Спортивные']")
        self.match_tv = (By.CSS_SELECTOR, 'button[title="Матч ТВ"]')
        self.kids = (By.XPATH, "//button[text()='Детские']")
        self.mult = (By.CSS_SELECTOR, 'button[title="МУЛЬТ"]')

    @allure.step("Открытие страницы фильма")
    def open_film(self):
        """
        Открывает страницу фильма.
        """
        # Добавляем задержку для надежности
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.film))
        self.driver.find_element(*self.film).click()

    @allure.step("Открытие трейлера фильма")
    def open_trailer(self):
        """
        Открывает трейлер фильма.
        """
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.trailer))
        self.driver.find_element(*self.trailer).click()

    @allure.step("Открытие трейлера на полный экран")
    def open_maximize(self):
        """
        Открывает трейлер в полноэкранном режиме.
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.maximize))
        self.driver.find_element(*self.maximize).click()

    @allure.step("Открытие страницы магазина")
    def open_shop(self):
        """
        Открывает страницу со списком каналов.
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.shop))
        self.driver.find_element(*self.shop).click()

    @allure.step("Переход на следующий фильм")
    def scroll_film(self):
        """
        Переходит нажатием кнопки на следующий фильм.
        """
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.scroll))
        self.driver.find_element(*self.scroll).click()

    @allure.step("Добавляние фильма в избранное")
    def add_favourite(self):
        """
        Добавляет фильм в избранное.
        """
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.button_favourite))
        self.driver.find_element(*self.button_favourite).click()

    def is_favorite(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.favourite))

    @allure.step("Поиск фильма по ключевому слову {keyword}")
    def search(self, keyword):
        """
        Ищет фильм по ключевому слову.
        :param keyword: str — ключевое слово для поиска фильма.
        """
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.search_button))
        self.driver.find_element(*self.search_button).click()
        # Добавляем задержку до появления поля поиска
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.input))
        self.driver.find_element(*self.input).send_keys(keyword)

    @allure.step("Открытие страницы фильма в через поисковик")
    def page_film(self):
        """
        Открывает страницу фильма после ввода ключевого слова.
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.result_film))
        self.driver.find_element(*self.result_film).click()
        # Добавляем задержку до появления картинки с названием фильма
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.img_film))

    @allure.step("Открытие страницы со списком каналов")
    def open_channels(self):
        """
        Открывает страницу со списком каналов.
        """
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.channels))
        self.driver.find_element(*self.channels).click()
        # Добавляем задержку до появления картинки "Смотреть кнаналы"
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.watch_channels))

    @allure.step("Открытие страницу каналов с разделом 'Федеральные'")
    def switch_federal(self):
        """
        Открывает раздел федеральных каналов.
        """
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.federal))
        self.driver.find_element(*self.federal).click()
        # Добавляем задержку до появления канала с названием "Первый канал"
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.first_channel))

    @allure.step("Открытие страницу каналов с разделом 'Спорт'")
    def switch_sport(self):
        """
        Открывает раздел спортивных каналов.
        """
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.sport))
        self.driver.find_element(*self.sport).click()
        # Добавляем задержку до появления канала с названием "МАТЧ ТВ"
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.match_tv))

    @allure.step("Открытие страницу каналов с разделом 'Детские'")
    def switch_kids(self):
        """
        Открывает раздел детских каналов.
        """
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.kids))
        self.driver.find_element(*self.kids).click()
        # Добавляем задержку до появления канала с названием "МУЛЬТ"
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.mult))

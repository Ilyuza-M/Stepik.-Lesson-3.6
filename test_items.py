from selenium.webdriver.common.by import By
import time


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button_add_to_basket(browser):
    browser.get(link)
    button = browser.find_elements(By.CSS_SELECTOR, 'butt.btn-lg.btn-primary')
    assert button is not None, 'Add to basket button not found. (Кнопка Добавить в корзину не найдена)'

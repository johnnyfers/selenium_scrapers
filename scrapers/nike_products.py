import time
from selenium.webdriver import Chrome as drivertype
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs4
from utils.save_csv import save_csv
from utils.get_random_string import get_random_string


def nike_scraper(driver: drivertype):
    driver.get('https://www.nike.com/w/sale-3yaep')
    last_height = driver.execute_script("return document.body.scrollHeight")
    products = []

    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(2)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    html = driver.page_source
    soup = bs4(html, 'lxml')
    boxes = soup.find_all('div', {'class': 'product-card__body'})
    for box in boxes:
        try:
            product = {
                'title': box.find('div', {'class': 'product-card__title'}).text,
                'link': box.find('a', {'class': 'product-card__img-link-overlay'})['href'],
                'current_price': box.find('div', {'class': 'product-price is--current-price css-1ydfahe'}).text
            }
            products.append(product)
        except:
            pass

    number_of_characters = 15
    filename = get_random_string(number_of_characters) + '.csv'
    path = f'files/nike_{filename}'
    save_csv(path, products)

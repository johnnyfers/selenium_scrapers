from scrapers.nike_products import nike_scraper
from utils.get_driver import get_driver


def ask():
    return input('''welcome to web scraping plataform, please choose an option: \n
    1. Get all products for sale at nike.com \n
    0. exit \n
    ''')


if __name__ == '__main__':
    drive = get_driver()
    option = ask()
    while True:
        if option == '1':
            nike_scraper(drive)
        elif option == '0':
            print('bye')
            break
        else:
            print('invalid option')

        option = ask()

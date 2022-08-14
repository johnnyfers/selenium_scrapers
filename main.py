from scrapers.nike_products import nike_scraper
from scrapers.twitter_tweets import twitter_scraper
from utils.get_driver import get_driver


def ask():
    return input('''welcome to web scraping plataform, please choose an option: \n
    1. Get all products for sale from nike.com \n
    2. Get a certain number of tweets from someone in twitter.com \n
    0. exit \n
    ''')


if __name__ == '__main__':
    drive = get_driver()
    option = ask()
    while True:
        if option == '1':
            nike_scraper(drive)
        elif option == '2':
            twitter_scraper(drive)
        elif option == '0':
            print('bye')
            break
        else:
            print('invalid option')

        option = ask()

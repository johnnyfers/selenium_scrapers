import time
from selenium.webdriver import Chrome as drivertype
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs4
from utils.get_random_string import get_random_string
from utils.save_csv import save_csv
from selenium.webdriver.common.keys import Keys
from getpass import getpass


def login(driver: drivertype, username: str, password: str):
    # inputs an email and password for the login details
    time.sleep(5)
    username_form = driver.find_element(
        By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
    username_form.send_keys(username)
    username_form.send_keys(Keys.ENTER)

    time.sleep(5)
    password_form = driver.find_element(
        By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    password_form.send_keys(password)
    password_form.send_keys(Keys.ENTER)


def search_profile(driver, user):
    time.sleep(5)
    search_box = driver.find_element(
        By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')
    search_box.send_keys(user)
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)

    peaole_tag = driver.find_element(
        By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[3]/a')
    peaole_tag.click()
    time.sleep(2)

    first_person = driver.find_element(
        By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a')
    first_person.click()

def remove_duplicate_tweets(tweets):
    return [i for n, i in enumerate(tweets) if i not in tweets[n + 1:]]

def twitter_scraper(driver: drivertype):
    # inputs an email and password for the login details
    username = input('Enter your username: ')
    password = getpass('Enter your password: ')
    user = input('Enter the user you want to search: ')
    tweets_limit = int(input('Enter the number of tweets you want to get: ')) 

    driver.get('https://twitter.com/login')
    time.sleep(5)

    driver.maximize_window()  # I always maximize the window
    login(driver, username, password)
    time.sleep(5)

    search_profile(driver, user)
    time.sleep(5)

    tweets = []
    soup = bs4(driver.page_source, 'lxml')
    posts = soup.find_all(
        'div', {'class': 'css-1dbjc4n r-j5o65s r-qklmqi r-1adg3ll r-1ny4l3l'})

    while True:
        for post in posts:
            try:
                tweet = {
                    'text': post.find('div', class_ = 'css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0').text,
                    'posted_at': post.find('a', {'class': 'css-4rbku5 css-18t94o4 css-901oao r-14j79pv r-1loqt21 r-1q142lx r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-3s2u2q r-qvutc0'})['aria-label']
                }
                tweets.append(tweet)
                if len(tweets) >= tweets_limit:
                    break
            except:
                pass

        driver.execute_script(
            'window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(3)

        soup = bs4(driver.page_source, 'lxml')
        posts = soup.find_all(
            'div', {'class': 'css-1dbjc4n r-j5o65s r-qklmqi r-1adg3ll r-1ny4l3l'})
        tweets = remove_duplicate_tweets(tweets)
        if len(tweets) >= tweets_limit:
            break

    number_of_characters = 15
    filename = get_random_string(number_of_characters) + '.csv'
    path = f'files/{user.strip()}_tweets_{filename}'
    save_csv(path, tweets)

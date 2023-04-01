import time
import os
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager as CM
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TIMEOUT = 15
USERNAME = os.getenv('USERNAME')
dirname = os.path.dirname(__file__)


def scrape():
    options = webdriver.ChromeOptions()
    # Uncomment this option to run it headless
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument("--log-level=3")
    # Add a Mozila firefox user-agent so instagram doesn't block you.
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36')

    bot = webdriver.Chrome(executable_path=CM().install(), options=options)
    instagram = 'https://www.instagram.com/'
    url = instagram + str(USERNAME)

    print('[Info] - Scraping Followers...')
    try:
        bot.get(url)
        time.sleep(3.5)
        followers_span = bot.find_element(By.CSS_SELECTOR,
                                          "span[title]")

        total_followers = followers_span.get_attribute('title')

        print(total_followers)
        print('[Info] - Saving...')
        print('[Info] - Total of ' + total_followers + ' followers')

        with open(os.path.join(dirname, 'followers.txt'), 'r+') as file:
            file.seek(0, 0)
            file.write(total_followers)
        print('[DONE] - Your total followers are saved in followers.txt file!')

    except NoSuchElementException:
        print(NoSuchElementException)


if __name__ == '__main__':
    scrape()

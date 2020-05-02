import schedule
import time
import datetime
from news_blog.scraper import scrap


def scraping():
    print(scrap())
    print(datetime.datetime.now())


schedule.every(0.1).minutes.do(scraping)

if __name__ == "__main__":
    '''
    while True:
        schedule.run_pending()
        time.sleep(1)
    '''
    scraping()

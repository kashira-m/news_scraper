from bs4 import BeautifulSoup
import requests
import re
from sqlalchemy.exc import SQLAlchemyError

from news_blog import db
# Userモデルの取得
from news_blog.models import *


def scrap():
    URL = "https://beta.playvalorant.com/en-us/news/?ga=0"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    # extract news dates, titles, descriptions, image_links
    dates = [date.get_text() for date in soup.find_all("span", class_="NewsCard-module--published--37jmR")]
    titles = [title.get_text() for title in soup.find_all("h5", class_="heading-05 NewsCard-module--title--1MoLu")]
    descrs = [descr.get_text() for descr in
                    soup.find_all("p", class_="copy-02 NewsCard-module--description--3sFiD")]
    contain_image_links = [image.get("style") for image in
                           soup.find_all("span", class_="NewsCard-module--image--2sGrc")]
    image_links = []
    for image_link in contain_image_links:
        splited = re.split('[()]', str(image_link))
        print(splited[1])
        image_links.append(splited[1])

    article_links = [link['href'] for link in soup.select('a[draggable]')]
    for n in range(len(article_links)):
        pattern = r'https://'
        if not re.match(pattern, article_links[n]):
            article_links[n] = "https://beta.playvalorant.com" + article_links[n]

    print(article_links)

    try:
        sendData(dates, titles, descrs, image_links, article_links)
    except SQLAlchemyError as e:
        print(e)
        return False

    return True


# send data to database
def sendData(dates, titles, descrs, image_links, article_links):
    print(titles)
    for n in range(len(titles)):
        Title = News.query.filter(News.title == titles[n]).first()
        if Title:
            pass
        else:
            news = News()
            news.title = titles[n]
            news.date = dates[n]
            news.descr = descrs[n]
            news.image_link = image_links[n]
            news.article_link = article_links[n]
            db.session.add(news)
            db.session.commit()

    newses = db.session.query(News).all()
    for news in newses:
        print(news.title)


def rScrap():
    newses = db.session.query(News).order_by(News.id).all()
    # newses2 = News.query.order_by(News.id).all()
    print(newses)
    return newses


from flask import request, redirect, url_for, render_template, flash
from news_blog import app, db
from news_blog.models import News
from news_blog.scraper import rScrap

@app.route('/')
def show_entries():
    newses = rScrap()
    return render_template('index.html', newses=newses, num=len(newses))



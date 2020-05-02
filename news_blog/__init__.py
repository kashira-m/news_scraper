from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_object('news_blog.config')

db = SQLAlchemy(app)

import news_blog.views

from flask import Flask, render_template
from datetime import datetime

from webapp.weather import weather_by_city
from webapp.model import db, News
from webapp.model import db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        title = 'Новости Python'
        news_list = News.query.order_by(News.published.desc()).all()
        return render_template('index.html', page_title=title, weather=weather, news_list=news_list)
    return app

# ЗАПУСК СЕРВЕРА
# set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run
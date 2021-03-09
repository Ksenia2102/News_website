from flask import Flask, render_template

from webapp.weather import weather_by_city
from webapp.python_news import get_python_news


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    @app.route('/')
    def index():
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        title = 'Новости Python'
        news_list = get_python_news()
        return render_template('index.html', page_title=title, weather=weather, news_list=news_list)
    
    return app

# ЗАПУСК СЕРВЕРА
# set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run
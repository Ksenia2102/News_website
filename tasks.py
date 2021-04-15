from celery import Celery
from webapp import create_app
from webapp.news.parsers import habr
from celery.schedules import crontab

celery_app = Celery('tasks', broker='redis://localhost:6379/0')

flask_app = create_app()

@celery_app.task
def habr_snippets():
    with flask_app.app_context():
        habr.get_news_snippets()


@celery_app.task
def habr_content():
    with flask_app.app_context():
        habr.get_news_content()

@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute='*/100'), habr_snippets.s())
    sender.add_periodic_task(crontab(minute='*/100'), habr_content.s())


# запуск Celery 
# celery -A tasks worker --loglevel=info
import logging

from flask import Flask
from celery import Celery


app = Flask(__name__)

celery = Celery('tasks', broker='redis://localhost:6379/5')

logging.basicConfig(
    filename='log/centipede.log',
    level=logging.INFO,
    format='%(asctime)s %(message)s'
)

logger = logging.getLogger()

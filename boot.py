import logging
from celery import Celery


centipede_app = Celery('tasks', broker='redis://localhost:6379/5')

logging.basicConfig(
    filename='log/centipede.log',
    level=logging.INFO,
    format='%(asctime)s %(message)s'
)

logger = logging.getLogger()

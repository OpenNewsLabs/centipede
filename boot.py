import logging

logging.basicConfig(
    filename='log/centipede.log',
    level=logging.INFO,
    format='%(asctime)s %(message)s'
)

logger = logging.getLogger()

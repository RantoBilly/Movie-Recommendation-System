import logging


def setup_loggin():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    return logger
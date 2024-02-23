import logging

from .crawler_util import *
from .slider_util import *
from .time_util import *


def init_loging_config(log_filename='mylog.log'):
    level = logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(name)s %(levelname)s %(message)s ",
        datefmt='%Y-%m-%d  %H:%M:%S',
        filename=log_filename,
        filemode='w'
    )
    _logger = logging.getLogger("MediaCrawler")
    _logger.setLevel(level)

    # If you also want to log to console, you can add a StreamHandler explicitly
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s", datefmt='%Y-%m-%d %H:%M:%S')
    console_handler.setFormatter(formatter)
    _logger.addHandler(console_handler)

    return _logger


logger = init_loging_config()

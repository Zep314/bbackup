# Вывод на экран и логирование

from util.settings import Settings
import logging
from datetime import datetime as dt
from pytz import timezone

class View:
    def __init__(self):
        match Settings().log_level.lower():
            case 'critical':
                level = logging.CRITICAL
            case 'error':
                level = logging.ERROR
            case 'warning':
                level = logging.WARNING
            case 'debug':
                level = logging.DEBUG
            case 'notset':
                level = logging.NOTSET
            case _:
                level = logging.INFO

        logging.basicConfig(level=level,
#                            filename=Settings().work_dir + os.sep + Settings().log_file, filemode="w",
                            filename=Settings().log_file, filemode="a",
                            format="%(asctime)s %(levelname)s %(message)s"
                            )


    # Вывод в лог и на экран
    def print(self, level, msg):
        if level >= logging.root.level:
            print(f'{dt.now(timezone("Europe/Moscow")).strftime("%Y-%m-%d %H:%M:%S")} {msg}')
            self.to_log(level,msg)

    # Вывод только в лог
    @staticmethod
    def to_log(level, msg):
        match level:
            case logging.CRITICAL:
                logging.critical(msg)
            case logging.ERROR:
                logging.error(msg)
            case logging.WARNING:
                logging.warning(msg)
            case logging.INFO:
                logging.info(msg)
            case logging.DEBUG:
                logging.debug(msg)

    def message(self, level, msg):
        self.print(level, msg)
        # отправка сообщения в телегу или email
        pass
# Вывод на экран и логирование

from util.settings import Settings
import logging
import os


class View:
    def __init__(self):
        logging.basicConfig(level=logging.INFO,
                            filename=Settings().work_dir + os.sep + Settings().log_file, filemode="w",
                            format="%(asctime)s %(levelname)s %(message)s"
                            )

    # Вывод в лог и на экран
    def print(self, level, msg):
        if level >= logging.root.level:
            print(msg)
        self.to_log(level,msg)

    # Вывод только в лог
    @staticmethod
    def to_log(level, msg):
        logging.info(msg)

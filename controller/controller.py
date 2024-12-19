import os
import shutil

from view.view import View
from util.settings import Settings
from shutil import copytree, rmtree, disk_usage
import logging
from datetime import datetime as dt
from pytz import timezone

class Controller:
    def __init__(self):
        self._viewer = View()

        if os.name == 'nt':
            self._dst_name = 'c:\\test_backup' + os.sep
            self._src_name = 'c:\\if'
        else:
            self._dst_name = os.sep
            self._src_name = Settings().source_dir

        self._dst_name += Settings().destination_dir
        self._dst_name += os.sep + (Settings().prefix + '_' +
                                    dt.now(timezone("Europe/Moscow")).strftime("%Y-%m-%d_%H-%M-%S"))

    def my_copy(self, source_dir, destination_dir):
        copytree(source_dir, destination_dir, dirs_exist_ok=True)
    def run(self):
        self._viewer.message(logging.INFO, "Запуск резервного копирования...")
        self._viewer.print(logging.DEBUG, f"Папка источник для копирования: {self._src_name}")
        self._viewer.print(logging.DEBUG, f"Папка назначения для копирования: {self._dst_name}")

        self._viewer.print(logging.INFO, "Читаю каталог с файлами...")

        self._viewer.print(logging.INFO, "Копирую...")
#        self.my_copy(self._src_name, self._dst_name)
        self._viewer.message(logging.INFO, "Резервное копирование завершено.")

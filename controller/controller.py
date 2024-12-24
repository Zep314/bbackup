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
            self._dst_name = 'c:\\test_backup\\bbackup' + os.sep
            self._src_name = 'c:\\if'
        else:
            #self._dst_name = os.sep
            self._src_name = Settings().source_dir
            self._dst_name = Settings().destination_dir
        self._work_dir = self._dst_name
        self._dst_name += os.sep + (Settings().prefix + '_' +
                                    dt.now(timezone("Europe/Moscow")).strftime("%Y-%m-%d_%H-%M-%S"))

    def my_copy(self, source_dir, destination_dir):
        copytree(source_dir, destination_dir, dirs_exist_ok=True)
    def check_period(self):
        """
        :return: True - если период прошел, и нужно работать
                 False - если период копирования еще не настал
        """
        try:
            with os.scandir(self._work_dir) as dirs:
                dirs2 = []
                for entry in dirs:
                    if entry.is_dir():
                        dirs2.append(entry.name[-19:])
                print(dirs2)
            return True
        except os.error:
            self._viewer.message(logging.INFO, "Папка назначения не найдена")
            return True
        except:
            self._viewer.message(logging.ERROR, "Ошибка проверки папки назначения")
            return False
    def run(self):
        self._viewer.print(logging.DEBUG, "Старт программы...")
        if self.check_period():
            self._viewer.message(logging.INFO, "Запуск резервного копирования...")
            self._viewer.print(logging.DEBUG, f"Папка источник для копирования: {self._src_name}")
            self._viewer.print(logging.DEBUG, f"Папка назначения для копирования: {self._dst_name}")

            self._viewer.print(logging.INFO, "Читаю каталог с файлами...")

            self._viewer.print(logging.INFO, "Копирую...")
            self.my_copy(self._src_name, self._dst_name)
            self._viewer.message(logging.INFO, "Резервное копирование завершено.")
        self._viewer.print(logging.INFO, "Программа завершена.")

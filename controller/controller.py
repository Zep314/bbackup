import os

from view.view import View
from util.settings import Settings
from shutil import copytree, rmtree, disk_usage
import logging
from datetime import datetime as dt
from datetime import timedelta

from pytz import timezone
import json
import re
import psutil

LAST_BACKUP_TIME_FILE = 'lbtf.json'
MY_DT_FORMAT = '%Y-%m-%d_%H-%M-%S'

class Controller:
    def __init__(self):
        self._viewer = View()

        if os.name == 'nt':
            self._dst_name = 'c:\\test_backup\\bbackup' + os.sep
            self._src_name = 'c:\\if'
        else:
            # self._dst_name = os.sep
            self._src_name = Settings().source_dir
            self._dst_name = Settings().destination_dir
        self._work_dir = self._dst_name
        self._dst_name += os.sep + (Settings().prefix + '_' +
                                    dt.now(timezone("Europe/Moscow")).strftime(MY_DT_FORMAT))

    def my_copy(self, source_dir, destination_dir):
        copytree(source_dir, destination_dir, dirs_exist_ok=True)

    def save_backup_datetime(self):
        try:
            with open(LAST_BACKUP_TIME_FILE, 'w') as f:
                json.dump({'date1': dt.now().strftime(MY_DT_FORMAT)}, f)
        except Exception as e:
            self._viewer.print(logging.ERROR, "Ошибка записи времени работы")

    def check_period(self):
        try:
            with open(LAST_BACKUP_TIME_FILE, 'r') as f:
                d = json.load(f)
                date1 = dt.strptime(d['date1'], MY_DT_FORMAT)
                try:
                    digit = int(re.sub(r"[^\d\.]", "", Settings().period))
                except ValueError:
                    digit = 7
                char = re.sub(r"[\d\.]", "", Settings().period)
                char = char if len(char) > 0 else 'd'

                match char:
                    case 's':
                        delta = timedelta(seconds=digit)
                    case 'm':
                        delta = timedelta(minutes=digit)
                    case 'h':
                        delta = timedelta(hours=digit)
                    case 'w':
                        delta = timedelta(weeks=digit)
                    case _:
                        delta = timedelta(days=digit)
                if date1 + delta < dt.now():
                    return True
                else:
                    return False
        except FileNotFoundError:
            return True
        except json.decoder.JSONDecodeError:
            return True
        except KeyError:
            return True

    def check_dir(self):
        """
        :return: True - если папка назначения доступна, и нужно работать
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

    def check_drive(self):
        print(psutil.disk_partitions())
        return True
    def run(self):
        self._viewer.print(logging.DEBUG, "Старт программы...")
#        if self.check_period():
        if True:  #####!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Убрать!
            if self.check_drive():
                self._viewer.message(logging.INFO, "Запуск резервного копирования...")
                self._viewer.print(logging.DEBUG, f"Папка источник для копирования: {self._src_name}")
                self._viewer.print(logging.DEBUG, f"Папка назначения для копирования: {self._dst_name}")

                self._viewer.print(logging.INFO, "Читаю каталог с файлами...")

                self._viewer.print(logging.INFO, "Копирую...")
                self.my_copy(self._src_name, self._dst_name)
                self.save_backup_datetime()
                self._viewer.message(logging.INFO, "Резервное копирование завершено.")
        self._viewer.print(logging.INFO, "Программа завершена.")

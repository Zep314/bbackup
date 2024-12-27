# Настройки

import configparser
import sys


class Settings:
    def __init__(self):
        # Настройки читаем из ini - файла
        config = configparser.ConfigParser()

        try:
            config.read('bbackup.ini')
        except Exception as e:
            print(f"Не могу прочитать файл конфигурации: {e}")
            sys.exit(-1)

        self.log_file = config.get('DEFAULT', 'log_file')
        self.work_dir = config.get('DEFAULT', 'work_dir')
        self.source_dir = config.get('DEFAULT', 'source_dir')
        self.destination_dir = config.get('DEFAULT', 'destination_dir')
        self.log_level = config.get('DEFAULT', 'log_level')
        self.prefix = config.get('DEFAULT', 'prefix')
        self.keep_copy = config.get('DEFAULT', 'keep_copy')
        self.backup_volume = config.get('DEFAULT', 'backup_volume')
        self.period = config.get('DEFAULT', 'period')

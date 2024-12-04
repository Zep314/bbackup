from view.view import View
from util.settings import Settings

class Controller:
    def __init__(self):
        self._viewer = View()

    def run(self):
        self._viewer.print("Запуск выгрузки...")
        self._viewer.print("Читаю каталог с файлами...")

        self._viewer.print("Выгрузка завершена!")

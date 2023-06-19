import json
from os import walk, path
from pprint import pprint

errors_dir_root = "errors_json"

class Error:
    def __init__(self, json_file_name):

        """
            Создает объект ошибки с полями:
            code - код ошибки
            title - заголовок ошибки
            description - подробное описание ошибки, почему могла возникнуть
            details - что конкретно пошло не так(в это поле входят, например, неизвестные символы)
            possible_solution - какие действия следует предпринять и в какао порядке, чтобы исправить ошибку?

            Args:
                Название json-файла со структурой ошибки. Из неё будет браться инфа, которая заполняет выходные поля.
                Файл может указываться с частью пути, начинающегося с папки, не выше <errors_dir_root>

            Returns:
                None
        """

        # Определяем поля класса

        self.code = 0
        self.title = ""
        self.description = ""
        self.details = ""
        self.possible_solution = ""

        # Если в имя json-файла не входит формат, добавляем его (.json)

        if json_file_name[-5:] != ".json":
            json_file_name += ".json"

        # находим нужный json-файл среди всей структуры папок, начиная с <errors_dir_root>

        json_file_name = self.find_error_file(json_file_name, errors_dir_root)

        # ВРЕМЕННО!!! Выводим содержимое структуры ошибки

        with open(f"{json_file_name}", "r", encoding="utf8") as file:
            data = json.load(file)
            pprint(data)

    def find_error_file(self, json_file_name, root_dir):

        # Перебираем рекурсивно json-файлы ошибок начиная с errors_json в поисках нужного пути
        for root, dirs, files in walk(root_dir, topdown=False):
            if path.exists(root + '\\' + json_file_name):
                return root+'\\'+json_file_name
            else:
                for dir in dirs:
                    self.find_error_file(json_file_name, root_dir+'\\'+dir)


if __name__ == '__main__':
    Error("card_create_errors\\card_create_error.json")
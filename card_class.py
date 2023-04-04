from typing import List


class Card:
    """Класс, представляющий карточку."""

    def __init__(self, name: str, values: List[str]):
        """
        Создает новую карточку, предварительно заранее проверив корректность входных знаений

        Args:
            name: Имя карточки.
            values: Значения карточки. По умолчанию все значения флагов == None
        """
        self.name = name
        self.values = []
        # Итерируемся по каждому значению в списке значений
        for value in values:
            # Создаем словарь с флагами для каждого значения
            value_flags = {
                'is_simple': None,  # Простое значение
                'is_selfref': None,  # Значение, которое ссылается на себя
                'is_templ': None,  # Шаблонное значение
                'is_id': None,  # Значение, которое является идентификатором
            }
            # Добавляем словарь в список значений
            self.values.append({'value': value, 'flags': value_flags})

    def get_values(self) -> List[str]:
        """
        Возвращает список значений, содержащихся в данной карте.

        Возвращает:
            List[str]: Список строковых значений, содержащихся в карте.
        """
        return [value['value'] for value in self.values]

    def check_one_value(self, value: str) -> bool:
        """Проверяет, может ли данное значение value быть использовано для создания карты.
        Args:
            value: строка, значение, которое нужно проверить.

        Returns:
            Если значение value уже есть в карте или входит в имя карты, то возвращает False.
            Если же данное значение может быть использовано для создания карты, возвращает True.
        """

        # Проверяем, если значение пустое, то оно не может быть использовано.
        if value == "":
            return False

        # Проверяем, если значение уже есть в списке значений карты, то оно не может быть использовано повторно.
        for val in self.values:
            if value == val['value']:
                return False

        # Проверяем, если значение входит в имя карты, то оно не может быть использовано.
        if value in self.name:
            return False

        # Если значение не повторяется в списке значений карты и не входит в имя карты, то оно может быть использовано.
        return True

    def check_some_values(self, values: List[str]) -> List[bool]:
        """
        Проверяет, являются ли все значения из списка допустимыми для данной карты.

        Параметры:
            values (List[str]): список значений, которые необходимо проверить.

        Возвращает:
            List[bool]: список значений True и False для каждого добавляемого значения в порядке их следования в параметрах.
        """
        return [self.check_one_value(value) for value in values]

    def add_one_value(self, value: str) -> bool:
        """
        Добавляет одно значение в карту, если оно может быть добавлено.

        Args:
            value (str): Значение, которое нужно добавить в карту.

        Returns:
            bool: True, если значение было успешно добавлено, False в противном случае.
        """

        value_flags = {
            'is_simple': None,  # Простое значение
            'is_selfref': None,  # Значение, которое ссылается на себя
            'is_templ': None,  # Шаблонное значение
            'is_id': None,  # Значение, которое является идентификатором
        }
        if self.check_one_value(value):
            # Значение может быть добавлено в карту.
            self.values.append({'value': value, 'flags': value_flags})
            return True
        else:
            # Значение не может быть добавлено в карту.
            return False

    def add_some_values(self, values: List[str]) -> List[bool]:
        """
        Добавляет список значений в список значений карты, используя add_one_value для каждого значения.

        Args:
            values: Список значений, которые нужно добавить.

        Returns:
            Список из значений True и False для каждого добавляемого значения в порядке их следования в параметрах.
        """
        results = []
        for value in values:
            if self.add_one_value(value):
                results.append(True)
            else:
                results.append(False)
        return results

    def delete_one_value(self, value: str) -> bool:
        """
        Удаляет значение из списка значений карты.

        Args:
            value (str): Значение, которое нужно удалить из карты.

        Returns:
            bool: True, если значение было успешно удалено, False в противном случае.
        """
        for item in self.values:
            if item['value'] == value:
                self.values.remove(item)
                return True
        return False

    def delete_some_values(self, values: List[str]) -> List[bool]:
        """
        Удаляет список значений из карты.

        Args:
            values: Список значений, которые нужно удалить.

        Returns:
            Список значений True и False для каждого значения в порядке их следования в параметрах.
        """
        result = []
        for value in values:
            if self.delete_one_value(value):
                result.append(True)
            else:
                result.append(False)
        return result

    def exchange_value(self, old_value: str, new_value: str) -> bool:
        """
        Заменяет одно значение карты на другое.

        Args:
            old_value: Старое значение, которое нужно заменить.
            new_value: Новое значение, на которое нужно заменить старое.

        Returns:
            bool: True, если старое значение было найдено и успешно заменено, False в противном случае.
        """
        for i, value in enumerate(self.values):
            if value['value'] == old_value:
                self.values[i] = {'value': new_value, 'flags': value['flags']}
                return True
        return False
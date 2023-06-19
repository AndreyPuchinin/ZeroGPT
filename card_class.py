from typing import List


class Card:
    """Класс, представляющий карточку."""

    def __init__(self, name: str, values: List[str]):
        """
        Создает новую карточку, предварительно заранее проверив корректность входных значений

        Args:
            name: Имя карточки.
            values: Значения карточки. По умолчанию все значения флагов == None
        """

        if len(values) == 0:
            raise ValueError("Error! No values.")

        self.name = name
        self.values = []

        # убеждаемся в корректности карты
        self.check_some_values(values)

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

    def is_selfref_val(self, value):
        """
        Проверяет, является ли значение самоссылкой

        Args:
            value: значение, которое надо проверить

        :return:
            True, если значение - самоссылка
            False иначе
        """
        if self.name in value:
            return True
        return False

    def get_values_with_flags(self) -> list[dict[str, dict[str, None | bool] | str]]:
        """
        Возвращает список значений, содержащихся в данной карте, включая флаги для каждого значения.

        Returns:
            Список значений с флагами.

        """
        return self.values

    def get_values_without_flags(self) -> List[str]:
        """
        Возвращает список значений, содержащихся в данной карте, НЕ включая флаги для каждого значения.

        Returns:
            Список значений без флагов.

        """
        return [value['value'] for value in self.values]

    def get_card(self):
        """
        Возвращает словарь с именем карточки и значениями карточки.

        Returns:
            Словарь с именем и значениями карточки.

        """
        return {'name': self.name, 'values': self.get_values_without_flags()}

    def check_one_value(self, value: str) -> bool:
        """
        Проверяет, может ли данное значение value быть использовано для создания карты.
        Более подробные условия смотри ниже в реализации функции.

        Args:
            value: строка, значение, которое нужно проверить.

        Returns:
            Если значение value пустое, то кидает исключение ValueError (см. ниже).
            Если значение value уже есть в карте или входит в имя карты, то кидает исключение ValueError (см. ниже).
            Если же данное значение может быть использовано для создания карты, возвращает True.
        """

        # Проверяем, если значение пустое, то оно не может быть использовано.
        if value == "":
            raise ValueError("Error! Empty value.")

        # Проверяем, если значение уже есть в списке значений карты, то оно не может быть использовано повторно.
        for val in self.values:
            if value == val['value']:
                raise ValueError(f'Error! The value \'{value}\' is already in card.')

        # Проверяем, если значение входит в имя карты, то оно не может быть использовано.
        if value in self.name:
            raise ValueError(f'Error! The name \'{self.name}\' shouldn\'t contain the value \'{value}\'.')

        # Если значение не повторяется в списке значений карты и не входит в имя карты, то оно может быть использовано.
        return True

    def check_some_values(self, values: List[str]) -> bool:
        """
        Проверяет, являются ли все значения из списка допустимыми для данной карты.

        Args:
            values (List[str]): список значений, которые необходимо проверить.

        Returns:
            True - если все значения допустимы
            Иначе - выбрасывает иключение из check_one_value()

        """
        for val in values:
            if values.count(val) > 1:
                raise ValueError(f'Error! The value \'{val}\' repeats.')
        for value in values:
            self.check_one_value(value)
        return True

    def add_one_value(self, value: str) -> bool:
        """
        Добавляет одно значение в карту, если оно может быть добавлено.
        Кидает исключение, если значеие не может быть добавлено.

        Args:
            value (str): Значение, которое нужно добавить в карту.

        Returns:
            bool: True, если значение было успешно добавлено.
            Иначе - выбрасывает иключение из check_one_value()

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
        # else НЕ НУЖЕН - есть исключения из check_one_value()
        # else:
        #    # Значение не может быть добавлено в карту.
        #    return False

    def add_some_values(self, values: List[str]) -> bool:
        """
        Добавляет список значений в список значений карты, проверяя каждое значение на корректность.
        Если значение некорректно, кидается исключение, и это значние не добавляется.

        Args:
            values: Список значений, которые нужно добавить.

        Returns:
            True, если все значения были успешно добавлены.
            Иначе - выбрасывает иключение из check_one_value()

        """
        for value in values:
            self.add_one_value(value)
        return True

    def delete_one_value(self, value: str) -> bool:
        """
        Удаляет значение из списка значений карты.

        Args:
            value (str): Значение, которое нужно удалить из карты.

        Returns:
            bool: True, если значение было успешно удалено
            Иначе - выбрасывает собсвтенное иключение.
            # Уточнить тип исключения! (сейчас просто Exception)

        """
        if value == '':
            raise ValueError('Error! Empty value.')
        for item in self.values:
            if item['value'] == value:
                self.values.remove(item)
                return True
        raise Exception(f'Error! No \'{value}\' value in card.')  # какого типа лучше бросить исключение?

    def delete_some_values(self, values: List[str]) -> bool:
        """
        Удаляет список значений из карты, если они могут быть удалены.
        В противном случае кидает исключение.

        Args:
            values: Список значений, которые нужно удалить.

        Returns:
            True, если все значения были успешно удалены.
            Иначе - выбрасывает иключение из delete_one_value()

        """

        for value in values:
            self.delete_one_value(value)
        return True

    def exchange_value(self, old_value: str, new_value: str) -> bool:
        """
        Заменяет одно значение карты на другое.

        Args:
            old_value: Старое значение, которое нужно заменить.
            new_value: Новое значение, на которое нужно заменить старое.

        Returns:
            bool: True, если старое значение было найдено и успешно заменено, False в противном случае.
            Иначе - выбрасывает собственное иключение.

        Examples:
            >>> card = Card("Test Card", ["Value 1", "Value 2", "Value 3"])
            >>> card.exchange_value("", "Value4")
            Traceback (most recent call last):
            ...
            ValueError: Error! Empty old value.
            >>> card.exchange_value("Value 1", "")
            Traceback (most recent call last):
            ...
            ValueError: Error! Empty new value.
            >>> card.exchange_value("Value 5","Value 6")
            Traceback (most recent call last):
            ...
            ValueError: Error! No 'Value 5' value in the card.
            >>> card.exchange_value("Value 3", "Value 3")
            Traceback (most recent call last):
            ...
            ValueError: Error! New value repeats the old value.
            >>> card.exchange_value("Value 2", "Value 4")
            True
        """
        if old_value == '':
            raise ValueError('Error! Empty old value.')

        elif new_value == '':
            raise ValueError('Error! Empty new value.')

        elif old_value == new_value:
            raise ValueError('Error! New value repeats the old value.')

        for i, value in enumerate(self.values):
            if value['value'] == old_value:
                self.values[i] = {'value': new_value, 'flags': value['flags']}
                return True
        raise ValueError(f'Error! No \'{old_value}\' value in the card.')


# if __name__ == '__main__':
    # card = Card("Test Card", ["Value 1"])
    # print(card.check_one_value("Test Card"))
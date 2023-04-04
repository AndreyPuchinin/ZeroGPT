from typing import List


class Card:
    """Класс, представляющий карточку."""

    def __init__(self, name: str, values: List[str]):
        """
        Создает новую карточку, предварительно заранее проверив корректность входных знаений

        Args:
            name: Имя карточки.
            values: Значения карточки.
        """
        self.name = name
        self.values = []
        for value in values:

            # на всякий случай проверяем, корректны ли вводимые значения
            if self.check_one_value(value):
                self.values.append(value)

    def get_values(self) -> List[str]:
        """
        Возвращает список значений, содержащихся в данной карте.

        Возвращает:
            List[str]: Список строковых значений, содержащихся в карте.
        """
        return list(self.values)

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
        if value in self.values:
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
        if self.check_one_value(value):
            # Значение может быть добавлено в карту.
            self.values.append(value)
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
        if value in self.values:
            # Значение есть в списке значений карты и может быть удалено.
            self.values.remove(value)
            return True
        else:
            # Значение не найдено в списке значений карты.
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
        if old_value in self.values:
            self.values.remove(old_value)
            self.values.append(new_value)
            return True
        else:
            return False


def test_check_one_value():
    card = Card("Test Card", ["Value 1", "Value 2"])
    assert card.check_one_value("Value 1") == False
    assert card.check_one_value("Value 2") == False
    assert card.check_one_value("Value 3") == True
    assert card.check_one_value("Test") == False
    assert card.check_one_value("") == False


def test_check_some_values():
    card = Card('name1', ['A', 'K', 'Q', 'J', '10'])

    assert card.check_some_values(['A', '10']) == [False, False]
    assert card.check_some_values(['K', '9']) == [False, True]
    assert card.check_some_values(['7', '8', '9']) == [True, True, True]


def test_add_one_value():
    card = Card("Test Card", ["Value 1", "Value 2"])
    assert card.add_one_value("Value 1") == False
    assert card.add_one_value("Value 2") == False
    assert card.add_one_value("Value 3") == True
    assert card.add_one_value("Test") == False
    assert card.add_one_value("") == False


def test_add_some_values():
    card = Card('name1', ['A', 'K', 'Q', 'J', '10'])

    assert card.add_some_values(['A', 'K', 'Q']) == [False, False, False]
    assert card.add_some_values(['J', '10', '9']) == [False, False, True]
    assert set(card.get_values()) == {'A', 'K', 'Q', 'J', '10', '9'}


def test_delete_one_value():
    card = Card("Test Card", ["Value 1", "Value 2", "Value 3"])
    card.delete_one_value("Value 2")
    assert "Value 2" not in card.values


def test_delete_some_values():
    card = Card('name1', ['A', 'K', 'Q', 'J', '10'])

    assert card.delete_some_values(['A', '10']) == [True, True]
    assert card.get_values() == ['K', 'Q', 'J']
    assert card.delete_some_values(['7', '8', '9']) == [False, False, False]


def test_exchange_value():
    card = Card("Test Card", ["Value 1", "Value 2", "Value 3"])
    card.exchange_value("Value 2", "Value 4")
    assert "Value 2" not in card.values and "Value 4" in card.values


if __name__ == "__main__":
    test_check_one_value()
    test_check_some_values()
    test_add_one_value()
    test_add_some_values()
    test_delete_one_value()
    test_delete_some_values()
    test_exchange_value()

    print("All tests pass")
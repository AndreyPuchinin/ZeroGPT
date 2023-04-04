from card_class import Card
from typing import List


class CardsManager:
    """Класс, управляющий картами."""

    def __init__(self):
        """Создает новый менеджер карт."""
        self.cards = []

    def check_one_card(self, card: Card) -> bool:
        """
        Проверяет, можно ли добавить данную карту в CardManager.

        Args:
            card: Карта, которую нужно проверить.

        Returns:
            True, если карту можно добавить, иначе False.
        """
        # Проверяем, что значения карты корректны
        if not card.check_some_values(card.values):
            return False

        # Проверяем, что все значения уникальны для всех карт, имеющихся в CardsManager
        all_values = set()
        for other_card in self.cards:
            all_values.update(other_card.values)
        if any(val in all_values for val in card.values):
            return False

        # Проверяем, что имя карты уникально для всех карт из CardsManager
        if any(c.name == card.name for c in self.cards):
            return False

        # Если все проверки пройдены, возвращаем True
        return True

    def check_some_cards(self, cards: List[Card]) -> List[bool]:
        """
        Проверяет, можно ли добавить список карт в CardManager.

        Args:
            cards: Список карт, которые нужно проверить.

        Returns:
            Список булевых значений, где True соответствует тому, что карта может быть добавлена в CardManager,
            а False - что карта не может быть добавлена в CardManager.
        """
        return [self.check_one_card(card) for card in cards]

    def add_one_card(self, card: Card) -> bool:
        """
        Добавляет карту в CardsManager, если она проходит проверку.

        Args:
            card: Карта, которую нужно добавить.

        Returns:
            True, если карта была успешно добавлена, иначе False.
        """
        if self.check_one_card(card):
            self.cards.append(card)
            return True
        return False

    def add_some_cards(self, cards: List[Card]) -> List[bool]:
        """
        Добавляет список карт в CardsManager, используя метод add_one_card.

        Args:
            cards: Список карт, которые нужно добавить.

        Returns:
            Список булевых значений, где True соответствует успешно добавленной карте, а False - некорректной карте.
        """
        results = []
        for card in cards:
            if self.add_one_card(card):
                results.append(True)
            else:
                results.append(False)
        return results

    def find_card_by_name(self, name: str) -> Card | None:
        """
        Ищет карту в CardsManager по имени.

        Args:
            name: имя карты, которую нужно найти.

        Returns:
            Объект Card, если карта найдена, иначе None.
        """
        for card in self.cards:
            if card.name == name:
                return card
        return None

    def find_card_by_value(self, value: str) -> Card | None:
        """
        Ищет карту по ее значению.

        Args:
            value: значение, по которому нужно найти карту.

        Returns:
            Объект карты типа Card, если карта найдена, иначе None.
        """
        for card in self.cards:
            if card.value == value:
                return card
        return None

    def remove_card_by_name(self, name: str) -> Card | None:
        """Удаляет карту из списка по ее имени.

        Args:
            name: строка, имя карты, которую нужно удалить.

        Returns:
            Объект типа Card, если карта была найдена и удалена, иначе None.
        """
        # Проходим по всем картам в списке.
        for i, card in enumerate(self.cards):
            # Если имя карты соответствует заданному имени, то удаляем карту из списка и возвращаем ее объект.
            if card.name == name:
                return self.cards.pop(i)
        # Если карта не найдена, то возвращаем None.
        return None

    def remove_card_by_value(self, value: str) -> Card | None:
        """
        Удаляет первую найденную карту с заданным значением value.

        Args:
            value: Значение карты, которую нужно удалить.

        Returns:
            Удаленный объект Card, если карта найдена и удалена успешно, иначе None.
        """
        for i, card in enumerate(self.cards):
            if card.value == value:
                # Если найдена карта с заданным значением, удаляем ее из списка карт и возвращаем ее
                return self.cards.pop(i)
        # Если карта не найдена, возвращаем None
        return None


def test_check_one_card():
    manager = CardsManager()

    # Добавляем первую карту, она должна пройти проверку
    card1 = Card("card1", ["value1", "value2"])
    assert manager.check_one_card(card1) == True

    # Добавляем вторую карту, ее значение уже есть в первой карте, проверка должна вернуть False
    card2 = Card("card2", ["value2", "value3"])
    assert manager.check_one_card(card2) == False

    # Добавляем третью карту, ее имя уже есть в первой карте, проверка должна вернуть False
    card3 = Card("card1", ["value4", "value5"])
    assert manager.check_one_card(card3) == False


def test_check_some_cards():
    manager = CardsManager()

    # Создаем список из двух карт, обе должны пройти проверку
    cards1 = [Card("card1", ["value1", "value2"]), Card("card2", ["value3", "value4"])]
    assert manager.check_some_cards(cards1) == [True, True]

    # Создаем список из двух карт, первая карта уже есть в менеджере, вторая карта проходит проверку
    cards2 = [Card("card1", ["value1", "value2"]), Card("card3", ["value5", "value6"])]
    assert manager.check_some_cards(cards2) == [False, True]

    # Создаем список из двух карт, обе карты уже есть в менеджере, проверка должна вернуть False для обоих карт
    cards3 = [Card("card1", ["value1", "value2"]), Card("card2", ["value3", "value4"])]
    assert manager.check_some_cards(cards3) == [False, False]


def test_add_one_card():
    manager = CardsManager()

    # Добавляем первую карту, она должна успешно добавиться
    card1 = Card("card1", ["value1", "value2"])
    assert manager.add_one_card(card1) == True

    # Добавляем вторую карту, ее значение уже есть в первой карте, добавление должно провалиться
    card2 = Card("card2", ["value2", "value3"])
    assert manager.add_one_card(card2) == False

    # Добавляем третью карту, ее имя уже есть в первой карте, добавление должно провалиться
    card3 = Card("card1", ["value4", "value5"])
    assert manager.add_one_card(card3) == False




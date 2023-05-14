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
        Более подробные условия смотри ниже в реализации функции.

        Args:
            card: Карта, которую нужно проверить.

        Returns:
            Исключение  еще до запуска данной функции check_one_card(), если  сама добавляемая карта некорректна
            (см. класс Card).
            Исключение, если  значение добавляемой карты уже есть в существующих картах.
            Исключение, если  имя добавляемой карты уже есть в существующих картах.
            True иначе.

        Examples:
            >>> manager = CardsManager()
            >>> Card("Card 1", ["Value 1", ""])
            Traceback (most recent call last):
            ...
            ValueError: Error! Empty value.
            >>> Card("Card 1", ["Value 1", "Value 1"])
            Traceback (most recent call last):
            ...
            ValueError: Error! The value 'Value 1' repeats.
            >>> Card("Card 1", ["Value 1", "Card"])
            Traceback (most recent call last):
            ...
            ValueError: Error! The name 'Card 1' shouldn't contain the value 'Card'.
            >>> card1 = Card("Card 1", ["Value 1", "Value 2"])
            >>> card2 = Card("Card 2", ["Value 3", "Value 2"])
            >>> manager.add_one_card(card1)
            True
            >>> manager.check_one_card(card2)
            Traceback (most recent call last):
            ...
            \
ValueError: Error! The card {'name': 'Card 1', 'values': ['Value 1', 'Value 2']} \
already consists the value 'Value 2'.
            >>> card3 = Card("Card 1", ["Value 4", "Value 5"])
            >>> manager.check_one_card(card3)
            Traceback (most recent call last):
            ...
            \
ValueError: Error! The card {'name': 'Card 1', 'values': ['Value 1', 'Value 2']} \
already consists the name 'Card 1'.
            >>> card4 = Card("Card 3", ["Value 4"])
            >>> manager.check_one_card(card4)
            True
            """

        # Проверяем, что все значения уникальны для всех карт, имеющихся в CardsManager
        for value in card.get_values_without_flags():
            for existing_card in self.cards:
                for existing_value in existing_card.get_values_without_flags():
                    if value == existing_value:
                        raise ValueError(
                            f"Error! The card {existing_card.get_card()} already consists the value \'{value}\'.")

        # Проверяем, что имя карты уникально для всех карт из CardsManager
        for existing_card in self.cards:
            if card.name == existing_card.name:
                raise ValueError(f"Error! The card {existing_card.get_card()} already consists the name \'{card.name}\'.")

        # Если все проверки пройдены, возвращаем True
        return True

    def check_some_cards(self, cards: List[Card]) -> bool:
        """
        Проверяет, можно ли добавить список карт в CardManager.

        Args:
            cards: Список карт, которые нужно проверить.

        Returns:
            Исключение из check_one_card(), если хотя бы одно значение не может быть добавлено.
            True, если все карты могут быть добавлены.

        Examples:
            >>> manager = CardsManager()
            >>> card1 = Card("Card 1", ["Value 1", "Value 2"])
            >>> card2 = Card("Card 2", ["Value 3", "Value 4"])
            >>> card3 = Card("Card 3", ["Value 5", "Value 2"])
            >>> card4 = Card("Card 1", ["Value 6", "Value 7"])
            >>> manager.add_one_card(card1)
            True
            >>> manager.check_some_cards([card2])
            True
            >>> manager.check_some_cards([card2, card3])
            Traceback (most recent call last):
            ...
            \
ValueError: Error! The card {'name': 'Card 1', 'values': ['Value 1', 'Value 2']} \
already consists the value 'Value 2'.
            >>> manager.check_some_cards([card4])
            Traceback (most recent call last):
            ...
            \
ValueError: Error! The card {'name': 'Card 1', 'values': ['Value 1', 'Value 2']} \
already consists the name 'Card 1'.
        """
        for card in cards:
            self.check_one_card(card)
        return True

    def add_one_card(self, card: Card) -> bool:
        """
        Добавляет карту в CardsManager, если она проходит проверку на корректность.

        Args:
            card: Карта, которую нужно добавить.

        Returns:
            Исключение из check_one_card(), если карта не может быть добавлена.
            True иначе.

        Examples:
            >>> manager = CardsManager()
            >>> card1 = Card("Card 1", ["Value 1", "Value 2"])
            >>> card2 = Card("Card 2", ["Value 3", "Value 4"])
            >>> card3 = Card("Card 3", ["Value 5", "Value 2"])
            >>> card4 = Card("Card 1", ["Value 6", "Value 7"])
            >>> manager.add_one_card(card1)
            True
            >>> manager.add_one_card(card3)
            Traceback (most recent call last):
            ...
            \
ValueError: Error! The card {'name': 'Card 1', 'values': ['Value 1', 'Value 2']} \
already consists the value 'Value 2'.
            >>> manager.add_one_card(card4)
            Traceback (most recent call last):
            ...
            \
ValueError: Error! The card {'name': 'Card 1', 'values': ['Value 1', 'Value 2']} \
already consists the name 'Card 1'.
        """
        self.check_one_card(card)
        self.cards.append(card)
        return True

    def add_some_cards(self, cards: List[Card]) -> bool:
        """
        Добавляет список карт в CardsManager, используя метод add_one_card.

        Args:
            cards: Список карт, которые нужно добавить.

        Returns:
            Исключение из check_one_card(), если карта не может быть доабвалена
            True иначе.

        Examples:
            >>> manager = CardsManager()
            >>> card1 = Card("Card 1", ["Value 1", "Value 2"])
            >>> card2 = Card("Card 2", ["Value 3", "Value 4"])
            >>> card3 = Card("Card 3", ["Value 5", "Value 2"])
            >>> card4 = Card("Card 1", ["Value 6", "Value 7"])
            >>> manager.add_one_card(card1)
            True
            >>> manager.add_some_cards([card2, card3])
            Traceback (most recent call last):
            ...
            \
ValueError: Error! The card {'name': 'Card 1', 'values': ['Value 1', 'Value 2']} \
already consists the value 'Value 2'.
            >>> manager.add_some_cards([card4])
            Traceback (most recent call last):
            ...
            \
ValueError: Error! The card {'name': 'Card 1', 'values': ['Value 1', 'Value 2']} \
already consists the name 'Card 1'.
        """
        results = []
        for card in cards:
            self.add_one_card(card)
        return True

    def find_card_by_name(self, name: str) -> Card | None:
        """
        Ищет карту в CardsManager по имени, если таковая есть.

        Args:
            name: имя карты, которую нужно найти.

        Returns:
            Собственное исключение, если карта не найдена.
            Объект Card иначе.

        Examples:
            >>> manager = CardsManager()
            >>> card1 = Card('Card 1', ['Value 1'])
            >>> manager.add_one_card(card1)
            True
            >>> manager.find_card_by_name('Card 2')
            Traceback (most recent call last):
            ...
            NameError: Error! No card with name 'Card 2'.
            >>> manager.find_card_by_name('Card 1').get_card()
            {'name': 'Card 1', 'values': ['Value 1']}
        """
        for card in self.cards:
            if card.name == name:
                return card
        raise NameError(f'Error! No card with name \'{name}\'.')

    def find_card_by_value(self, value: str) -> Card:
        """
        Ищет карту по ее значению.

        Args:
            value: значение, по которому нужно найти карту.

        Returns:
            Собственное исклеючение, если карта не найдена.
            Объект карты типа Card иначе.

        Examples:
            >>> manager = CardsManager()
            >>> card1 = Card('Card 1', ['Value 1'])
            >>> manager.add_one_card(card1)
            True
            >>> manager.find_card_by_value('Value 2')
            Traceback (most recent call last):
            ...
            ValueError: Error! No card with value 'Value 2'.
            >>> manager.find_card_by_value('Value 1').get_card()
            {'name': 'Card 1', 'values': ['Value 1']}
        """
        for card in self.cards:
            for existing_value in card.get_values_without_flags():
                if existing_value == value:
                    return card
        raise ValueError(f'Error! No card with value \'{value}\'.')

    def remove_card_by_name(self, name: str) -> Card | None:
        """Удаляет карту из списка по ее имени, если таковая имеется.

        Args:
            name: строка, имя карты, которую нужно удалить.

        Returns:
            Исключение из find_card_by_name(), если карта не найдена.
            Объект типа Card (удаленнноя карта) иначе.

        Examples:
            >>> manager = CardsManager()
            >>> card1 = Card('Card 1', ['Value 1'])
            >>> manager.add_one_card(card1)
            True
            >>> manager.remove_card_by_name('Card 2')
            Traceback (most recent call last):
            ...
            NameError: Error! No card with name 'Card 2'.
            >>> manager.remove_card_by_name('Card 1').get_card()
            {'name': 'Card 1', 'values': ['Value 1']}
            >>> len(manager.cards)
            0
        """
        # Проверяем, что карта с таким именем есть.
        self.find_card_by_name(name)

        # Проходим по всем картам в списке.
        for i, card in enumerate(self.cards):
            # Если имя карты соответствует заданному имени, то удаляем карту из списка и возвращаем ее объект.
            if card.name == name:
                return self.cards.pop(i)

    def remove_card_by_value(self, value: str) -> Card:
        """
        Удаляет первую найденную карту с заданным значением value, если таковая есть.

        Args:
            value: Значение карты, которую нужно удалить.

        Returns:
            Исключение из find_card_by_value(), если карта не найдена.
            Удаленный объект Card иначе.

        Examples:
            >>> manager = CardsManager()
            >>> card1 = Card('Card 1', ['Value 1'])
            >>> manager.add_one_card(card1)
            True
            >>> manager.remove_card_by_value('Value 2')
            Traceback (most recent call last):
            ...
            ValueError: Error! No card with value 'Value 2'.
            >>> manager.remove_card_by_value('Value 1').get_card()
            {'name': 'Card 1', 'values': ['Value 1']}
        """
        # Проверяем, что карта с таким значением есть.
        self.find_card_by_value(value)

        for i, card in enumerate(self.cards):
            for existing_value in card.get_values_without_flags():
                if existing_value == value:
                    # Если найдена карта с заданным значением, удаляем ее из списка карт и возвращаем ее
                    return self.cards.pop(i)
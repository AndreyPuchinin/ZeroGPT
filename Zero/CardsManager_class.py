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

    def check_some_cards(self, cards: List[Card]) -> bool:
        """
        Проверяет, можно ли добавить список карт в CardManager.

        Args:
            cards: Список карт, которые нужно проверить.

        Returns:
            True, если все карты можно добавить, иначе False.
        """
        for card in cards:
            if not self.check_one_card(card):
                return False
        return True

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

    def add_some_cards(self, cards: List[Card]) -> int:
        """
        Добавляет список карт в CardsManager, используя метод add_one_card.

        Args:
            cards: Список карт, которые нужно добавить.

        Returns:
            Количество успешно добавленных карт.
        """
        count = 0
        for card in cards:
            if self.add_one_card(card):
                count += 1
        return count
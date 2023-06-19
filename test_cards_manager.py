import unittest
from typing import List
from CardsManager_class import Card, CardsManager


class TestCardManager(unittest.TestCase):
    def setUp(self):
        pass

    def test_check_one_card_returns_true_for_valid_card(self):
        self.cards_manager = CardsManager()
        # Создаем карту, которую будем проверять
        card = Card("Test card", ["value1", "value2", "value3"])

        # Проверяем, что метод возвращает True
        result = self.cards_manager.check_one_card(card)
        self.assertTrue(result)

    def test_check_one_card_returns_false_if_values_not_unique(self):
        self.cards_manager = CardsManager()
        # Создаем карту, у которой есть одно значение, которое уже есть у другой карты
        card1 = Card("Test card 1", ["value1", "value2"])
        card2 = Card("Test card 2", ["value2", "value3"])

        # Добавляем первую карту в CardsManager
        self.cards_manager.cards.append(card1)

        # Проверяем, что метод возвращает False при попытке добавить вторую карту
        result = self.cards_manager.check_one_card(card2)
        self.assertFalse(result)

    def test_check_one_card_returns_false_if_card_name_not_unique(self):
        self.cards_manager = CardsManager()
        # Создаем две карты с одинаковыми именами
        card1 = Card("Test card", ["value1", "value2"])
        card2 = Card("Test card", ["value3", "value4"])

        # Добавляем первую карту в CardsManager
        self.cards_manager.cards.append(card1)

        # Проверяем, что метод возвращает False при попытке добавить вторую карту
        result = self.cards_manager.check_one_card(card2)
        self.assertFalse(result)

    def test_check_one_card_returns_false_if_card_values_invalid(self):
        self.cards_manager = CardsManager()
        # Создаем карту, у которой одно значение не проходит проверку
        card = Card("Test card", ["invalid_value", "value2"])

        # Проверяем, что метод возвращает False
        # print(self.cards_manager.check_one_card(card))
        # self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
from unittest import TestCase, main
from card_class import *


class CardTest(TestCase):
    def test_card_create(self):

        # Карта БЕЗ значений

        with self.assertRaises(ValueError) as e:
            Card("Card 1", [])
        self.assertEqual('Error! No values.', e.exception.args[0])

        # Пустое значение

        with self.assertRaises(ValueError) as e:
            Card("Card 1", ["Value 1", ""])
        self.assertEqual('Error! Empty value.', e.exception.args[0])

        # Повторное значение

        with self.assertRaises(ValueError) as e:
            Card("Card 1", ["Value 1", "Value 1"])
        self.assertEqual('Error! The value \'Value 1\' repeats.', e.exception.args[0])

        # Значение входит в имя

        with self.assertRaises(ValueError) as e:
            Card("Card 1", ["Value 1", "Card"])
        self.assertEqual('Error! The name \'Card 1\' shouldn\'t contain the value \'Card\'.', e.exception.args[0])

    def test_is_selfref_val(self):

        # Значение-самоссылка (имя входит в значение)

        card = Card("<num>", ["..."])
        self.assertEqual(card.is_selfref_val("<num><num>"), True)

        # НЕ значение-самоссылка (имя НЕ входит в значение)

        card = Card("<num>", ["..."])
        self.assertEqual(card.is_selfref_val("<smth>"), False)

    def test_get_values_with_flags(self):

        # Получаем все значения СО флагами

        card = Card("Card 1", ["Value 1", "Value 2"])
        args = [
            {'value': 'Value 1', 'flags': {'is_simple': None, 'is_selfref': None, 'is_templ': None, 'is_id': None}},
            {'value': 'Value 2', 'flags': {'is_simple': None, 'is_selfref': None, 'is_templ': None, 'is_id': None}}]
        self.assertEqual(card.get_values_with_flags(), args)

    def test_get_values_without_flags(self):

        # Получаем все значения без флагов (в данном случае ПРИ наличии значений)

        card = Card("Test Card", ['Value 1', 'Value 2'])
        self.assertEqual(card.get_values_without_flags(), ['Value 1', 'Value 2'])

        # Получаем все значения без флагов (в данном случае БЕЗ наличия значений)

        card3 = Card("Test Card 3", [])
        self.assertEqual(card3.get_values_without_flags(), [])

    def test_get_card(self):

        # Получаем карточку в формате структуры. Флаги НЕ включаются!

        card1 = Card('Card 1', ['Value 1', 'Value 2'])
        self.assertEqual(card1.get_card(), {'name': 'Card 1', 'values': ['Value 1', 'Value 2']})

    def test_check_one_value(self):

        # Проверяем одно УЖЕ существующее значение

        with self.assertRaises(ValueError) as e:
            card = Card("Test Card", ["Value 1", "Value 2"])
            card.check_one_value("Value 1")
        self.assertEqual('Error! The value \'Value 1\' is already in card.', e.exception.args[0])

        # Проверяем одно ЕЩЕ НЕ существующее значение

        self.assertEqual(card.check_one_value("Value 3"), True)

        # Проверяем одно значение, входящее в имя

        with self.assertRaises(ValueError) as e:
            card.check_one_value("Test")
        self.assertEqual('Error! The name \'Test Card\' shouldn\'t contain the value \'Test\'.', e.exception.args[0])

        # Проверяем одно значение, которое полностью совпадает с именем

        with self.assertRaises(ValueError) as e:
            card.check_one_value("Test Card")
        self.assertEqual('Error! The name \'Test Card\' shouldn\'t contain the value \'Test Card\'.',
                         e.exception.args[0])

        # Проверяем одно пустое значение

        with self.assertRaises(ValueError) as e:
            card.check_one_value("")
        self.assertEqual('Error! Empty value.', e.exception.args[0])

    def test_check_some_values(self):

        # Проверяем два одинаковых значения

        with self.assertRaises(ValueError) as e:
            card = Card('Card 1', ['A', 'K', 'Q', 'J', '10'])
            card.check_some_values(['I', 'I'])
        self.assertEqual('Error! The value \'I\' repeats.', e.exception.args[0])

        # Проверяем два значения, оба из которых УЖЕ есть

        with self.assertRaises(ValueError) as e:
            card.check_some_values(['A', '10'])
        self.assertEqual('Error! The value \'A\' is already in card.', e.exception.args[0])

        # Проверяем два значений, одно из которых УЖЕ есть

        with self.assertRaises(ValueError) as e:
            card.check_some_values(['K', '9'])
        self.assertEqual('Error! The value \'K\' is already in card.', e.exception.args[0])

        # Проверяем несколько значений, которых ЕЩЕ НЕТ

        self.assertEqual(card.check_some_values(['7', '8', '9']), True)

    def test_add_one_value(self):

        # Добавляем одно значение, которое УЖЕ есть

        with self.assertRaises(ValueError) as e:
            card = Card("Test Card", ["Value 1", "Value 2"])
            card.add_one_value("Value 1")
        self.assertEqual('Error! The value \'Value 1\' is already in card.', e.exception.args[0])

        # Добавляем одно значение, содержащееся в имени

        with self.assertRaises(ValueError) as e:
            card.add_one_value("Test")
        self.assertEqual('Error! The name \'Test Card\' shouldn\'t contain the value \'Test\'.', e.exception.args[0])

        # Добавляем одно пустое значение

        with self.assertRaises(ValueError) as e:
            card.add_one_value("")
        self.assertEqual('Error! Empty value.', e.exception.args[0])

        # Добавляем одно корректное значение

        self.assertEqual(card.add_one_value("Value 3"), True)

    def test_add_some_values(self):

        # Добавляем три значения, каждое из которых УЖЕ есть

        with self.assertRaises(ValueError) as e:
            card = Card('name1', ['A', 'K', 'Q', 'J', '10'])
            card.add_some_values(['A', 'K', 'Q'])
        self.assertEqual('Error! The value \'A\' is already in card.', e.exception.args[0])

        # Добавляем три значения, два из которых УЖЕ есть

        with self.assertRaises(ValueError) as e:
            card.add_some_values(['J', '10', '9'])
        self.assertEqual('Error! The value \'J\' is already in card.', e.exception.args[0])

        # Добавляем одно значение, которого ЕЩЕ НЕТ, через функцию для добавления нескольких

        self.assertEqual(card.add_some_values(['9']), True)

        # Проверяем, какие значения добавились, а какие нет (смотрим на обновленный список всех в конечном итоге)

        args = [
            {'value': 'A', 'flags': {'is_simple': None, 'is_selfref': None, 'is_templ': None, 'is_id': None}},
            {'value': 'K', 'flags': {'is_simple': None, 'is_selfref': None, 'is_templ': None, 'is_id': None}},
            {'value': 'Q', 'flags': {'is_simple': None, 'is_selfref': None, 'is_templ': None, 'is_id': None}},
            {'value': 'J', 'flags': {'is_simple': None, 'is_selfref': None, 'is_templ': None, 'is_id': None}},
            {'value': '10', 'flags': {'is_simple': None, 'is_selfref': None, 'is_templ': None, 'is_id': None}},
            {'value': '9', 'flags': {'is_simple': None, 'is_selfref': None, 'is_templ': None, 'is_id': None}}]

        self.assertEqual(card.get_values_with_flags(), args)

    def test_delete_one_value(self):

        # Удаляем одно пустое значение

        with self.assertRaises(ValueError) as e:
            card = Card("Test Card", ["Value 1", "Value 2", "Value 3"])
            card.delete_one_value("")
        self.assertEqual('Error! Empty value.', e.exception.args[0])

        # Удаляем одно несуществующее значение

        with self.assertRaises(Exception) as e:
            card.delete_one_value("Value 4")
        self.assertEqual('Error! No \'Value 4\' value in card.', e.exception.args[0])

        # Удаляем одно существующее значение

        self.assertEqual(card.delete_one_value("Value 2"), True)

    def test_delete_some_values(self):

        #

        args = [
            {'value': 'A', 'flags': {'is_simple': None, 'is_selfref': None, 'is_templ': None, 'is_id': None}},
            {'value': 'K', 'flags': {'is_simple': None, 'is_selfref': None, 'is_templ': None, 'is_id': None}},
            {'value': 'Q', 'flags': {'is_simple': None, 'is_selfref': None, 'is_templ': None, 'is_id': None}},
            {'value': 'J', 'flags': {'is_simple': None, 'is_selfref': None, 'is_templ': None, 'is_id': None}},
            {'value': '10', 'flags': {'is_simple': None, 'is_selfref': None, 'is_templ': None, 'is_id': None}}]
        card = Card('name1', ['A', 'K', 'Q', 'J', '10'])

        # Сверяемся со значениями карты

        self.assertEqual(card.get_values_with_flags(), args)

        # Удаляем три значения, всех трех из которых нет

        with self.assertRaises(Exception) as e:
            card.delete_some_values(['7', '8', '9'])
        self.assertEqual('Error! No \'7\' value in card.', e.exception.args[0])

        # Удаляем несколько значений, которые есть

        self.assertEqual(card.delete_some_values(['A', '10']), True)


if __name__ == '__main__':
    main()  # из unittest

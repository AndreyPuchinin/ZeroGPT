import unittest
from card_class import Card


class TestCard(unittest.TestCase):
    """
    Тип def get_values() изменен со списка со значениями на список со значниями и флагами!
    Из-за этого тесты могут работать некорректно.
    В будущем ИЗМЕНИТЬ тесты с Юниттестов на Доктесты!!! Данный класс удалить!!!
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    Данный класс полностью перенесен в доктесты класса Card
    Теперь его можно не импортировать
    Однако я решил оставить этот класс в памяти проекта на всякий случай
    """

    def test_check_one_value(self):
        """
                Эта функция уже полностью перенесена в Card.
                Первичный тест: прошел успещно.
                Общий тест после перенесения всех тестовых функций в Card: прошел успещно.
        """
        card = Card("Test Card", ["Value 1", "Value 2"])
        self.assertFalse(card.check_one_value("Value 1"))
        self.assertFalse(card.check_one_value("Value 2"))
        self.assertTrue(card.check_one_value("Value 3"))
        self.assertFalse(card.check_one_value("Test"))
        self.assertFalse(card.check_one_value(""))

    def test_check_some_values(self):
        """
                Эта функция уже полностью перенесена в Card.
                Первичный тест: прошел успещно.
                Общий тест после перенесения всех тестовых функций в Card: прошел успещно.
        """
        card = Card('name1', ['A', 'K', 'Q', 'J', '10'])

        self.assertEqual(card.check_some_values(['A', '10']), [False, False])
        self.assertEqual(card.check_some_values(['K', '9']), [False, True])
        self.assertEqual(card.check_some_values(['7', '8', '9']), [True, True, True])

    def test_add_one_value(self):
        """
                Эта функция уже полностью перенесена в Card.
                Первичный тест: прошел успещно.
                Общий тест после перенесения всех тестовых функций в Card: прошел успещно.
        """
        card = Card("Test Card", ["Value 1", "Value 2"])
        self.assertFalse(card.add_one_value("Value 1"))
        self.assertFalse(card.add_one_value("Value 2"))
        self.assertTrue(card.add_one_value("Value 3"))
        self.assertFalse(card.add_one_value("Test"))
        self.assertFalse(card.add_one_value(""))

    def test_add_some_values(self):
        """
                Эта функция уже полностью перенесена в Card.
                Первичный тест: прошел успещно.
                Общий тест после перенесения всех тестовых функций в Card: прошел успещно.
        """
        card = Card('name1', ['A', 'K', 'Q', 'J', '10'])

        self.assertEqual(card.add_some_values(['A', 'K', 'Q']), [False, False, False])
        self.assertEqual(card.add_some_values(['J', '10', '9']), [False, False, True])
        self.assertEqual(set(card.get_values_with_flags()), {'A', 'K', 'Q', 'J', '10', '9'})

    def test_delete_one_value(self):
        """
                Эта функция уже полностью перенесена в Card.
                Первичный тест: прошел успещно.
                Общий тест после перенесения всех тестовых функций в Card: прошел успещно.
        """
        card = Card("Test Card", ["Value 1", "Value 2", "Value 3"])
        card.delete_one_value("Value 2")
        self.assertNotIn("Value 2", [value['value'] for value in card.values])

    def test_delete_some_values(self):
        """
                Эта функция уже полностью перенесена в Card.
                Первичный тест: прошел успещно.
                Общий тест после перенесения всех тестовых функций в Card: прошел успещно.
        """
        card = Card('name1', ['A', 'K', 'Q', 'J', '10'])

        self.assertEqual(card.delete_some_values(['A', '10']), [True, True])
        self.assertEqual(card.get_values_with_flags(), ['K', 'Q', 'J'])
        self.assertEqual(card.delete_some_values(['7', '8', '9']), [False, False, False])

    def test_exchange_value(self):
        """
               Эта функция уже полностью перенесена в Card.
               Первичный тест: прошел успещно.
               Общий тест после перенесения всех тестовых функций в Card: прошел успещно.
        """
        card = Card("Test Card", ["Value 1", "Value 2", "Value 3"])
        card.exchange_value("Value 2", "Value 4")
        self.assertNotIn("Value 2", [value['value'] for value in card.values])
        self.assertIn("Value 4", [value['value'] for value in card.values])


if __name__ == '__main__':
    unittest.main()
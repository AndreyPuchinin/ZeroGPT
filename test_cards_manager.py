import unittest
from card_class import Card


class TestCard(unittest.TestCase):

    def test_init(self):
        card = Card("test", ["value1", "value2"])
        self.assertEqual(card.name, "test")
        self.assertEqual(card.values, ["value1", "value2"])

    def test_get_values(self):
        card = Card("test", ["value1", "value2"])
        self.assertEqual(card.get_values(), ["value1", "value2"])

    def test_check_one_value(self):
        card = Card("test", ["value1", "value2"])
        self.assertFalse(card.check_one_value("value1"))
        self.assertFalse(card.check_one_value("test"))
        self.assertTrue(card.check_one_value("value3"))

    def test_check_some_values(self):
        card = Card("test", ["value1", "value2"])
        self.assertEqual(card.check_some_values(["value1", "value2", "value3"]), [False, False, True])

    def test_add_one_value(self):
        card = Card("test", ["value1", "value2"])
        self.assertTrue(card.add_one_value("value3"))
        self.assertEqual(card.values, ["value1", "value2", "value3"])
        self.assertFalse(card.add_one_value("value1"))
        self.assertFalse(card.add_one_value("test"))
        self.assertFalse(card.add_one_value(""))

    def test_add_some_values(self):
        card = Card("test", ["value1", "value2"])
        self.assertEqual(card.add_some_values(["value2", "value3", "value1", "test", ""]), [False, True, False, False, False])
        self.assertEqual(card.values, ["value1", "value2", "value3"])

    def test_delete_one_value(self):
        card = Card("test", ["value1", "value2"])
        self.assertTrue(card.delete_one_value("value1"))
        self.assertEqual(card.values, ["value2"])
        self.assertFalse(card.delete_one_value("value3"))

    def test_delete_some_values(self):
        card = Card("test", ["value1", "value2"])
        self.assertEqual(card.delete_some_values(["value2", "value3", "value1", ""]), [True, False, True, False])
        self.assertEqual(card.values, [])

    def test_exchange_value(self):
        card = Card("test", ["value1", "value2"])
        self.assertTrue(card.exchange_value("value1", "value3"))
        self.assertEqual(set(card.values), {"value3", "value2"})
        self.assertFalse(card.exchange_value("value1", "test"))
        self.assertFalse(card.exchange_value("value1", ""))

import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame:

    def setUp(self):
        self.card = Card('hearts', 6)
        self.ace = Card('spades', 1)
        self.cards = (self.card, self.ace)
    
    def test_card_has_suit(self):
        self.assertEqual('hearts', self.card.suit)

    def test_card_has_value(self):
        self.assertEqual(6, self.card.value)

    def test_check_for_ace_true(self):
        result = check_for_ace(self.ace)
        self.assertEqual(True, result)

    def test_check_for_ace_false(self):
        result = check_for_ace(self.card)
        self.assertEqual(False, result)

    def test_highest_card_card(self):
        result = highest_card(self.card, self.ace)
        self.assertEqual('card', result)

    def test_highest_card_card2(self):
        result = highest_card(self.ace, self.card)
        self.assertEqual('card2', result)

    def test_cards_total(self):
        result = cards_total(self.cards)
        self.assertEqual("You have a total of 7", result)

    



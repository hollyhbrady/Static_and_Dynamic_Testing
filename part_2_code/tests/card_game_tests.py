import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.h6 = Card('hearts', 6)
        self.ace = Card('spades', 1)
        self.hand = (self.h6, self.ace)
        self.game = CardGame()
    
    def test_card_has_suit(self):
        self.assertEqual('hearts', self.h6.suit)

    def test_card_has_value(self):
        self.assertEqual(6, self.h6.value)

    def test_check_for_ace_true(self):
        result = self.game.check_for_ace(self.ace)
        self.assertEqual(True, result)

    def test_check_for_ace_false(self):
        result = self.game.check_for_ace(self.h6)
        self.assertEqual(False, result)

    def test_highest_card_card1(self):
        result = self.game.highest_card(self.h6, self.ace)
        self.assertEqual(self.h6, result)

    def test_highest_card_card2(self):
        result = self.game.highest_card(self.ace, self.h6)
        self.assertEqual(self.h6, result)

    def test_cards_total(self):
        result = self.game.cards_total(self.hand)
        self.assertEqual("You have a total of 7", result)

    



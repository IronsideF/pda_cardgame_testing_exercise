import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.cardgame = CardGame()
        self.card1 = Card('Spades', 1)
        self.card2 = Card('Hearts', 10)
        self.card3 = Card('Clubs', 7)
        self.card4 = Card('Diamonds', 3)
        self.cards = [self.card1, self.card2, self.card3, self.card4]

    def test_can_identify_ace(self):
        self.assertEqual(self.cardgame.check_for_ace(self.card1), True)
    
    def test_can_identify_not_ace(self):
        self.assertEqual(self.cardgame.check_for_ace(self.card2), False)

    def test_can_return_high_card(self):
        self.assertEqual(self.cardgame.highest_card(self.card2, self.card3), self.card2)
    
    def test_can_return_total_card_value(self):
        self.assertEqual(self.cardgame.cards_total(self.cards), 'You have a total of 21')
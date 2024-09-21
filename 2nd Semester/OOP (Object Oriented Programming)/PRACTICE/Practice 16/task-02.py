import random

class PlayingCard:
    def __init__(self, value, suit, type, color):
        self.value = value
        self.suit = suit
        self.type = type
        self.color = color
    def __str__(self):
        return f'{self.value} {self.suit} {self.type} {self.color}'
     
class Hand:
    def __init__(self):
        self.card1 = PlayingCard(Hand.random_card_value(), Hand.random_type_color())
        self.card2 = PlayingCard(Hand.random_card_value(), Hand.random_type_color())
        self.card3 = PlayingCard(Hand.random_card_value(), Hand.random_type_color())
        self.card4 = PlayingCard(Hand.random_card_value(), Hand.random_type_color())
        self.card5 = PlayingCard(Hand.random_card_value(), Hand.random_type_color())
    def __str__(self):
        pass
    def random_card_value():
        val = random.randint(1,12)
        if val == 1:
            return val, 'ACE'
        elif val == 11:
            return val, 'JACK'
        elif val == 12:
            return val ,"QUEEN"
        elif val == 13:
            return val, 'KING'
        else:
            return val, str(val)

    def random_type_color():
        val = random.randint(1,4)
        if val == 1:
            return 'SPADES', 'BLACK'
        elif val == 2:
            return 'CLUBS', 'BLACK'
        elif val == 3:
            return 'DIAMONDS', 'RED'
        elif val == 4:
            return 'HEARTS', 'RED'

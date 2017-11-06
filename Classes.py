class Card:

    """playing card object where numeric rank, suit and blackjack values are stored"""

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.ranks = [None,"Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
        self.suits = {"d": "Diamonds",
                   "c": "Clubs",
                   "h": "Hearts",
                   "s": "Spades"}

    def getRank(self):
        """returns the rank of the card"""
        return self.rank

    def getSuit(self):
        return self.suits.get(self.suit)

    def bjValue(self):
        rankOfCard = self.ranks[self.rank]
        if rankOfCard in range(1,12):
            self.value = self.rank

        elif rankOfCard == "Ace":
            self.value = 1

        elif rankOfCard == "Jack" or rankOfCard == "Queen" or rankOfCard == "King":
            self.value = 10


        return self.value


    def __str__(self):

        return "%s of %s" % (self.ranks[self.rank], self.suits.get(self.suit))

class Hand:
    def __init__(self):
        self.hand=[]
    def addCard(self,x):
        self.hand.append(x)
    def bust(self):
        print()
    def resethand(self):
        self.hand = []
class dhand(Hand):
    pass

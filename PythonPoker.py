import random
#Variables --------------------------------------------------------
Values = ["Ace","2","3","4","5","6","7","8","9","10","JACK","QUEEN","KING"]
Suits = ["Clubs","Spades","Hearts","Diamonds"]
Deck = []

#Tests --------------------------------------------------------

def CardCountTest():
    ExpectedDeckLength = 52
    ActualLenth = len(Deck)

    if ExpectedDeckLength == ActualLenth:
        print("Deck has correct amount of cards")
    else:
        print("Test Fail")


#Classes --------------------------------------------------------

class Card(object):
    """Card object which contains card value and suit"""
    def __init__(self,Value,Suit):
        super(Card, self).__init__()
        self.Value = Value
        self.Suit = Suit



#Functions --------------------------------------------------------

def PopulateDeck():
    for Value in Values:
        for Suit in Suits:
            NewCard = Card(Value,Suit)
            Deck.append(NewCard)


def ShuffleDeck(Deck):
    for i in range(0,5000):
        CurrentCard = Card(Deck[0].Value,Deck[0].Suit)
        Deck.pop(0)
        NewIndex = (random.randrange(52))
        Deck.insert(NewIndex,CurrentCard)

def PrintDeckOrder(Deck):
    for Card in Deck:
        print(Card.Value,"of",Card.Suit)

#-------------------------------------------------------- Main --------------------------------------------------------

def Main():
        #Populating deck of cards
        PopulateDeck()
        ShuffleDeck(Deck)
        PrintDeckOrder(Deck)


#Calling main function
Main()

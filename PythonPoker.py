import random
#Variables --------------------------------------------------------
Values = ["Ace","2","3","4","5","6","7","8","9","10","JACK","QUEEN","KING"]
Suits = ["Clubs","Spades","Hearts","Diamonds"]
Deck = []
Players = []
TableCards = []

#Tests --------------------------------------------------------

#Ensures deck is correct size
def CardCountTest():
    ExpectedDeckLength = 52
    ActualLenth = len(Deck)

    if ExpectedDeckLength == ActualLenth:
        print("Deck has correct amount of cards")
    else:
        print("Test Fail")


#Classes --------------------------------------------------------

#Self explanitory
class Card(object):
    """Card object which contains card value and suit"""
    def __init__(self,Value,Suit):
        super(Card, self).__init__()
        self.Value = Value
        self.Suit = Suit


#PLayer class which stores hand, combinations and card strength.
class Player(object):
    """Class used to store players hand"""

    def __init__(self,Name):
        super(Player, self).__init__()
        self.Hand = []
        self.Name = Name
        self.CardCombinations = []
        Self.BestHandStrength = 0




#Functions --------------------------------------------------------

#Creates cards and appends them to deck
def PopulateDeck():
    for Value in Values:
        for Suit in Suits:
            NewCard = Card(Value,Suit)
            Deck.append(NewCard)

#Selects the first item in the deck and places it at a random index 1000 times.
def ShuffleDeck(Deck):
    for i in range(0,5000):
        CurrentCard = Card(Deck[0].Value,Deck[0].Suit)
        Deck.pop(0)
        NewIndex = (random.randrange(52))
        Deck.insert(NewIndex,CurrentCard)

#Used to print the oder of the deck to ensure the order is random
def PrintDeckOrder(Deck):
    for Card in Deck:
        print(Card.Value,"of",Card.Suit)

#Instanciates player classes for dealer and current player
def CreatePlayers():
    Dealer = Player("Dealer")
    Players.append(Dealer)
    CurrentPlayer = Player("Alex")
    Players.append(CurrentPlayer)

#Deals two cards to each player and deals 5 cards to the table
def Deal():
    for i in range(0,len(Players)):
        for x in range(0,2):
            CurrentCard = Deck[0]
            Players[i].Hand.append(CurrentCard)
            Deck.pop(0)

    for z in range(0,5):
        CurrentCard = Deck[0]
        TableCards.append(CurrentCard)
        Deck.pop(0)

#Print the Value and Suit of cards held by all Player Classes
def PrintPlayerHands():
    for Player in Players:
        print(Player.Name)
        for Card in Player.Hand:
            print(Card.Value,"of", Card.Suit)

#Prints all cards in a passed list alongside source of list
def PrintCards(Source,ListOfCards):
    print(Source)
    for Card in ListOfCards:
        print(Card.Value,"of", Card.Suit)


#Each player will have a number of possible hands made up two held cards and 5 table cards. This function records all 5 card combinations as a result of moving both cards individually acrosss the list of table cards.
def GetSingleCardChangeCombinations(TableCards, Players):
    for Player in Players:
        Player.CardCombinations.append(TableCards)
        for PlayerCard in Player.Hand:
            CurrentCombination = []
            for i in range(0,len(TableCards)):
                for Card in TableCards:
                    CurrentCombination.append(Card)
                CurrentCombination.pop(i)
                CurrentCombination.insert(i,PlayerCard)
                Player.CardCombinations.append(CurrentCombination)
                CurrentCombination = []
    GetDoubleCardChangeCombinations(TableCards, Players)


#Records all possible combinations as a result of adding both player cards into the 5 table cards. The maximum size of a single hand to be evaluated is 5.
def GetDoubleCardChangeCombinations(TableCards, Players):
    for Player in Players:




















#-------------------------------------------------------- Main --------------------------------------------------------

def Main():
        #Populating deck of cards
        PopulateDeck()
        ShuffleDeck(Deck)
        CreatePlayers()
        Deal()
        GetSingleCardChangeCombinations(TableCards,Players)



#Calling main function
Main()

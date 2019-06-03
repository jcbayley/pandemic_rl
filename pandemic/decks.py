import random

class InfectionDeck:
    
    def __init__(self,parent):
        """
        Class for the infections deck
        
        args
        -----------
        parent: Pandemic
            parent pandemic class
        """
        self._parent = parent
        
        # add citys to the deck
        self.deck = self._parent.cities.keys()
        
        # set up the discard pile
        self.discard = []
        
        #shuffle the deck
        random.shuffle(deck)
        
    def turn(self):
        """
        complete a turn of the infection deck
        """
        
        # select 3 cities from the top of the deck
        selected = []
        for cty in range(3):
            selected.append(self.deck.pop(cty))
        
        # infect each of these cities
        for cty in selected:
            self._parent.cities[cty].infect(color = self._parent.cities[cty].color)
        
        # add these cities to the discard pile
        self.discard.extend(selected)
            
    def shuffle_discard(self):
        """
        shuffle the discard and add to top of deck
        """
        #shuffle discard
        random.shuffle(discard)
        
        # add to deck
        for i in discard:
            self.deck.insert(0,i)
        
        #empty the discard deck
        self.discard = []
            


class PlayerDeck:
    
    def __init__(self,parent):
        """
        Class for the player deck
        
        args
        -----------
        parent: Pandemic
            parent pandemic class
        """
        self._parent = parent
        
        # add the cities to the player deck
        self.deck = self._parent.cities
        
        # set the order of the deck so card can be drawn from the to
        # python dictionaries are not ordered, also need to add epidemic card in here
        self.order = self.deck.keys()
        
        # setup the player deck discard
        self.discard = {}
        
    def shuffle(self):
        """
        shuffle the player deck
        """
        #shuffle the deck
        random.shuffle(self.order)
        
    def draw(self,player):
        """
        draw a card from the deck for a given player
        args
        ------
        player: string
            name of the player to draw a card
        """
        # remove name from first card of order list
        name = self.order.pop(0)
        #remove this card from the dekc dictionary
        val = self.deck.pop(name)
        # add this card the the players hand
        self._parent.players[player].hand[name] = val
        
        del name,val

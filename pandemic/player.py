
class Player:
    
    def __init__(self,name,parent):
        """
        General class for player
        """
        self.name = name
        self._parent = parent
        
        #defualt start location is atlanta
        self.location = "Atlanta"
        
        #number of actions per turn is 0
        self.actions = 0
        
        # setup hand as empty dictionary
        self.hand = {}
        
    def end_turn(self):
        """
        end turn
        """
        # at end of turn reset the actions to zero
        self.actions = 0
        
        #self._parent.infect
        
    def increase_action(self):
        """
        increase the number of actions
        """
        self.actions += 1
        # if the number of actions is 4 then the turn ends
        if self.actions == 4:
            self.end_turn()
    
    def get_player_card(self):
        """
        draw a card from the player deck
        """
        self._parent.player_deck.draw(self.name)
    
    def move(self,city):
        """
        move to another city, maximum moves is number of actions left
        
        args
        ---------
        city: string
            city name to move to
        """
        
        # find the shortest path to this city on the board
        shortest_path = nx.shortest_path(self._parent.board,source=self.location,target=city)
        
        # if the city is furhter awaw than th number of ations left then raise error
        if len(shortest_path) > 4 - self.actions :
            raise Exception("Cannot move here: only {} actions left".format(self.actions))
        else:
            # set player location to this city adn increase the actions by number of moves
            self.location = city
            for i in range(len(shortest_path)):
                self.increase_action()
    
    def direct_fly(self,city):
        """
        directly fly to a city if city in hand
        args
        ---------
        city: string
            city to fly to
        """
        if city in self.hand:
            self.location = city
            #remove city from hand and add it to the player deck discard pile
            card = self.hand.pop(city)
            self._parent.player_deck.discard[card.name] = card
            # increase number of actions taken
            self.increase_action()
        else:
            raise Exception("You do not have this City")
    
    def charter_fly(self,city):
        """
        fly to any other city if you have the card of the city you are in
        args
        -------
        city: string
            which city to move to
        """
        if self.location in self.hand.keys():
            #if you have the current location card change your location
            self.location = city
            # remove this city from you hand and add to the player deck discard
            card = self.hand.pop(self.location)
            self._parent.player_deck.discard[card.name] = card
            self.increase_action()
    
    def shuttle_fly(self,city):
        """
        if you are in a city with a research station fly to any other city with a research station
        args
        -----------
        city: string
            which city to fly to
        """
        if self._parent.citys[self.location].has_research_station == True and self._parent.citys[city].has_research_station:
            self.location = city
            self.increase_action()
            
    def build_research_station(self,city=None):
        """
        build a research station in the city which you are in  
        """
        if self.location in self.hand:
            # check if all research stations have been used
            if self._parent.research_stations !=0:
                if self._parent.cities[self.location].has_research_station:
                    raise Exception("This city already has a research station")
                # add research station to current city
                self._parent.cities[self.location].has_research_station = True
                self._parent.research_stations -= 1
                self.increase_action()
            else:
                # if all research stations have been used up, take one from another city, where city is deifed
                if city is not None:
                    self._parent.citys[city].has_research_station = False
                    self._parent.citys[self.location].has_research_station = True
                    self.increase_action()
                
                else:
                    raise Exception("Please define a city to take the research station from")
    
    def treat_disease(self,color=None):
        """
        treat a disease in your current city
        
        args
        ----------
        color: string (optional)
            treat the current city of cubes with this color (defualt color is the color of the city you are in)
        """
        # set color if not defined
        if color is None:
            color = self._parent.cities[self.location].color

        self._parent.cities[self.location].treat(color)
        self.increase_action()
    
    def discover_cure(self,color):
        """
        discover a cure for a given color
        
        args
        ---------
        color: string
            color to discover the cure for
        """
        
        # dont cure if already cured
        if color in self._parent.cured:
            raise Exception("This disease is already cured")
        
        elif self._parent.cities[self.location].has_research_station:
            # if it has a research station then cure the city
            
            #check if have enough cities of correct color
            
            ctys = {}
            for nm,cty in self.hand.items():
                if cty.type == "city":
                    if cty.color = color:
                        ctys[nm] = cty
                        
            num_color = len(ctys)
            if num_color >= 5:
                self._parent.cured.append(color)
                card_count = 0
                while card_count < 5:
                    for nm,card in ctys.items():
                        crd = self.hand.pop(nm)
                        self._parent.player_deck.discard[crd.name] = crd 
                        card_count += 1
                self.increase_action()
        else:
            raise Exception("This city does not have a research station")
    
    def share_knowledge(self,player,direction="give"):
        
        if self.location in self.hand:
            if self.location == self._parent.players[player].location:
                if direction == "give":
                    crd = self.hand.pop(self.location)
                    self.players[player].hand[crd.name] = crd
                    self.increase_action()
                elif direction == "take":
                    crd = self.players[player].hand.pop(self.location)
                    self.hand[crd.name] = crd
                    self.increase_action()
            else:
                raise Exception("Not in same location as other player")
        else:
            raise Exception("You do not have the city card of your current location")
    
    def skip(self):
        
        self.end_turn()
        
    def play_card(self,card):
        
        if card in self.hand.keys():
            crd = self.hand.pop(card)
            crd.play()

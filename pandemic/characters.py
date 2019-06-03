from player import Player

class Scientist(Player):
    
    def __init__(self,name, parent):
        
        self._parent = parent 
        
        self.name = name
        
    def discover_cure(self,color):
        
        if color in self._parent.cured:
            raise Exception("This disease is already cured")
        
        elif self._parent.cities[self.location].has_research_station:
            
            ctys = {}
            for nm,cty in self.hand.items():
                if cty.type == "city":
                    if cty.color = color:
                        ctys[nm] = cty
                        
            num_color = len(ctys)
            if num_color >= 4:
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
            
            
class Medic(Player):
    
    def __init__(self,name,parent):
        
        self._parent = parent 
        
        self.name = name
        
class Dispatcher(Player):
    
    def __init__(self,parent):
        
        self._parent = parent 
        
        self.name = name
        
class OperationsExpert(Player):
    
    def __init__(self,parent):
        
        self._parent = parent 
        
        self.name = name
        
class Researcher(Player):
    
    def __init__(self,parent):
        
        self._parent = parent 
        
        self.name = name
        
class QuarantineSpecialist(Player):
    
    def __init__(self,parent):
        
        self._parent = parent 
        
        self.name = name
        
class ContingencyPlanner(Player):
    
    def __init__(self,parent):
        
        self._parent = parent 
        
        self.name = name

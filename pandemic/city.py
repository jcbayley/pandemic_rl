
class City:
    
    def __init__(self, parent):
        """
        City class to be used in the infections deck and the player deck
        
        args
        -----------
        parent: Pandemic
            parent pandemic class
        """
        # set up citys name color and connections
        self.connections = None
        self.name = None
        self.color = None
        self.type = "city"
        self.coordinates = (0,0) 
        
        self._parent = parent
        
        #self.red_infect = 0
        #self.blue_infect = 0
        #self.black_infect = 0
        #self.yellow_infect = 0
        
        # set up the infections cubes for this city
        self.infections = []
        self.tot_infection_number = 0
        
        # check if city has a research station
        self.has_research_station = False
        
    def outbreak(self,color):
        """
        make this city outbreak
        
        args
        ------
        color: string
            which color outbreaks
        """
        
        # infect each of the citys this is connected to 
        for cty in connections:
            self._parent.cities[cty].infect(color)
            
        # increases the number of outbreaks on the pandemic board (i.e. increase counter etc)
        self._parent.outbreak()
        
    def infect(self,color):
        """
        Infect a city with a certain disease color
        
        args
        -------------
        color: string
            which color to infect with
        """
        #cur_value = getattr(self, "{}_infect".format(color))
        #setattr(self, "{}_infect".format(color), cur_value + 1)
        
        #parent_cur_value = getattr(self._parent, "{}_disease".format(color))
        #setattr(self._parent, "{}_disease".format(color), parent_cur_value - 1)
        
        # add this color sube to the infections of this city
        self.infections.append(color)
        # remove this infection color from the set of cubes on the board
        self._parent.diseases.remove(color)
        
        # if the disease cubes of a certain color is 0 you have lost the game
        if self._parent.diseases.count(color) == 0:
            self._parent.lose("Run out of infection cubes")
           
        # increase this citys infection number
        self.tot_infection_number += 1
        
        # if the total number of infection cubes on this city is greater than 3 outbreak
        if self.tot_infection_number > 3:
            self.outbreak(color)
            
    def treat(self,color):
        """
        treat an infection of a city
        
        args
        --------
        color: string
            which color to treat
        """
        
        # if this disease color is already cured remove all cubes of this color from this city and add back to pool of disease cubes
        if color in self._parent.cured:
            while color in self.infections:
                self.infections.remove(color)
                self._parent.diseases.append(color)
        else:
            # if it is not cured just remove one cube and add to pool
            self.infections.remove(color)
            self._parent.diseases.append(color)
    
        

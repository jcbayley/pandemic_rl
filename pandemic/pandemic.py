from __future__ import absolute_import
import configparser 
import json
import networkx as nx
import matplotlib.pyplot as plt
from city import City

class Pandemic:
    
    def __init__(self):
        
        self.cities = {}
        self.connections = []
        
        self.read_cities()
        
        self.infection_rate_ind = 0
        self.infection_rate = 2
        self.outbreaks = 0
        
        self.cured = []
        self.eradicated = []
        
        self.research_stations = 5
        
        self.diseases = ["red"]*24 + ["blue"]*24 + ["black"]*24 + ["yellow"]*24
        self.red_disease = self.diseases.count("red")
        self.blue_disease = self.diseases.count("blue")
        self.black_disease = self.diseases.count("black")
        self.yellow_disease = self.diseases.count("yellow")
        
        self.players = []
    
    def add_city(self, city):
        
        """
        Add a city to the game.
        Parameters
        ------------
        city: City
            city which is to be added to the game
        """
        if not city.name in self.cities.keys():
            self.cities[city.name] = city

    def outbreak(self):
        
        infection_rates = [2,2,2,3,3,4,4]
        
        self.infection_rate_ind += 1
        self.infection_rate = infection_rates[self.infection_rate_ind]
        
        self.outbreaks += 1
        
    def lose(self,msg):
    
        print("You have lost the game because: {}".format(msg))
        
        return 0
        
    def read_cities(self,filepath = "../data/connections.ini"):
        
        cp = configparser.ConfigParser()
        cp.read(filepath)
        
        for key,vals in cp.items():
            temp_city = City(self)
            temp_city.name = key
            for val in vals:
                ent = cp.get(key,val)
                if val == "connections":
                    ent = [i.strip(" ") for i in ent.strip("[]").strip("]").split(",")]
                setattr(temp_city,val,ent)
                self.add_city(temp_city)
            del temp_city
            
    def create_graph(self):
        
        self.board = nx.MultiGraph()
        
        connections = []
        
        for city in self.cities.values():
            
            self.board.add_node(city.name, data = city)
            
            for con in city.connections:
                if (city.name,con) in connections or (con,city.name) in connections:
                    continue
                else:
                    self.board.add_edge(city.name,con)
                    connections.append((city.name,con))

                    
    def plot_model(self,figsize = (15,10)):
        """
        pot the model using networkx
        """
        nodes = self.board.nodes()
        labels = {n:n for n in nodes}
        fig, ax = plt.subplots(figsize = figsize)
        pos = nx.spring_layout(self.board)
        ex = nx.draw_networkx_edges(self.board, pos, alpha = 0.2)
        nc = nx.draw_networkx_nodes(self.board, pos, nodelist=nodes, node_size=300)
        lc = nx.draw_networkx_labels(self.board, pos, labels)
        ax.axis('off')

import json
from collections import defaultdict

file=open("Input data\\level1a.json","r")
dict_file=json.load(file)


no_neighbours=dict_file["n_neighbourhoods"]
no_restaurants=dict_file["n_restaurants"]

#neighbours information

neighbours=dict_file["neighbourhoods"]
neighbours_dict=defaultdict(dict)
neighbours_distance=defaultdict(list)
neighbours_quantity=dict()

for neighbour in neighbours:
    neighbours_dict[neighbour]=neighbours[neighbour]

for neighbour in neighbours_dict:
    neighbours_distance[neighbour]=neighbours_dict[neighbour]["distances"]
    neighbours_quantity[neighbour]=neighbours_dict[neighbour]["order_quantity"]


#restaurant inforation

restaurant_dict = dict_file["restaurants"]
restaurant_neighbour_distance=defaultdict(list)
restaurant_restaurant_distance=defaultdict(list)

for restaurant in restaurant_dict:
    restaurant_neighbour_distance[restaurant]=restaurant_dict[restaurant]["neighbourhood_distance"]
    restaurant_restaurant_distance[restaurant]=restaurant_dict[restaurant]["restaurant_distance"]

#vehicles info
    
vehicles_dict=dict_file["vehicles"]
vehicles_starting_point=dict()
vehicles_capacity=dict()

for vehicle in vehicles_dict:
    vehicles_starting_point[vehicle]=vehicles_dict[vehicle]["start_point"]
    vehicles_capacity[vehicle]=vehicles_dict[vehicle]["capacity"]

#for storing each vehicle path 
vehicle_path=defaultdict(dict)

import json
from collections import defaultdict

file=open("Input data\\level0.json","r")
dict_file=json.load(file)


no_neighbours=dict_file["n_neighbourhoods"]
no_restaurants=dict_file["n_restaurants"]

#neighbours information

neighbours=dict_file["neighbourhoods"]
neighbours_dict=defaultdict(dict)
neighbours_distance=defaultdict(list)

for neighbour in neighbours.keys():
    neighbours_dict[neighbour]=neighbours[neighbour]

for neighbour in neighbours_dict.keys():
    neighbours_distance[neighbour]=neighbours_dict[neighbour]["distances"]

#restaurant inforation

restaurant_dict = dict_file["restaurants"]
restaurant_neighbour_distance=defaultdict(list)
restaurant_restaurant_distance=defaultdict(list)

for restaurant in restaurant_dict.keys():
    restaurant_neighbour_distance[restaurant]=restaurant_dict[restaurant]["neighbourhood_distance"]
    restaurant_restaurant_distance[restaurant]=restaurant_dict[restaurant]["restaurant_distance"]

#vehicles info
    
vehicles_dict=dict_file["vehicles"]
vehicles_starting_point=dict()

for vehicle in vehicles_dict.keys():
    vehicles_starting_point[vehicle]=vehicles_dict[vehicle]["start_point"]

#for storing each vehicle path 
vehicle_path=defaultdict(dict)

min_dist_neigh_r0=restaurant_neighbour_distance["r0"].index(min(restaurant_neighbour_distance["r0"]))
min_dist_neigh_r0_str="n"+str(min_dist_neigh_r0)

path_list=["r0"]
path_list.append(min_dist_neigh_r0_str)

#for claculating cost
cost=0
cost+=neighbours_distance[neighbour][min_dist_neigh_r0]

while len(path_list)<=no_neighbours:
    neighbour=path_list[-1]
    neighbour_int=neighbour[1:]
    neighbours_distance[neighbour][int(neighbour_int)]=float('inf')
    min_dist_neigh=neighbours_distance[neighbour].index(min(neighbours_distance[neighbour]))
    min_dist_neigh_str="n"+str(min_dist_neigh)
    while min_dist_neigh_str in path_list and len(path_list)<no_neighbours+1:
        neighbours_distance[neighbour][min_dist_neigh]=float('inf')
        min_dist_neigh=neighbours_distance[neighbour].index(min(neighbours_distance[neighbour]))
        min_dist_neigh_str="n"+str(min_dist_neigh)
    cost+=neighbours_distance[neighbour][min_dist_neigh]
    path_list.append(min_dist_neigh_str)
path_list.append("r0")  

path_dict=dict()

path_dict["path"]=path_list
vehicle_path["vo"]=path_dict
print("Path is ")
for path in vehicle_path:
    print(path,vehicle_path[path])

print("Cost is ",cost)

with open("21pt34_solution\\output_file","w") as outfile:
    json.dump(vehicle_path,outfile)
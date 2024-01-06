import json
from collections import defaultdict

file=open("Input data\\level2b.json","r")
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

vehicle_each_path=defaultdict(list)
visited=[]
count={}
for vehicle in vehicles_capacity:
    count[vehicle]=1
while len(visited)<no_neighbours:
    for vehicle in vehicles_capacity:
        capacity=0
        min_dist_neigh=restaurant_neighbour_distance["r0"].index(min(restaurant_neighbour_distance["r0"]))
        min_dist_neigh_str="n"+str(min_dist_neigh)
        restaurant_neighbour_distance["r0"][min_dist_neigh]=float('inf')
        path_list=["r0"]
        while min_dist_neigh_str in visited:
            min_dist_neigh=restaurant_neighbour_distance["r0"].index(min(restaurant_neighbour_distance["r0"]))
            min_dist_neigh_str="n"+str(min_dist_neigh)
            restaurant_neighbour_distance["r0"][min_dist_neigh]=float('inf')
        capacity+=neighbours_quantity[min_dist_neigh_str]
        path_list.append(min_dist_neigh_str)
        visited.append(min_dist_neigh_str)
        while capacity<=vehicles_capacity[vehicle] and len(visited)<no_neighbours:
            neighbour=path_list[-1]
            neighbour_int=neighbour[1:]
            neighbours_distance[neighbour][int(neighbour_int)]=float('inf')
            min_dist_neigh=neighbours_distance[neighbour].index(min(neighbours_distance[neighbour]))
            min_dist_neigh_str="n"+str(min_dist_neigh)
            flag=1
            while 1:     
                while (min_dist_neigh_str in path_list and len(path_list)<no_neighbours+1) or capacity+neighbours_quantity[min_dist_neigh_str]>vehicles_capacity[vehicle] or min_dist_neigh_str in visited:
                        flag=1
                        neighbours_distance[neighbour][min_dist_neigh]=float('inf')
                        min_dist_neigh=neighbours_distance[neighbour].index(min(neighbours_distance[neighbour]))
                        min_dist_neigh_str="n"+str(min_dist_neigh)
                        min_dist=min(neighbours_distance[neighbour])
                        if min_dist == float('inf'):
                            flag=0
                            break
                if flag==0:
                    break
                if capacity+neighbours_quantity[min_dist_neigh_str]<=vehicles_capacity[vehicle]:
                    capacity+=neighbours_quantity[min_dist_neigh_str]
                    path_list.append(min_dist_neigh_str)
                    visited.append(min_dist_neigh_str)
                    break
            if flag==0:
                break
        path_list.append("r0")
        path_no="path"+str(count[vehicle])
        vehicle_each_path[path_no]=path_list
        count[vehicle]=count[vehicle]+1
        vehicle_path[vehicle][path_no]=path_list
        if len(visited)>=no_neighbours:
            break

with open("21pt34_solution\\level2b_output.json","w") as outfile:
    json.dump(vehicle_path,outfile)


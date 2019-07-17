#I had implemented the A-star algorithm for a route planner during the first section/project in the Udacity C++ nanodegree I am currently enrolled in: https://github.com/ssheikh85/CppND-Route-Planning-Project
#In addition I used the following references for this project
#https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
#https://www.growingwiththeweb.com/2012/06/a-pathfinding-algorithm.html

import math

class Node(object):
        
    def __init__(self, intersection, parent):
        self.intersection = intersection
        self.parent = parent
        self.g = 0
        self.f = 0
        self.h = 0
        
#Calculate the euclidean distance, for use in calculating heuristic
def distance(x1, x2, y1, y2):
    return math.sqrt(pow((x1-x2),2) + pow((y1-y2),2))

#get's node from open list with lowest f value
def get_min(open_list):
    current_node = open_list[0]
    current_index = 0

    for index, node in enumerate(open_list):
        if node.f < current_node.f:
            current_node = node
            current_index = index
    
    return current_node, current_index
    
#function to add neighbors to the open set
def add_neighbors(current, goal_x, goal_y, M, open_list, closed_list):
  
    neighbors = M.roads[current.intersection]
    current_x = M.intersections[current.intersection][0]
    current_y = M.intersections[current.intersection][1]
    
    open_set = set(open_list)
    closed_set = set(closed_list)
    
    #get neighbors of current node
    for neighbor in neighbors:
        new_node = Node(neighbor, current)
            
        if new_node not in closed_set:
            new_node_x = M.intersections[neighbor][0]
            new_node_y = M.intersections[neighbor][1]
            new_node.g = current.g + distance(current_x, new_node_x, current_y, new_node_y)
            new_node.h = distance(new_node_x, goal_x, new_node_y, goal_y)
            new_node.f = new_node.g+new_node.h

            if new_node not in open_set:
                open_list.append(new_node)
            else:
                for open_node in open_set:
                    if new_node.g < open_node.g :
                        open_node.g = new_node.g
                        open_node.parent = new_node.parent

        

def shortest_path(M,start,goal):

    #open nodes list
    open_list = list()
    
    #closed nodes list
    closed_list = list()
    
    #final path list
    path = list()
    
    #goal x and y coords
    goal_x = M.intersections[goal][0]
    goal_y = M.intersections[goal][1]
    
    start_node = Node(start, None)
    goal_node = Node(goal, None)
    
    open_list.append(start_node)
    
    
    while len(open_list) > 0:
        
        current_node, current_index = get_min(open_list)
        
        open_list.pop(current_index)
        closed_list.append(current_node)
        
        current = current_node
        if current.intersection == goal_node.intersection:
            while current is not None:
                path.append(current.intersection)
                current = current.parent
            #Path originally is from goal to start so needs to be revereed
            return path[::-1]
        
        
        add_neighbors(current_node, goal_x, goal_y, M, open_list, closed_list)
        
        
    print("No path could be found")
    return
    
    
    
    
    
    
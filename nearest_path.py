from typing import DefaultDict
 
 
INT_MAX = 2147483647
 
# Function to find the minimum
# cost path for all the paths

def calc_distance(station1, station2):
    return( ((station1[1]-station2[1])**2 + (station1[2]-station2[2])**2) ** (1/2) )


def get_matrix_form(stations):
    matrix = []
    for station1 in stations:
        row = []
        for station2 in stations:
            if station1 == station2 :
                row.append(0)
            else:
                row.append(calc_distance(station1,station2))
        matrix.append(row)
    return matrix
    
        

def findMinRoute(stations):
    tsp = get_matrix_form(stations)
    sum = 0
    counter = 0
    j = 0
    i = 0
    min = INT_MAX
    visitedRouteList = DefaultDict(int)
 
    # Starting from the 0th indexed
    # city i.e., the first city
    visitedRouteList[0] = 1
    route = [0] * len(tsp)
 
    # Traverse the adjacency
    # matrix tsp[][]
    while i < len(tsp) and j < len(tsp[i]):
 
        # Corner of the Matrix
        if counter >= len(tsp[i]) - 1:
            break
 
        # If this path is unvisited then
        # and if the cost is less then
        # update the cost
        if j != i and (visitedRouteList[j] == 0):
            if tsp[i][j] < min:
                min = tsp[i][j]
                route[counter] = j + 1
 
        j += 1
 
        # Check all paths from the
        # ith indexed city
        if j == len(tsp[i]):
            sum += min
            min = INT_MAX
            visitedRouteList[route[counter] - 1] = 1
            j = 0
            i = route[counter] - 1
            counter += 1
 
    # Update the ending city in array
    # from city which was last visited
    i = route[counter - 1] - 1
 
    for j in range(len(tsp)):
 
        if (i != j) and tsp[i][j] < min:
            min = tsp[i][j]
            route[counter] = j + 1
 
    sum += min
 
    # Started from the node where
    print('*********************************** nearest path method calculations ***********************************\n\n')
    # we finished as well.
    print("Minimum Cost is :", sum)
    print(route)
    return route
 
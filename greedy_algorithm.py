from collections import namedtuple
from typing import List
import matplotlib.pyplot as plot

Route = namedtuple( 'Route', ['start', 'end','distance'] )

def calc_distance(station1, station2):
    return( ((station1[1]-station2[1])**2 + (station1[2]-station2[2])**2) ** (1/2) )


# using all stations  and generating a list of all possible routes and distances between them
def get_all_routes(stations):
    routes = []
    for station_1_index ,station1 in enumerate(stations):
        for station_2_index in range(station_1_index ,len( stations ) ):
            station2 = stations[ station_2_index ]
            # assuming there is no path between a station and it self
            if station_2_index != station_1_index:
                route = Route( station_1_index , station_2_index, calc_distance( station1 , station2 ) )
                routes.append( route )
    return routes

# using it to sort routes list
def get_route_distance(route : Route):
    return route.distance

#calculating_min_cost
def calculating_min_cost(routes):
    cost = 0
    for route in routes:
        cost += route.distance
    return cost

# main logic for algorithm
def calc_tsp_greedy_method( stations ):
    '''
    stations is a list wich its elements are [ name of the station,  X axis coordinates, Y axis coordinates]
    '''
    print('*********************************** greedy method calculations ***********************************\n\n')
    stations_data = [[] for i in range(len(stations))]

    def add_route_to_stations(st1, st2):
        stations_data[st1].append(st2)
        stations_data[st2].append(st1)
    def remove_route_from_stations(st1, st2):
        stations_data[st1].remove(st2)
        stations_data[st2].remove(st1)

    print("getting all possible routes")
    routes = get_all_routes(stations)
    print('sorting routes by distance')
    routes.sort( key = get_route_distance )

    passed_stations = set(())
    tour = []

    # looping through routes and examining each rout
    for route in routes :
        if len(tour) == len(stations) :
            break
        # if route won't make us pass an station twice
        order_of_a = len( stations_data[ route.start ])
        order_of_b = len(stations_data[ route.end ])
        
        if ( order_of_a < 2  and order_of_b < 2 ) :
            
            if ( order_of_a == 1 and order_of_b ==1 ):
                
                add_route_to_stations(route.start, route.end)
                
                cycle = False

                current_station = route.end
                previos_station = route.start
                while True:
                    
                    if len(stations_data[current_station]) < 2:
                        break
                    else:
                        temp_data = stations_data[current_station].copy()
                        temp_data.remove(previos_station)
                        if( temp_data[0] == route.start ):
                            
                            if len(tour) != len(stations)-1:
                                cycle = True
                            break
                        else:
                            previos_station =  current_station
                            current_station = temp_data[0]
                            
                if cycle :
                    
                    remove_route_from_stations(route.start, route.end)
                    
                else:
                    tour.append(route)
                    passed_stations.update( {route.start, route.end} )

            else:
                
                tour.append(route)
                add_route_to_stations(route.start, route.end)


                passed_stations.update( {route.start, route.end} )
        else:
            # this rout makse us pass the station twice
            pass

    print('routes we should take: ')
    print(tour)
    print('stations routes we should travel')
    print(stations_data)
    print('min cost :')
    print(calculating_min_cost(tour))
    return tour
    
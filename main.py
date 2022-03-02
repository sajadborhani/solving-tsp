from random import randint
from turtle import color
import matplotlib.pyplot as plot
from greedy_algorithm import calc_tsp_greedy_method 
import csv
from nearest_path import findMinRoute
stations = []

# if you want to read data from the file uncomment line 10 - 17

# with open('one_year_sale.csv') as file:
#     csv_reader = csv.reader(file, delimiter=',')
#     for index,row in enumerate(csv_reader):
#         if index != 0 and [row[2], 0, 0] not in stations: 
#             stations.append( [row[2], 0, 0] )
# generating random coordinates for each station
# for index,station in enumerate(stations):
#     stations[index] = [station[0], randint(0,100), randint(0,100)]

# if you want top code to work uncomment 20 - 21
for i in range(197):
    stations.append( [i, randint(0,10000), randint(0,10000)] )

print('stations coordinates')
print(stations)

greedy_alg_results = calc_tsp_greedy_method(stations=stations)
nearest_route_alg_results = findMinRoute(stations)

fig, axs = plot.subplots( 2, 1)
axs[1].set_title('greedy approach algorithm')
axs[0].set_title('nearest route approache')

# this part is for ploting the greedy algorithm results
for index,route in enumerate( greedy_alg_results):
    gx = [stations[route.start][1], stations[route.end][1] ]
    gy = [stations[route.start][2], stations[route.end][2] ]
    axs[1].plot(gx ,gy, color='blue')
for station in stations:
    x = [station[1]]
    y = [station[2]]
    axs[1].plot(x,y , 'ro')

# this part is for ploting the nearest path algorithm results
nx = []
ny = []
for station_index in nearest_route_alg_results:
    nx.append(stations[station_index-1][1])
    ny.append(stations[station_index-1][2]) 

nx.append(stations[0][1])
ny.append(stations[0][2]) 
axs[0].plot(nx,ny,color='blue')
for station in stations:
    x = [station[1]]
    y = [station[2]]
    axs[0].plot(x,y , 'ro')

axs[0].axis('equal')
axs[1].axis('equal')
plot.grid()
plot.show()
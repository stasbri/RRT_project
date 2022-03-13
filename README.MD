first of all run

chmod +x run

in order to load all reqiered libraries run

./run build

or

./run b

in order to run search do

./run RRT new_map.json

in order to run RRT* do

./run RRT* new_map.json

in order to see visualisation do

./run visual

or

./run v

in order to make new map do

./run n

first type name of new map file

then type map size

x_size y_size

then start and finish coordinates

x_coordinate y_coordinate

then type step limit

limit

then you start making new obstacles. each obstacle is a polygon. so you will be typing points as x and y coordinates. when you wish to stop making this obstacle type -1. when you wish to stop making obstacles type again -1
example of making a triangle and a square:
0 0
100 100
200 0
-1
300 300
300 400
400 400
400 300
-1
-1


Sorry, but i'm not currently in any condition to write everything that officially as it's required, so here goes a smile :)

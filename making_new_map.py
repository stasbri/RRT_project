import json
import sys
args = sys.argv
new_map_file: str = None
if len(args) > 1:
    new_map_file = args[1]

if new_map_file is None:
    new_map_file = input('no file name given\n')

size = list(map(int, input('give me map size\n').split()))
if len(size) == 1:
    size.append(int(input('give me map y_size\n')))

start = list(map(int, input('give me start coordinates\n').split()))
if len(start) == 1:
    start.append(int(input('give me start y_coordinate\n')))

finish = list(map(int, input('give me finish\n').split()))
if len(finish) == 1:
    finish.append(int(input('give me finish y_coordinate\n')))

limit = float(input('give me step limit\n'))

obstacles = True
obstacle_list = []
while obstacles:
    obstacle_coordinates = []
    print('if you want to stop making new obstacles give -1\n')
    obstacle_coordinates += [list(map(float, input().split()))]
    obstacle = True
    if obstacle_coordinates[-1][0] == -1:
        obstacles = False
        obstacle = False
        obstacle_coordinates = None
    while obstacle:
        print('if you want to stop making new vertices for this obstacle give -1\n')
        new_coordinates = list(map(float, input().split()))
        if new_coordinates[0] == -1:
            obstacle = False
        else:
            obstacle_coordinates += [new_coordinates]
    if obstacle_coordinates is not None:
        obstacle_list += [obstacle_coordinates]


d = {'size': size,
     'start': start,
     'finish': finish,
     'limit': limit,
     'obstacles': obstacle_list}

f = open(new_map_file, 'w')
f.write(json.dumps(d))
f.close()

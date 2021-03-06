import pygame
import time
from constants.constants import *
import json

f = open('src/logs.json', 'r')
logs = f.read()
f.close()
logs = json.loads(logs)
print(logs)
source = logs['map']

f = open(source, 'r')
map_logs = json.loads(f.read())
f.close()
print('/n' * 3)
print(map_logs)


pygame.init()
size = map_logs['size']
screen = pygame.display.set_mode(size)


screen.fill(color=black)
for obstacle in map_logs['obstacles']:
    if len(obstacle) > 1:
        pygame.draw.line(screen, red, obstacle[-1], obstacle[0])
        for i in range(len(obstacle) - 1):
            pygame.draw.line(screen, red, obstacle[i], obstacle[i + 1])
            print(obstacle[i])
    else:
        pygame.draw.circle(screen, red, obstacle[0], 0)
pygame.display.update()


done = False
tree = True
start = map_logs['start']
finish = map_logs['finish']
pygame.draw.circle(screen, red, start, 2)
pygame.draw.circle(screen, blue, finish, 2)
pygame.display.update()
var = 0.01
Stop = False
Next = False
Reverse = False
time.sleep(0)
i = 0
j = 0
first_coor_to_delete = []
second_coor_to_delete = []
while not done:
    if i + j >= len(logs['verts']) + len(logs['path']) - 3:
        done = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        var = 2
    if Next:
        Stop = True
        Next = False
    if Reverse:
        Stop = True
        Reverse = False
    if keys[pygame.K_p]:
        time.sleep(0.1)
        Stop = (Stop + 1) % 2
    if keys[pygame.K_n]:
        time.sleep(0.1)
        Stop = False
        Next = True
    if keys[pygame.K_r]:
        Reverse = True
        Stop = False
        time.sleep(0.1)
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
    if not Stop:
        if i < len(logs['verts']) - 1:
            print('tree')
            if Reverse:
                i -= 1
                print('reverse')
                if logs['verts'][i][0] == '+':
                    cor = logs['verts'][i][1:]
                    print(cor)
                    print(f'firstcoor{first_coor_to_delete}')

                    pygame.draw.line(screen, black, cor[:2], cor[2:])
                    first_coor_to_delete = cor[:2]
                    second_coor_to_delete = cor[2:]
                    pygame.display.update()
                    time.sleep(var)

                else:
                    cor = logs['verts'][i][1:]
                    print(cor)
                    pygame.draw.line(screen, white, cor[:2], cor[2:])
                    if cor[:2] == first_coor_to_delete and cor[2:] == second_coor_to_delete:
                        first_coor_to_delete = []
                        second_coor_to_delete = []
                    pygame.display.update()
                    time.sleep(var)
            else:
                if logs['verts'][i][0] == '+':
                    cor = logs['verts'][i][1:]
                    print(cor)
                    print(f'firstcoor{first_coor_to_delete}')
                    if first_coor_to_delete:
                        print('deleting')
                        pygame.draw.line(screen, white, first_coor_to_delete, second_coor_to_delete)
                    pygame.draw.line(screen, green, cor[:2], cor[2:])
                    first_coor_to_delete = cor[:2]
                    second_coor_to_delete = cor[2:]
                    pygame.display.update()
                    time.sleep(var)

                else:
                    cor = logs['verts'][i][1:]
                    print(cor)
                    pygame.draw.line(screen, black, cor[:2], cor[2:])
                    if cor[:2] == first_coor_to_delete and cor[2:] == second_coor_to_delete:
                        first_coor_to_delete = []
                        second_coor_to_delete = []
                    pygame.display.update()
                    time.sleep(var)
                i += 1
        else:
            print('path')
            cor = logs['path'][j]
            print(cor)
            pygame.draw.line(screen, green, cor[:2], cor[2:])
            pygame.display.update()
            time.sleep(0.01)
            j += 1
        var = 0

time.sleep(15)
pygame.quit()

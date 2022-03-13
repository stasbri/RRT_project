import pygame
import time
from constants.constants import *
import json

f = open('src/logs.json', 'r')
logs = f.read()
f.close()
logs = json.loads(logs)

f = open('new_map.json', 'r')
map_logs = json.loads(f.read())
f.close()

pygame.init()
size = map_logs['size']
screen = pygame.display.set_mode(size)

print(size)
print(logs)

for obstacle in map_logs['obstacles']:
    if len(obstacle) > 1:
        pygame.draw.line(screen, red, obstacle[-1], obstacle[0])
        for i in range(len(obstacle) - 1):
            pygame.draw.line(screen, red, obstacle[i], obstacle[i + 1])
    else:
        pygame.draw.circle(screen, red, obstacle[0])
pygame.display.update()

done = False
tree = True
start = map_logs['start']
finish = map_logs['finish']
pygame.draw.circle(screen, red, start, 2)
pygame.draw.circle(screen, blue, finish, 2)
pygame.display.update()
time.sleep(0.1)
i = 0
j = 0
while not done:
    if i + j >= len(logs['verts']) + len(logs['path']) - 3:
        done = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # print(len(logs[i]), i, len(logs))
    if i < len(logs['verts']) - 1:
        print('tree')
        if logs['verts'][i][0] == '+':
            cor = logs['verts'][i][1:]
            print(cor)
            pygame.draw.line(screen, white, cor[:2], cor[2:])
            pygame.display.update()
            time.sleep(0.01)
        else:
            cor = logs['verts'][i][1:]
            print(cor)
            pygame.draw.line(screen, black, cor[:2], cor[2:])
            pygame.display.update()
            time.sleep(0)
        i += 1
    else:
        print('path')
        cor = logs['path'][j]
        print(cor)
        pygame.draw.line(screen, green, cor[:2], cor[2:])
        pygame.display.update()
        time.sleep(0.01)
        j += 1

time.sleep(15)

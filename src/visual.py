import pygame
import time
from constants.constants import *
f = open('src/logs', 'r')
logs = f.readlines()
f.close()


f = open('src/map_log', 'r')
map_logs = f.readlines()
f.close()

pygame.init()
size = list(map(int, logs[0].split()))
screen = pygame.display.set_mode(size)

print(size)
print(logs)

for line in map_logs:
    cor = list(map(int, line.split()))
    pygame.draw.line(screen, red, cor[:2], cor[2:])
pygame.display.update()

done = False
i = 3
tree = True
start = list(map(int, logs[1].split()))
finish = list(map(int, logs[2].split()))
pygame.draw.circle(screen, red, finish, 2)
pygame.draw.circle(screen, blue, finish, 2)
pygame.display.update()
time.sleep(0.1)
while not done:
    if i == len(logs) - 1:
        done = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    print(len(logs[i]), i, len(logs))
    if logs[i] == 'path\n':
        tree = False
    else:
        if tree:
            cor = list(map(int, logs[i].split()))
            print(cor)
            pygame.draw.line(screen, white, cor[:2], cor[2:])
            pygame.display.update()
            time.sleep(0.01)
        else:
            cor = list(map(int, logs[i].split()))
            print(cor)
            pygame.draw.line(screen, green, cor[:2], cor[2:])
            pygame.display.update()
            time.sleep(0.05)
    i += 1
time.sleep(5)

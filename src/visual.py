import pygame
import time

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
f = open('src/logs', 'r')
logs = f.readlines()
f.close()
size = list(map(int, logs[0].split()))

pygame.init()
screen = pygame.display.set_mode(size)
print(size)
print(logs)

done = False

i = 3
tree = True

start = list(map(int, logs[1].split()))
finish = list(map(int, logs[2].split()))
pygame.draw.circle(screen, red, start, 2)
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
            time.sleep(0.1)
        else:
            cor = list(map(int, logs[i].split()))
            print(cor)
            pygame.draw.line(screen, green, cor[:2], cor[2:])
            pygame.display.update()
            time.sleep(0.01)
    i += 1
time.sleep(10)

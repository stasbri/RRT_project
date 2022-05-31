import pygame
import json
import time

class constants:
    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 255, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)


resulting_dict = dict()
resulting_dict['size'] = list(map(int, input('size\n').split()))
resulting_dict['start'] = list(map(int, input('start\n').split()))
resulting_dict['finish'] = list(map(int, input('finish\n').split()))
resulting_dict['limit'] = int(input('limit\n'))


class Drawer:
    def __init__(self, screen, screen_size, res):
        self.res = res
        self.x = 0
        self.y = 0
        self.size = 10
        self.color = constants.white
        self.screen = screen
        self.screen_size = screen_size
        self.obstacle = []
        self.res['obstacles'] = []

    def remember(self):
        self.obstacle.append([self.x, self.y])
        if len(self.obstacle) > 1:
            pygame.draw.line(self.screen, self.color, self.obstacle[-2], self.obstacle[-1])

    def draw(self, color=None):
        color = color or self.color
        pygame.draw.circle(self.screen, color, (int(self.x), int(self.y)), self.size)

    def move(self, screen_color, x, y):
        self.draw(screen_color)
        self.x, self.y = x, y
        self.draw()

    def finish_obstacle(self):
        self.remember()
        pygame.draw.line(self.screen, self.color, self.obstacle[0], self.obstacle[-1])
        self.res['obstacles'].append(self.obstacle.copy())
        self.obstacle.clear()

    def finish(self):
        self.finish_obstacle()
        return self.res


pygame.init()
size = resulting_dict['size']
screen = pygame.display.set_mode(size)
screen.fill(color=constants.black)

pygame.display.update()
pygame.draw.circle(screen, constants.green, resulting_dict['start'], 10)
pygame.draw.circle(screen, constants.red, resulting_dict['finish'], 10)

drawer = Drawer(screen, size, resulting_dict)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    keys = pygame.key.get_pressed()
    x_1 = drawer.x
    y_1 = drawer.y
    if keys[pygame.K_LEFT]:
        x_1 -= 1

    if keys[pygame.K_RIGHT]:
        x_1 += 1

    if keys[pygame.K_UP]:
        y_1 -= 1

    if keys[pygame.K_DOWN]:
        y_1 += 1
    if keys[pygame.K_x]:
        drawer.finish_obstacle()
    if keys[pygame.K_SPACE]:
        drawer.remember()
    if keys[pygame.K_ESCAPE]:
        res = drawer.finish()
        done = True
    drawer.move(constants.black, x_1, y_1)
    pygame.display.update()
    time.sleep(0.001)
    if done:
        pygame.display.quit()


file_name = input('Please provide filename .json \n')
f = open(file_name, 'w')
f.write(json.dumps(res))
f.close()


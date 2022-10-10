import pygame
pygame.init
import random
import time
from sys import exit

x = []
n = 200
width = 800
height = 600

while len(x) < n:
    number = random.randint(1,height)
    if number not in x:
        x.append(number)

sorting = True

wn = pygame.display.set_mode((800,600))
wn.fill((0,0,0))

while True:
    while sorting:
        in_order = 0
        for i in range(n-1):
            for j in range(n):
                pygame.draw.rect(wn, (255,255,255),(j*(width/n),height-(x[j]),(width/n-1),(x[j])))
            pygame.draw.rect(wn, (0,155,0),(i*(width/n),height-(x[i]),(width/n-1),(x[i])))
            if x[i] > x[i+1]:
                temp = x[i]
                x[i] = x[i+1]
                x[i+1] = temp
                in_order = 0
            in_order += 1
            pygame.display.update()
            #time.sleep(0.2)
            wn.fill((0,0,0))
        in_order = 0
        for i in range(n-1):
            for j in range(n):
                pygame.draw.rect(wn, (255,255,255),(j*(width/n),height-(x[j]),(width/n-1),(x[j]*height/n)))
            pygame.draw.rect(wn, (0,155,0),((n-1-i)*(width/n),height-(x[n-1-i]),(width/n-1),(x[n-1-i])))
            if x[n-1-i] < x[n-1-(i+1)]:
                temp = x[n-1-(i+1)]
                x[n-1-(i+1)] = x[n-1-i]
                x[n-1-i] = temp
                in_order = 0
            in_order += 1
            pygame.display.update()
            #time.sleep(0.2)
            wn.fill((0,0,0))
        if in_order == n-1:
            sorting = False
    for j in range(n):
        pygame.draw.rect(wn, (255,255,255),(j*(width/n),height-(x[j]),(width/n-1),(x[j])))
    pygame.display.update()
    wn.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

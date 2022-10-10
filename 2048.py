import pygame
import random
import time
pygame.init()

#window
window = pygame.display.set_mode((400,400))
pygame.display.set_caption('2048')

#Fonts
Number_1_font = pygame.font.SysFont("Fixedsys", 100)
Number_2_font = pygame.font.SysFont("Fixedsys", 95)
Number_3_font = pygame.font.SysFont("Fixedsys", 70)
Number_4_font = pygame.font.SysFont("Fixedsys", 50)

#grid
grid = [" "," "," "," ",
        " "," "," "," ",
        " "," "," "," ",
        " "," "," "," "]

#Functions
def complete():
    global grid
    full = True
    for i in range(0,16):
        if grid[i] == "2048":
            pygame.draw.rect(window, (0,0,150), (30,115,350,80))
            Finish = Number_1_font.render("Well Done",True,(0,0,0))
            window.blit(Finish,(35, 120))
            pygame.display.update()
            pygame.time.delay(1000)
            grid = [" "," "," "," ",
                    " "," "," "," ",
                    " "," "," "," ",
                    " "," "," "," "]
    update()

def update():
    window.fill(0)
    for i in range(0,4):
        for j in range(0,4):
            pygame.draw.rect(window, (155,155,155), (j*100+1,i*100+1,99,99))
            if grid[i*4+j] == "2":
                pygame.draw.rect(window, (255,180,100), (j*100+1,i*100+1,99,99))
                grid_number = Number_1_font.render(grid[i*4+j],True,(0,0,0))
                x = 32
                y = 22
            if grid[i*4+j] == "4":
                pygame.draw.rect(window, (220,170,80), (j*100+1,i*100+1,99,99))
                grid_number = Number_1_font.render(grid[i*4+j],True,(0,0,0))
                x = 32
                y = 22
            if grid[i*4+j] == "8":
                pygame.draw.rect(window, (200,100,0), (j*100+1,i*100+1,99,99))
                grid_number = Number_1_font.render(grid[i*4+j],True,(0,0,0))
                x = 32
                y = 22
            if grid[i*4+j] == "16":
                pygame.draw.rect(window, (200,0,0), (j*100+1,i*100+1,99,99))
                grid_number = Number_2_font.render(grid[i*4+j],True,(0,0,0))
                x = 10
                y = 22
            if grid[i*4+j] == "32":
                pygame.draw.rect(window, (150,0,0), (j*100+1,i*100+1,99,99))
                grid_number = Number_2_font.render(grid[i*4+j],True,(0,0,0))
                x = 12
                y = 22
            if grid[i*4+j] == "64":
                pygame.draw.rect(window, (100,0,50), (j*100+1,i*100+1,99,99))
                grid_number = Number_2_font.render(grid[i*4+j],True,(0,0,0))
                x = 12
                y = 22
            if grid[i*4+j] == "128":
                pygame.draw.rect(window, (150,0,150), (j*100+1,i*100+1,99,99))
                grid_number = Number_3_font.render(grid[i*4+j],True,(0,0,0))
                x = 7
                y = 30
            if grid[i*4+j] == "256":
                pygame.draw.rect(window, (70,0,150), (j*100+1,i*100+1,99,99))
                grid_number = Number_3_font.render(grid[i*4+j],True,(0,0,0))
                x = 7
                y = 30
            if grid[i*4+j] == "512":
                pygame.draw.rect(window, (0,0,200), (j*100+1,i*100+1,99,99))
                grid_number = Number_3_font.render(grid[i*4+j],True,(0,0,0))
                x = 7
                y = 30
            if grid[i*4+j] == "1024":
                pygame.draw.rect(window, (0,100,200), (j*100+1,i*100+1,99,99))
                grid_number = Number_4_font.render(grid[i*4+j],True,(0,0,0))
                x = 12
                y = 32
            if grid[i*4+j] == "2048":
                pygame.draw.rect(window, (0,200,200), (j*100+1,i*100+1,99,99))
                grid_number = Number_4_font.render(grid[i*4+j],True,(0,0,0))
                x = 12
                y = 32
            if grid[i*4+j] == " ":
                grid_number = Number_1_font.render(grid[i*4+j],True,(0,0,0))
                x = 0
                y = 0
            window.blit(grid_number,(j*100+x,i*100+y))
    pygame.display.update()

update()

def up():
    for i in range(0,4):
        for j in range(0,4):
            n = i*4+j
            while grid[n] != " " and grid[n-4] == " " and n-4 > -1 or grid[n] == grid[n-4] and n-4 > -1:
                if grid[n-4] == " ":
                    grid[n-4] = grid[n]
                    grid[n] = " "
                if grid[n] == grid[n-4]:
                    if grid[n] == "2":
                        grid[n-4] = "4"
                    if grid[n] == "4":
                        grid[n-4] = "8"
                    if grid[n] == "8":
                        grid[n-4] = "16"
                    if grid[n] == "16":
                        grid[n-4] = "32"
                    if grid[n] == "32":
                        grid[n-4] = "64"
                    if grid[n] == "64":
                        grid[n-4] = "128"
                    if grid[n] == "128":
                        grid[n-4] = "256"
                    if grid[n] == "256":
                        grid[n-4] = "512"
                    if grid[n] == "512":
                        grid[n-4] = "1024"
                    if grid[n] == "1024":
                        grid[n-4] = "2048"
                    grid[n] = " "
                n -= 4
    random_grid_number = random.randint(0,15)
    while grid[random_grid_number] != " ":
        random_grid_number = random.randint(0,15)
    n = random.randint(0,1)
    if n == 0 and grid[random_grid_number] == " ":
        grid[random_grid_number] = "2"
    if n == 1 and grid[random_grid_number] == " ":
        grid[random_grid_number] = "4"
    update()
    complete()
    pygame.display.update()
def down():
    for i in range(-3,1):
        for j in range(-3,1):
            n = i*-4+j*-1
            while n-4 > -1 and n < 16 and grid[n-4] != " " and grid[n] == " " or n-4 > -1  and n < 16 and grid[n-4] == grid[n]:
                if grid[n] == " ":
                    grid[n] = grid[n-4]
                    grid[n-4] = " "
                if grid[n-4] == grid[n]:
                    if grid[n-4] == "2":
                        grid[n] = "4"
                    if grid[n-4] == "4":
                        grid[n] = "8"
                    if grid[n-4] == "8":
                        grid[n] = "16"
                    if grid[n-4] == "16":
                        grid[n] = "32"
                    if grid[n-4] == "32":
                        grid[n] = "64"
                    if grid[n-4] == "64":
                        grid[n] = "128"
                    if grid[n-4] == "128":
                        grid[n] = "256"
                    if grid[n-4] == "256":
                        grid[n] = "512"
                    if grid[n-4] == "512":
                        grid[n] = "1024"
                    if grid[n-4] == "1024":
                        grid[n] = "2048"
                    grid[n-4] = " "
                n += 4
    random_grid_number = random.randint(0,15)
    while grid[random_grid_number] != " ":
        random_grid_number = random.randint(0,15)
    if grid[random_grid_number] == " ":
        grid[random_grid_number] = "2"
    update()
    complete()
    pygame.display.update()
def left():
    for i in range(0,4):
        for j in range(0,4):
            n = i*4+j
            while n-1 != -1 and n-1 != 3 and n-1 != 7 and n-1 != 11 and grid[n] != " " and grid[n-1] == " " or  n-1 != -1 and n-1 != 3 and n-1 != 7 and n-1 != 11 and grid[n] == grid[n-1]:
                if grid[n-1] == " ":
                    grid[n-1] = grid[n]
                    grid[n] = " "
                if grid[n] == grid[n-1]:
                    if grid[n] == "2":
                        grid[n-1] = "4"
                    if grid[n] == "4":
                        grid[n-1] = "8"
                    if grid[n] == "8":
                        grid[n-1] = "16"
                    if grid[n] == "16":
                        grid[n-1] = "32"
                    if grid[n] == "32":
                        grid[n-1] = "64"
                    if grid[n] == "64":
                        grid[n-1] = "128"
                    if grid[n] == "128":
                        grid[n-1] = "256"
                    if grid[n] == "256":
                        grid[n-1] = "512"
                    if grid[n] == "512":
                        grid[n-1] = "1024"
                    if grid[n] == "1024":
                        grid[n-1] = "2048"
                    grid[n] = " "
                n -= 1
    random_grid_number = random.randint(0,15)
    while grid[random_grid_number] != " ":
        random_grid_number = random.randint(0,15)
    if grid[random_grid_number] == " ":
        grid[random_grid_number] = "2"
    update()
    complete()
    pygame.display.update()
def right():
    for i in range(-3,1):
        for j in range(-3,1):
            n = i*-4+j*-1
            while n+1 != 4 and n+1 != 8 and n+1 != 12 and n+1 != 16 and grid[n] != " " and grid[n+1] == " " or  n+1 != 4 and n+1 != 8 and n+1 != 12 and n+1 != 16 and grid[n] == grid[n+1]:
                if grid[n+1] == " ":
                    grid[n+1] = grid[n]
                    grid[n] = " "
                if grid[n] == grid[n+1]:
                    if grid[n] == "2":
                        grid[n+1] = "4"
                    if grid[n] == "4":
                        grid[n+1] = "8"
                    if grid[n] == "8":
                        grid[n+1] = "16"
                    if grid[n] == "16":
                        grid[n+1] = "32"
                    if grid[n] == "32":
                        grid[n+1] = "64"
                    if grid[n] == "64":
                        grid[n+1] = "128"
                    if grid[n] == "128":
                        grid[n+1] = "256"
                    if grid[n] == "256":
                        grid[n+1] = "512"
                    if grid[n] == "512":
                        grid[n+1] = "1024"
                    if grid[n] == "1024":
                        grid[n+1] = "2048"
                    grid[n] = " "
                n += 1
    random_grid_number = random.randint(0,15)
    while grid[random_grid_number] != " ":
        random_grid_number = random.randint(0,15)
    if grid[random_grid_number] == " ":
        grid[random_grid_number] = "2"
    update()
    complete()
    pygame.display.update()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
            if event.key == pygame.K_r:
                grid = [" "," "," "," ",
                        " "," "," "," ",
                        " "," "," "," ",
                        " "," "," "," "]
                update()
            if event.key == pygame.K_UP:
                up()
            if event.key == pygame.K_DOWN:
                down()
            if event.key == pygame.K_LEFT:
                left()
            if event.key == pygame.K_RIGHT:
                right()

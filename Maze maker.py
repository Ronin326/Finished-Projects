import pygame
pygame.init
import time
import random

width = 600
height = 600

wn = pygame.display.set_mode((width,height))
wn.fill((100,100,100))

s = 10
cols = round(width/s)
rows = round(height/s)
grid = []
stack = []
path_walked = []

class Cell:
    def __init__(this, i, j):
        this.i = i
        this.j = j
        this.walls = [True,True,True,True]
        this.visited = False
        this.walked = False

    def checkNeighbores(this):
        neighbors = []

        index = ((this.i) + (this.j-1)*cols)
        if index > -1 and index < len(grid):
            top    = grid[index]
            if not top.visited:
                neighbors.append(top)
                
        index = ((this.i+1) + (this.j)*cols)
        if index > -1 and this.i+1 < cols:
            right  = grid[index]
            if not right.visited:
                neighbors.append(right)
                
        index = ((this.i) + (this.j+1)*cols)
        if index > -1 and index < len(grid):
            bottom = grid[index]
            if not bottom.visited:
                neighbors.append(bottom)
                
        index = ((this.i-1) + (this.j)*cols)
        if index > -1 and this.i > 0:
            left   = grid[index]
            if not left.visited:
                neighbors.append(left)


        if len(neighbors) > 0:
            r = random.randint(0,len(neighbors)-1)
            return neighbors[r]
        else:
            return False

    def check_open_path(this):
        open_paths = []

        index = ((this.i) + (this.j-1)*cols)
        if index > -1 and index < len(grid) and grid[((this.i) + (this.j)*cols)].walls[0] == False:
            top    = grid[index]
            if not top.walked:
                open_paths.append(top)
                
        index = ((this.i+1) + (this.j)*cols)
        if index > -1 and this.i+1 < cols and grid[((this.i) + (this.j)*cols)].walls[1] == False:
            right  = grid[index]
            if not right.walked:
                open_paths.append(right)
                
        index = ((this.i) + (this.j+1)*cols)
        if index > -1 and index < len(grid) and grid[((this.i) + (this.j)*cols)].walls[2] == False:
            bottom = grid[index]
            if not bottom.walked:
                open_paths.append(bottom)
                
        index = ((this.i-1) + (this.j)*cols)
        if index > -1 and this.i > 0 and grid[((this.i) + (this.j)*cols)].walls[3] == False:
            left   = grid[index]
            if not left.walked:
                open_paths.append(left)
                
        if len(open_paths) > 0:
            r = random.randint(0,len(open_paths)-1)
            return open_paths[r]
        else:
            return False

    def show(this):
        x = this.i*s
        y = this.j*s
        
        if this.visited == True:
            pygame.draw.rect(wn , (0,150,150),(x,y,s,s))
                
        if this.walls[0]:
            pygame.draw.line(wn, (0,0,0), (x,y),(x+s,y))
        if this.walls[3]:
            pygame.draw.line(wn, (0,0,0), (x,y),(x,y+s))
        if this.walls[1]:
            pygame.draw.line(wn, (0,0,0), (x+s,y),(x+s,y+s))
        if this.walls[2]:
            pygame.draw.line(wn, (0,0,0), (x,y+s),(x+s,y+s))

    def highlight(this):
        x = this.i*s
        y = this.j*s
        pygame.draw.rect(wn , (200,100,0),(x,y,s,s))

def removeWalls(a, b):
    x = a.i - b.i
    y = a.j - b.j
    if x == 1:
        a.walls[3] = False
        b.walls[1] = False
    if x == -1:
        a.walls[1] = False
        b.walls[3] = False
        
    if y == 1:
        a.walls[0] = False
        b.walls[2] = False
    if y == -1:
        a.walls[2] = False
        b.walls[0] = False

for j in range(rows):
    for i in range(cols):
        cell = Cell(i,j)
        grid.append(cell)
        i += 1
    j += 1
current_cell = grid[0]

generating_maze = True
solving = False
solved = False

for i in range(len(grid)):
    grid[i].show()
    i += 1
pygame.display.update()
        
while generating_maze:
    current_cell.visited = True
    pygame.draw.rect(wn, (0,255,0),(grid[len(grid)-1].i*s, grid[len(grid)-1].j*s, s, s))
    current_cell.highlight()
    pygame.display.update()
    
    for i in range(len(grid)):
        grid[i].show()
        i += 1
        
    next_cell = current_cell.checkNeighbores()
    if next_cell != False:
        next_cell.visited = True
        stack.append(current_cell)

        removeWalls(current_cell, next_cell)
        
        current_cell = next_cell
    if next_cell == False and len(stack) > 0:
        current_cell = stack.pop()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            generating_maze = False

    if current_cell == grid[0]:
        generating_maze = False
        solving = True

    #time.sleep(0.2)

for i in range(len(grid)):
    grid[i].show()
    i += 1
    
pygame.display.update()
current_cell.walked = True
path_walked.append(current_cell)

while solving:
##    pygame.draw.rect(wn, (0,255,0),(grid[len(grid)-1].i*s, grid[len(grid)-1].j*s, s, s))
##    current_cell.highlight()
##    pygame.display.update()
##    
##    for i in range(len(grid)):
##        grid[i].show()
##        i += 1

    next_cell = current_cell.check_open_path()
    if next_cell != False:
        next_cell.walked = True
        
        path_walked.append(current_cell)
        
        current_cell = next_cell
        
    if next_cell == False and len(path_walked) > 0:
        current_cell = path_walked.pop()

    if current_cell == grid[len(grid)-1]:
        current_cell = grid[0]
        path_walked.append(grid[len(grid)-1])
        solving = False
        solved = True
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            solving = False
            
    #time.sleep(0.2)

while solved:
    pygame.draw.rect(wn, (0,255,0),(grid[len(grid)-1].i*s, grid[len(grid)-1].j*s, s, s))
    current_cell.highlight()
    pygame.display.update()

    for n in range(len(path_walked)-1):
        pygame.draw.line(wn, (255,0,0), (path_walked[n].i*s + s/2, path_walked[n].j*s + s/2), (path_walked[n+1].i*s + s/2, path_walked[n+1].j*s + s/2), width = 2)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            solved = False

pygame.quit()

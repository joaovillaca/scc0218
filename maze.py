#!/usr/bin/python
# -*- coding: utf-8 -*-

def floodfill(maze, x, y):

    global n
    global total
    
    if x == y and x == n - 1:
        total += 1
        return
        
    maze[x][y] = 2
    
    # '0' -> maze em string
    if y != 0 and maze[x][y - 1] == '0':
        floodfill(maze, x, y - 1)
    if x != 0 and maze[x - 1][y] == '0':
        floodfill(maze, x - 1, y)
    if y != n - 1 and maze[x][y + 1] == '0':
        floodfill(maze, x, y + 1)
    if x != n - 1 and maze[x + 1][y] == '0':
        floodfill(maze, x + 1, y)
        
    maze[x][y] = '0'
    return

n = input()
n = int(n)
maze = list()

try:
    for i in range(n):
            maze.append(input().split()) #le como string
    
except EOFError:
    pass

#print(maze)
total = 0
floodfill(maze, 0, 0)
print(str(total))
#print(maze)
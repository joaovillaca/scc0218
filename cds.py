#!/usr/bin/python
# -*- coding: utf-8 -*-

def dfs(i, soma):
    global tam
    global path
    global entry
    if i == num:
        if soma > tam and maxx >= soma:
            tam = soma
            path = list(path2)
        return
    path2.append(entry[i+2])
    dfs(i+1, soma+entry[i+2])
    path2.pop()
    dfs(i+1, soma)
    
while True:
    try:
        entry = list(map(int, input().split()))
        maxx =  entry[0]
        num = entry[1]
        tam = 0
        path = list()
        path2 = list()
        dfs(0, 0)
        
        for i in path:
            print(str(i) + ' ' , end='')
        print('sum:%d' % tam)
        
    except EOFError:
        break
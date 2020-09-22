c = 0
s = 0
t = 0
iterator = 0
mass = list()

for y in range(4):
    aux = list(map(int, input().split()))
    c = aux[0]
    s = aux[1]
    
    spec = list(map(int, input().split()))
        
    iterator = s
    while iterator < c*2 - 1:
        if iterator > s:
            break
        spec[iterator-1] = 0
        iterator += 1
        
    spec.sort()
    t += 1
    print('Set #' + str(t))
    
    avg = float(0)
    for i in range(c):
        d = c*2 - i - 1
        if d > s:
            d = s - i - 1
        mass.append(spec[i] + spec[d-1])
        avg += mass[i]
        print(' ' + str(i) + ': ', end = '')
        if spec[i]:
            print(str(spec[i]) + ' ', end = '')
        if spec[d-1]:
            print(str(spec[d-1]))
     
    avg /= c
    imb = float(0)
    for i in range(c):
        imb += abs(mass[i] - avg)
    print('IMBALANCE = %.5f\n' % imb)
    
    spec.clear()
    
        
        
        
        
        
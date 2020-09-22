for cont in range(int(input())):

    num = int(input())
    lista_m = []
    lista_h = []
    
    for i in range(num):
        lista_aux = list(map(int, input().split()))
        lista_m.append(lista_aux[1:])

    for i in range(num):
        lista_aux = list(map(int, input().split()))
        lista_h.append(lista_aux[1:])
    
    homensolteiro = [i for i in range(1, num+1)]
    mulhersolteira = [i for i in range(1, num+1)]
    
    dic_homem = {}
    dic_mulher = {}
    
    while len(homensolteiro) > 0:
        homem = homensolteiro[0]
        mulher = lista_h[homem-1].pop(0)
        if mulher in mulhersolteira:
            dic_homem[homem] = mulher
            dic_mulher[mulher] = homem
            mulhersolteira.remove(mulher)
            homensolteiro.remove(homem)
        elif lista_m[mulher-1].index(homem) < lista_m[mulher-1].index(dic_mulher[mulher]):
            homensolteiro.append(dic_mulher[mulher])
            homensolteiro.remove(homem)
            dic_homem[dic_mulher[mulher]] = None
            dic_mulher[mulher] = homem
            dic_homem[homem] = mulher
    
    for i in range(1, num+1):
        print(i, dic_homem[i])
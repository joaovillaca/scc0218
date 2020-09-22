t = int(input())
moedas = list()
while t > 0:
    n = int(input())
    moedas = list(map(int, input().split()))
    total = 0
    saida = 0
    for i in range(n):
    	if n-1 == i or total + moedas[i] < moedas[i+1]:
    		total += moedas[i]
    		saida += 1
    print(saida)
    moedas.clear()
    t = t - 1
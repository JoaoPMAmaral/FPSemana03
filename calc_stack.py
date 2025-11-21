from collections import deque

numerosDeque = deque()
numerosDequeLeft = deque()

numeros = input("")

for a in range(0,len(numeros)):
    if numeros[a] != " ":
        numerosDeque.append(int(numeros[a]))
        numerosDequeLeft.appendleft(int(numeros[a]))

print(numerosDeque)

for b in numerosDequeLeft:
    print(b * 2)
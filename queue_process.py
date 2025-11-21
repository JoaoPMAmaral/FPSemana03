from collections import deque


palavras = input("")
palavra = ""
palavrasDeque = deque()
palavrasDequeque = deque()

for a in range(0,len(palavras)):
    if palavras[a] != " ":
        palavra += palavras[a]
    else:
        palavrasDeque.appendleft(palavra)
        palavrasDequeque.append(palavra)
        palavra = ""

print(palavrasDeque)

for b in palavrasDequeque:
    if(b.count("a") > 0):
        print(b)
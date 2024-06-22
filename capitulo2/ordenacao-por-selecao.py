import random
from pprint import pprint

def buscaMaior (arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i][1] > menor[1]:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def ordenarPorSelecao (arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMaior(arr)
        novoArr.append(arr.pop(menor))
    return novoArr


musicas = [
    ("Bohemian Rhapsody - Queen", random.randint(1, 1000)),
    ("Hotel California - Eagles", random.randint(1, 1000)),
    ("Stairway to Heaven - Led Zeppelin", random.randint(1, 1000)),
    ("Imagine - John Lennon", random.randint(1, 1000)),
    ("Smells Like Teen Spirit - Nirvana", random.randint(1, 1000)),
    ("Sweet Child O' Mine - Guns N' Roses", random.randint(1, 1000)),
    ("Billie Jean - Michael Jackson", random.randint(1, 1000)),
    ("Hey Jude - The Beatles", random.randint(1, 1000)),
    ("Like a Rolling Stone - Bob Dylan", random.randint(1, 1000)),
    ("Rolling in the Deep - Adele", random.randint(1, 1000))
]

pprint(musicas)
musicasOrdenadas = ordenarPorSelecao(musicas)
print("\n")
pprint(musicasOrdenadas)
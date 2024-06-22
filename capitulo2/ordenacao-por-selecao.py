def buscaMenor (arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
        print("iterou buscaMenor")
    return menor_indice

def ordenarPorSelecao (arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
        print("iterou ordenarPorSelecao")
    return novoArr

print(ordenarPorSelecao([
    100,
    65,
    897,
    6,
    99,
    3,
    5
]))
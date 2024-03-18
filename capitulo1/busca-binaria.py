def gerar_lista_ordenada(valor_final):
    contador = 0
    lista = []
    for x in range(valor_final):
        contador = contador + 1
        lista.append(contador)
    return lista

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    contador = 0

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return {"iterações": contador, "indice": meio}
        if chute > item:
            alto = meio - 1
        if chute < item:
            baixo = meio + 1
        contador = contador + 1
    return None

minha_lista = gerar_lista_ordenada(256)
print (len(minha_lista))
print (pesquisa_binaria(minha_lista, 256))

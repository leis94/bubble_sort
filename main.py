import random


def ordenamiento_de_burbuja(lista):

    n = len(lista)
    temp = 0
    for i in range(0, n-1):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j+1]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
    return lista


if __name__ == "__main__":
    lista = [random.randint(0, 100) for i in range(5)]
    print(lista)
    ordenamiento_de_burbuja(lista)
    lista_ordenada = ordenamiento_de_burbuja(lista)
    print(lista_ordenada)
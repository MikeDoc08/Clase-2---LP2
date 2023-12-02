def busqueda_no_ordenada(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i  # Se encontró el elemento en la posición i
    return -1  # El elemento no está en la lista

def busqueda_binaria(arr, objetivo):
    izquierda, derecha = 0, len(arr) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if arr[medio] == objetivo:
            return medio  # Elemento encontrado, devuelve el índice
        elif arr[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1  # Elemento no encontrado

# Ejemplo de uso
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elemento_a_buscar = 8

resultado = busqueda_binaria(mi_lista, elemento_a_buscar)
print("Índice del elemento:", resultado)

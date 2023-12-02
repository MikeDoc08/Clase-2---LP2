def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[0]
        menores = [x for x in arr[1:] if x <= pivote]
        mayores = [x for x in arr[1:] if x > pivote]
        return quicksort(menores) + [pivote] + quicksort(mayores)

# Ejemplo de uso
mi_lista = [64, 34, 25, 12, 22, 11, 90]
resultado = quicksort(mi_lista)
print("Lista ordenada:", resultado)

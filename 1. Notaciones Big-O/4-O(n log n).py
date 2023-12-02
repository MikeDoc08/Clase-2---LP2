def merge_sort(arr):
    if len(arr) > 1:
        medio = len(arr) // 2
        izquierda = arr[:medio]
        derecha = arr[medio:]

        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0

        # Fusionar las listas izquierda y derecha en la lista original
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                arr[k] = izquierda[i]
                i += 1
            else:
                arr[k] = derecha[j]
                j += 1
            k += 1

        # Asegurarse de que no falten elementos
        while i < len(izquierda):
            arr[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            arr[k] = derecha[j]
            j += 1
            k += 1

# Ejemplo de uso
mi_lista = [38, 27, 43, 3, 9, 82, 10]
merge_sort(mi_lista)
print("Lista ordenada:", mi_lista)

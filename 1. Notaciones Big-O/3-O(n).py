def busqueda_secuencial(lista, objetivo):
    """Búsqueda secuencial en una lista."""
    for elemento in lista:
        if elemento == objetivo:
            return True
    return False

# Lista de ejemplo
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Ejemplos de uso
print(busqueda_secuencial(mi_lista, 5))  # Devuelve True
print(busqueda_secuencial(mi_lista, 11))  # Devuelve False

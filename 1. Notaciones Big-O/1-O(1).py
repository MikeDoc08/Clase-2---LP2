lista_ejemplo = [1, 2, 3]

def ejemplo_o1(lista):
    # Acceder al primer elemento de la lista
    primer_elemento = lista[0]
    
    # Imprimir el primer elemento
    print(primer_elemento)
    
    # Añadir un elemento al final de la lista
    lista.append(42)

ejemplo_o1(lista_ejemplo)

print(lista_ejemplo)

# En este ejemplo:

# Acceder al primer elemento de la lista (lista[0]) es una operación de complejidad O(1) porque no importa cuántos elementos tenga la lista, siempre toma un tiempo constante acceder al primer elemento.

# Imprimir el primer elemento (print(primer_elemento)) también es una operación O(1) en términos de complejidad, ya que imprimir un valor es una operación básica que no depende del tamaño de la lista.

# Añadir un elemento al final de la lista (lista.append(42)) también es O(1), ya que la operación de agregar un elemento al final de una lista en Python tiene una complejidad constante amortizada.
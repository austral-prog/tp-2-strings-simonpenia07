def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    nombre = input('Como es tu nombre?')
    apellido = input('Como es tu apellido?')
    print((nombre + ' ' + apellido).lower())
    print((nombre + ' ' + apellido).title())
    print((nombre + ' ' + apellido).upper())
    print(('\t' + nombre + ' ' + apellido).lower())

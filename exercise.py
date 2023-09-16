lista_personas = [
    ('11111111', 'Pedro', 'Paez', 24),
    ('22222222', 'Fito', 'Garcia', 23),
    ('33333333', 'Leo', 'Peralta', 26),
    ('44444444', 'Bruno', 'Mac', 25),
    ('55555555', 'Nico', 'Zaoral', 27),
    ('44444444', 'Bruno', 'Mac', 25),
]


def ordenar(lista_personas):
    """ El metodo debe devolver una lista con las edades ordenadas de menor a mayor"""
    ordered_list = sorted(lista_personas, key=lambda tup: tup[3])
    return ordered_list


def convertir_a_diccionario(lista_personas):
    """ Hacer un diccionario que tenga como claves los “dni” y como valores tuplas con nombre, apellido y edad """
    people_dict = {}
    for dni, name, last_name, age in lista_personas:
        people_dict[dni] = (name, last_name, age)
    return people_dict


def devolver_edad(lista_personas, dni):
    """ Para la 'lista_personas' devuelve la edad de la persona que tenga el dni definido.
    Tip: intentar usar el método convertir_a_diccionario"""
    people_dict = convertir_a_diccionario(lista_personas)
    person = people_dict.get(dni)
    if person is not None:
        return person[2]
    else:
        return None


def eliminar_repetidos(lista_personas):
    """ El metodo debe devolver los elementos unicos """
    unique_persons_list = []
    
    for person in lista_personas:
        if person not in unique_persons_list:
            unique_persons_list.append(person)

    # unique_persons_list = list(set(lista_personas))

    return unique_persons_list

def separar_por_edad(lista_personas):
    """ Devolver dos listas
    * lista 1: mayores de 25 (incluido)
    * lista 2: menores de 25
    """
    people_list = eliminar_repetidos(lista_personas)
    older_than_25 = []
    younger_than_25 = []

    for person in people_list:
        _, _, _, age = person
        if age >= 25:
            older_than_25.append(person)
        else:
            younger_than_25.append(person)

    return older_than_25, younger_than_25


def obtener_promedio(lista):
    """ Implementar obtener el promedio de la lista de números que se recibe.
    Capturar con un try/except la excepción de dividir por cero"""
    try:
        people_list = eliminar_repetidos(lista)
        ages = [person[3] for person in people_list]

        if len(ages) == 0:
            raise ZeroDivisionError("La lista de edades está vacía. No se puede calcular el promedio.")
        else:
            average = sum(ages) / len(ages)
            return average
    except ZeroDivisionError as e:
        print(e)
        return None

def main():
    """ Este metodo no debe modificarse y es solo a fines de probar el codigo """
    print('Resultados:\n')
    print(' * Edades ordenadas: %s\n' % ordenar(lista_personas))
    print(' * Elementos como diccionario: %s\n' % convertir_a_diccionario(lista_personas))
    print(' * La edad para dni 55555555 es: %s\n' % devolver_edad(lista_personas, '55555555'))
    print(' * Elementos únicos: %s\n' % eliminar_repetidos(lista_personas))
    print(' * Los mayores de 25 son: %s\n' % separar_por_edad(lista_personas)[0])
    print(' * Los menores de 25 son: %s\n' % separar_por_edad(lista_personas)[1])
    print(' * El promedio de las edades es: %s\n' % obtener_promedio(ordenar(lista_personas)))
    print(' * El promedio de una lista vacía es: %s\n' % obtener_promedio([]))


if __name__ == '__main__':
    main()

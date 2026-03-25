"""
Biel Teixidor Cladellas
>>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

>>> descompon(36 * 175 * 143)
(2, 2, 3, 3, 5, 5, 7, 11, 13)

>>> mcm(90, 14)
630

>>> mcd(924, 780)
12

>>> mcm(42, 60, 70, 63)
1260

>>> mcd(840, 630, 1050, 1470)
210
"""

def esPrimo(numero):
    """
    Devuelve True si su argumento es primo, y False si no lo es
    
    Argumentos:
        numero (int)

    Salida:
        bool
    """
    esprimer = True

    if numero <= 0:
        raise TypeError("El numero ha de ser natural i mes gran que 1")    
    
    if numero == 1:
        return False
    
    for i in range(2, numero):
        if numero % i == 0:
            esprimer = False
            break 
    return esprimer


def primos(numero):
    """
    Devuelve una tupla con todos los números primos menores que su argumento.
    
    Argumentos:
        numero (int)

    Salida:
        Una tupla con todos los numeros primos que ha encontrado.
    """
    vecPrimos = tuple(i for i in range(1, numero) if esPrimo(i))
    return vecPrimos


def descompon(numero):
    """
    Devuelve una tupla con la descomposicion en factores primos de su argumento.
    
    Argumentos:
        numero (int)
    
    Salida:
        Una tupla con los factores primos resultantes.
    """
    if esPrimo(numero):
        return tuple(numero)
    else:
        vecDescom = []
        divisor = 2
        while numero > 1:
            if numero % divisor == 0:
                vecDescom.append(divisor)
                numero = numero // divisor
            else:
                divisor += 1                       
        return tuple(vecDescom)


def mcm(*numeros):
    """
    Devuelve el minimo comun multiplo de sus argumentos
    
    Argumentos:
        *numeros: Los numeros que queramos calcular, separados por comas.

    Salida:
        El resultado del minimo comun múltiplo.
    """
    resultat_final = numeros[0]
    
    for numero in numeros[1:]:
        divNumero1 = list(descompon(resultat_final))
        divNumero2 = list(descompon(numero))
        
        resultat = 1
        
        for element in divNumero1:
            resultat = resultat * element
            if element in divNumero2:
                divNumero2.remove(element)
                
        for factor in divNumero2:
            resultat = resultat * factor
            
        resultat_final = resultat
        
    return resultat_final


def mcd(*numeros):
    """
    Devuelve el maximo comun divisor de sus argumentos.
    
    Argumentos:
        *numeros: Los numeros que queramos calcular, separados por comas.

    Salida:
        El resultado del maximo comun divisor.
    """
    resultat_final = numeros[0]
    
    for numero in numeros[1:]:
        divNumero1 = list(descompon(resultat_final))
        divNumero2 = list(descompon(numero))
        
        resultat = 1
        
        for element in divNumero1:
            if element in divNumero2:
                resultat = resultat * element
                divNumero2.remove(element)
                
        resultat_final = resultat
        
    return resultat_final

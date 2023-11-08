def soma(*args):
    total = 0
    
    for numeros in args:
        total += numeros
        return total

soma1__2 = soma(1, 2, 3, 4, 5, 6)
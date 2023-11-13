# Resolução do Luiz no exercicio 117

selected_number = 4

def create_multiplicator(multiplicator):
    def multiplicate(number):
        return number * multiplicator
    return multiplicate

double = create_multiplicator(2)
triple = create_multiplicator(3)
quadruple = create_multiplicator(4)

print(double(selected_number))
print(triple(selected_number))
print(quadruple(selected_number))

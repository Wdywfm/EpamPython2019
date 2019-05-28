
def is_armstrong(number):
    return number == sum([int(x)**len(str(number)) for x in str(number)])


assert is_armstrong(153) == True, 'Число Армстронга'
assert is_armstrong(10) == False, 'Не число Армстронга'

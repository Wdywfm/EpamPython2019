
def letters_range(start='a', stop=None, step=1, **smth):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = [x for x in alphabet]
    for key in smth:
        index = alphabet.index(key)
        alphabet[index] = smth[key]
    if not stop:
        stop = alphabet.index(start)
        start = 0
    else:
        start = alphabet.index(start)
        stop = alphabet.index(stop)
    return alphabet[start:stop:step]


print(letters_range('b', 'w', 2))
print(letters_range('g'))
print(letters_range('g', 'p'))
print(letters_range('g', 'p', **{'l': 700, 'o': 0}))
print(letters_range('p', 'g', -2))
print(letters_range('a'))

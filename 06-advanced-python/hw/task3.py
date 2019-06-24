"""
Реализовать дескриптор, кодирующий слова с помощью шифра Цезаря

"""


class ShiftDescriptor:

    def __init__(self, value):
        self.value = value
        self.message = ''
        self.alphabet = self.get_alphabet()

    def __get__(self, instance, owner):
        return self.message

    def __set__(self, instance, value):
        value_list = list(value)
        for i, c in enumerate(value_list):
            value_list[i] = self.alphabet[c]
        value = ''.join(value_list)
        self.message = value

    def get_alphabet(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        new_alphabet = list(alphabet)
        orig_alphabet = list(alphabet)
        while self.value >= 26:
            self.value -= 26
        for i, c in enumerate(new_alphabet):
            j = ord(c)
            if j + self.value > 122:
                j = j + self.value - 26
            else:
                j += self.value
            new_alphabet[i] = chr(j)
        k = dict(zip(orig_alphabet, new_alphabet))
        return k


class CeasarSipher:

    message = ShiftDescriptor(4)
    another_message = ShiftDescriptor(7)
    mesg = ShiftDescriptor(26)


a = CeasarSipher()
a.message = 'abc'
a.another_message = 'hello'
a.mesg = 'same'

assert a.message == 'efg'
assert a.another_message == 'olssv'

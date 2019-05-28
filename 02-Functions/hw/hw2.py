
def atom(a=None):
    g = a

    def set_value(z):
        nonlocal g
        g = z
        return g

    def get_value():
        return g

    def process_value(args, *f):
        for i, func in enumerate(f):
            func(args[i])
        return g

    def delete_value():
        nonlocal g
        g = None

    return get_value, set_value, process_value, delete_value


getv, setv, processv, deletev = atom(3)
print(getv())
print(setv(0))
arguments = (1, 5, 7)
print(processv(arguments, *[setv, setv, setv]))
deletev()
print(getv())

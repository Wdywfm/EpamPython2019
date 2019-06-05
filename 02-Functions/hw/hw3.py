
counter_name = 0


def make_it_count(func):
    def new_func(c):
        global counter_name
        counter_name += 1
        return func(c)
    return new_func


n = make_it_count(sorted)
s = 'fdfsasfgw'
for i in range(10):
    print(n(s), counter_name)

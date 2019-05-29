from functools import reduce

# Problem 6 - "Sum square difference"
dif = sum([x for x in range(1, 101)])**2 - sum([x**2 for x in range(1, 101)])
print(dif)

# Problem 40 - "Champernowne's constant"
arr = [int(''.join(str(c) for c in range(10**6))[10**k]) for k in range(7)]
prod = reduce(lambda x, y: x*y, arr)
print(prod)

# Problem 48 - "Self powers"
last_ten__digits = (sum([k**k for k in range(1000)])-1) % 10**10
print(last_ten__digits)

# Problem 9 - "Special Pythagorean triplet"
triplet = [a*b*c for a in range(1, 334) for b in range(a, 500)
           for c in range(b, 501) if a+b+c == 1000 and a**2+b**2 == c**2][0]
print(triplet)


def collatz_steps(n):
    return 0 if n == 1 else collatz_steps(n/2) + 1 if n % 2 == 0\
        else collatz_steps(3*n+1) + 1


assert collatz_steps(16) == 4
assert collatz_steps(12) == 9
assert collatz_steps(1000000) == 152

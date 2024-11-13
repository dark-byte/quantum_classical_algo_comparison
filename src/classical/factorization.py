# src/classical/factorization.py

import math
import random

def gcd(a, b):
    """Calculate the greatest common divisor of a and b."""
    while b != 0:
        a, b = b, a % b
    return a

def pollards_rho(n):
    """
    Pollard's Rho algorithm for integer factorization.
    
    Parameters:
        n (int): The integer to factorize.
    
    Returns:
        int: A non-trivial factor of n.
    """
    if n % 2 == 0:
        return 2
    
    x = random.randint(2, n - 1)
    y = x
    c = random.randint(1, n - 1)
    d = 1

    def f(x):
        return (x * x + c) % n

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)
    
    if d == n:
        return pollards_rho(n)  # Retry if factorization fails
    return d


if __name__ == "__main__":
    n = 91  # Example number to factorize
    factor = pollards_rho(n)
    print(f"A non-trivial factor of {n} is: {factor}")
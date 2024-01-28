import math

# Input the value of 'n'
n = int(input("Enter a positive integer: "))

# Check if n is a positive integer
if n <= 0:
    print("Wrong Input")
else:
    # Calculate the square root of n
    sqrt_n = int(math.sqrt(n))

    # Initialize a list to store the factors
    factors = []

    # Find factors up to the square root of n
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            factors.append(i)

    # Add the corresponding pair of factors
    for factor in factors:
        pair_factor = n // factor
        factors.append(pair_factor)

    # Remove duplicates (in case n is a perfect square)
    factors = list(set(factors))

    # Sort the list of factors
    factors.sort()

    # Print the factors
    if factors:
        print("Factors of", n, "up to its square root:", factors)
    else:
        print(n, "is a prime number.")

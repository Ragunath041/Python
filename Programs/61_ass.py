# Input the value of N
N = int(input("Enter the value of N: "))

# Print the upper half of the pattern
for i in range(1, N + 1):
    # Print the numbers in increasing order
    for j in range(1, i + 1):
        print(f"{i}", end="")
        if j < i:
            print("*", end="")
    print()

# Print the lower half of the pattern
for i in range(N, 0, -1):
    # Print the numbers in decreasing order
    for j in range(1, i):
        print(f"{i}", end="")
        if j < i - 1:
            print("*", end="")
    print()

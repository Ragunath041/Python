def calculate_bit_score(n):
    # Initialize large and small to extreme values
    large = 0
    small = 9

    # Find largest and smallest digits in the number
    while n > 0:
        remd = n % 10
        if remd > large:
            large = remd
        if remd < small:
            small = remd
        n //= 10
    
    # Calculate bit score based on largest and smallest digits
    return (large * 11 + small * 7) % 100

def main():
    # Read input
    N = int(input())
    numbers = list(map(int, input().split()))

    # Calculate bit scores for each number
    bit_scores = [calculate_bit_score(num) for num in numbers]

    # Initialize pairs counter
    Pairs = 0

    # Count pairs based on bit scores' first digit
    for i in range(1, 10):
        count = 0
        
        # Count occurrences in even indices (0-based)
        for j in range(0, len(bit_scores), 2):
            if bit_scores[j] // 10 == i:
                count += 1
        
        # Update Pairs based on count
        if count == 2:
            Pairs += 1
        elif count >= 3:
            Pairs += 2
        
        count = 0
        
        # Count occurrences in odd indices (0-based)
        for j in range(1, len(bit_scores), 2):
            if bit_scores[j] // 10 == i:
                count += 1
        
        # Update Pairs based on count
        if count == 2:
            Pairs += 1
        elif count >= 3:
            Pairs += 2

    # Print the total number of pairs
    print(Pairs)

if __name__ == "__main__":
    main()

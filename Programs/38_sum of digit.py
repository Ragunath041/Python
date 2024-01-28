# def get_single_digit_sum(number):
#     while number > 9:
#         # Convert the number to a list of digits
#         digits = [int(digit) for digit in str(number)]
        
#         # Calculate the sum of the digits
#         number = sum(digits)
    
#     return number

# # Example usage
# number = int(input())
# result = get_single_digit_sum(number)
# print(result)
def get_single_digit_sum(number):
    if number <= 9:
        return number
    
    # Convert the number to a list of digits
    digits = [int(digit) for digit in str(number)]
    
    # Calculate the sum of the digits
    sum_of_digits = sum(digits)
    
    return get_single_digit_sum(sum_of_digits)

# Example usage
number = 987654321
result = get_single_digit_sum(number)

print("Original number:", number)
print("Sum of digits (single digit):", result)

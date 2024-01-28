input_list = [234, 567, 321, 345, 123, 110, 767, 111]
output_list = []

for num in input_list:
    large_digit = max(map(int, str(num)))  
    small_digit = min(map(int, str(num)))  
    result = (large_digit * 11) + (small_digit * 7)
    output_list.append(result)

print(output_list)

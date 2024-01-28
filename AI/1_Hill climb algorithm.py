import random

def hill_climb(number):
    current_max = max(number)
    while True:
        index = random.randint(0,len(number) - 1)
        new_num = random.randint(min(number) , max(number))
        new_number = number.copy()

        new_number[index] = new_num

        if max(new_number) > max(number):
            number = new_number
        else:
            break
    return max(number)


length = int(input("Enter the Size :"))
start = int(input("Initial :"))
end = int(input("Final :"))

number = [random.randint(start,end) for i in range(length)]

print("Original number :",number)

ans = hill_climb(number)
print("Maximum Value : ",ans)
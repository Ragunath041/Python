def find_product(num1, num2, num3):
    if num1 != 7 and num2 != 7 and num3 != 7:
        a = num1 * num2 * num3
        return a
    elif num1 == 7:
        a = num2 * num3
        return a
    elif num2 == 7:
        a = num3
        return a
    else:
        return -1

product = find_product(7, 6, 2)
print(product)

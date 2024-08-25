def is_prime(n):
    if n <= 1:
        return False
    for i in range(2 , int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
a = int(input())
b = int(input())
arr = []
for i in range(a , b + 1):
    if is_prime(i):
        arr.append(i)
ans = []
a_1 = sorted(arr)
a_2 = sorted(arr)[::-1]
for i in range(len(arr)):
    if a_1[i] not in ans:
        ans.append(a_1[i])
    if a_2[i] not in ans:
        ans.append(a_2[i])
print(ans)

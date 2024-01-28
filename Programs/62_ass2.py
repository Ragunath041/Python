# Read input
n = int(input())
p_list = list(map(int, input().split()))
q_list = list(map(int, input().split()))
a = set(p_list[1:] + q_list[1:])


# Create a set for levels Little X and Little Y can pass together
# passable_levels = set(p_list[1:] + q_list[1:])

# Check all levels
# for level in range(1, n+1):
#     if level not in passable_levels:
#         print("Oh, my keyboard!")
#         break
# else:
#     print("I become the guy.")
print(a)
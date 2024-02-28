for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    ans = lst[0] + lst[1]
    for i in range(2 , n):
        ans += lst[i] * 2
    print(ans)
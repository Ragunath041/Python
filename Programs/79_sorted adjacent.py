for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    if n == 2:
        print("NO" if a[0] > a[1] else "YES")
        continue
    if n == 3:
        print("NO" if a[1] < min(a[2] , a[0]) or a[1] > max(a[2] , a[0]) else "YES")
        continue
    print("YES")
            
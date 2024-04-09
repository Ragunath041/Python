if __name__ == "__main__":
    T = int(input())
    arr = []
    for _ in range(T):
        n = int(input())
        f = n // 100
        s = (n // 10) % 10
        t = n % 10
        max_digit = max(s, max(f, t))
        min_digit = min(s, min(f, t))
        ans = max_digit * 11 + min_digit * 7
        arr.append(ans % 100)
    
    ans = 0
    for i in range(T - 1):
        for j in range(i + 1, T):
            if arr[i] // 10 == arr[j] // 10 and i != j:
                ans += 1
                break
    
    print(ans)

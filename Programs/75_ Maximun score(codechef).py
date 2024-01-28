t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    st = []
    st.append(arr[0])
    ans = 0
    for i in range(1, n):
        val = arr[i]

        if len(st) == 0:
            st.append(val)
        else:
            top = st[-1]
            if top == val:
                st.append(val)
            else:
                st.pop()
                ans += 1

    print(ans)

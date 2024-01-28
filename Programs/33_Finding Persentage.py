n = int(input())
ans = {}
for i in range (n):
    x = input()
    name = x [0]
    marks = [float (i) for i in x [1:]]
    ans [name] = marks
std_name = input()
marks = data.get(std_name)
if marks:
    avg = sum(marks) / len(marks)
    res = f"{avg :.2f}"
    print(res)

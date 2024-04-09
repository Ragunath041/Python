import math
PIE = 3.14
s_x, s_y, s_z = 0, 0, 0
def shortDist(x, y, z):
    global s_x, s_y, s_z
    if z == s_z and (y == s_y or x == s_x) and s_z != 0:
        if x != s_x:
            dis = (2 * PIE * abs(x - s_x)) / 6.0
        else:
            dis = (2 * PIE * abs(y - s_y)) / 6.0
    else:
        dis = int(math.sqrt((x - s_x) ** 2 + (y - s_y) ** 2) + abs(z - s_z))
    s_x, s_y, s_z = x, y, z
    return dis
if __name__ == "__main__":
    N = int(input())
    N *= 3
    arr = list(map(int, input().split()))
    sum_dist = 0.0
    s_x, s_y, s_z = arr[0], arr[1], arr[2]
    for i in range(3, N, 3):
        sum_dist += shortDist(arr[i], arr[i+1], arr[i+2])
    print("{:.2f}".format(sum_dist))
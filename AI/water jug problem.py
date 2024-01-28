juga_cap = 4
jugb_cap = 3
a = 0
b = 0
fill = 2

while a != fill:
    if a == 0:
        a = juga_cap
    elif b > 0 and a < juga_cap:
        pour = min(b, juga_cap - a)
        a += pour
        b -= pour
    elif b == 0:
        b = jugb_cap

print(f"A: {a} B: {b}")

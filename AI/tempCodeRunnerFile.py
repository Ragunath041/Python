juga_cap = 4
jugb_cap = 3
a = 0
b = 0
fill = 2
while a != fill:
    if a == 0:
        a = juga_cap
    elif b > 0:
        b = 0
    elif a < juga_cap and b > 0:
        pour = min(b,juga - a)
        a += pour
        b += pour
    elif b == 0:
        b = jugb_cap
print(f"A : {a} B: {b} ")
# 1yr=365days
# 90yr=32850days

# 1yr=12mnth
# 90yr=1080mnth

# 1mnth=5weeks
# 12mnth=60weeks
# 90yrs=5400weeks
age=int(input("ENTER YOUR AGE:"))
x=90-age
days=x*365
months=x*12
weeks=x*52
print(f"Your Age is {x} and remaining {months} days {weeks} months and {days} weeks left for upto 90 years")

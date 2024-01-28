print("Day Pridiction...")
print("------------------------------------------")

month_cal = {
    "1" : 0,
    "2" : 3,
    "3" : 3,
    "4" : 6,
    "5" : 1,
    "6" : 4,
    "7" : 6,
    "8" : 2,
    "9" : 5,
    "10": 3,
    "11": 3,
    "12": 5
}
Day_finder = {
    0 : "SUNDAY",
    1 : "MONDAY",
    2 : "TUESDAY",
    3 : "WEDNESDAY",
    4 : "THURSDAY",
    5 : "FRIDAY",
    6 : "SATURDAY"
}
date = int(input("Enter Date :"))
month = int(input("Enter Month (1 to 12):"))
year = int(input("Enter the Year :")) #2013
year_lst = list(str(year)) #['2','0','1','3']
a = int(year_lst[2]) #1
b = int(year_lst[3]) #3
if a == 0:
    x = b #3
else:
    x = int(str(a) + str(b)) #13
quo = x // 4 #3
no_month = month_cal.get(str(month),"Entered Wrong input")

if year >= 1600 and year <= 1699:
    ans = (x + quo + date + no_month + 6) % 7
    print(end="\n")
    print(f"{date} / {month} / {year} is {Day_finder.get(ans)}")
elif year >= 1700 and year <= 1799:
    ans = (x + quo + date + no_month + 4)% 7
    print(end="\n")
    print(f"{date} / {month} / {year} is {Day_finder.get(ans)}")
elif year >= 2000 and year <= 2099:
    ans = (x + quo + date + no_month + 6) % 7
    print(end="\n")
    print(f"{date} / {month} / {year} is {Day_finder.get(ans)}")
elif year >= 1800 and year <= 1899:
    ans = (x + quo + date + no_month + 2) % 7
    print(end="\n")
    print(f"{date} / {month} / {year} is {Day_finder.get(ans)}")
elif year >= 1900 and year <= 1999:
    ans = (x + quo + date + no_month + 0) % 7
    print(end="\n")
    print(f"{date} / {month} / {year} is {Day_finder.get(ans)}")
else:
    print("Wrong Input...")
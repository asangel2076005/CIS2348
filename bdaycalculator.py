#Angelo Angel

print("Birthday Calculator")

print("Current day")
month_current = int(input("Month: "))
day_current = int(input("Day: "))
year_current = int(input("Year: "))

print("Birthday")
month_bday = int(input("Month: "))
day_bday = int(input("Day: "))
year_bday = int(input("Year: "))

user_year = year_current - year_bday - 1

if (month_bday < month_current):
    user_year = user_year + 1
elif (month_bday == month_current):
    if (day_bday <= day_current):
        user_year = user_year + 1

if (month_bday == month_current) and (day_bday == day_current):
    print("Happy Birthday!")

print(f"You are {user_year} years old.")




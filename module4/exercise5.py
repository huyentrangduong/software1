year = int(input("Enter a year: "))

if year%4 or year%100:
    print(f"{year} is a leap year.")
elif year%100 and year%400:
    print(f"{year} is a not leap year.")
else:
    print(f"{year} is not a leap year.")
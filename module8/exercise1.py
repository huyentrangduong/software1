month_number = int(input("Enter the number of a month (1-12): "))
print(f"You entered: {month_number}")

month_of_year = ("December (12)", "January (1)", "February (2)", "March (3)", "April (4)", "May (5)", "June (6)", "July (7)", "August (8)", "September (9)", "October (10)", "November (11)")

def get_season (month_number):
    
    if month_number in [12, 1, 2]:
        return "winter"
        
    elif month_number in [3, 4, 5]:
        return "spring"

    elif month_number in [6, 7, 8]:
        return "summer"
        
    elif month_number in [9, 10, 11]:
        return "autumn"

    else:
        return "Please enter a number between 1 and 12."
        
season = get_season(month_number)
if season == "Please enter a number between 1 and 12.":
    print (season)
else:
    print (f"The season is {season}.")






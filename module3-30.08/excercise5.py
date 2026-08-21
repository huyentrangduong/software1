talents = input("Enter talents: ")
talents = float(talents)

pounds = input("Enter pounds: ")
pounds = float(pounds)

lots = input("Enter lots: ")
lots = float(lots)

total_grams = (((talents*20)+ pounds)*32 + lots)*13.3
#total_grams = int(total_grams)

kilograms = int(total_grams//1000)  #convert gr to kg
remaining_grams = (total_grams%1000)

print("The weight in modern units: ")
print(f'{kilograms} kilograms and {remaining_grams:.2f} grams.')

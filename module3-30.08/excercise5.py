
talents = input("Enter talents: ")
talents = float(talents)

pounds = input("Enter pounds: ")
pounds = float(pounds)

lots = input("Enter lots: ")
lots = float(lots)

total_grams = talents + pounds + lots
kilograms = total_grams/1000  #convert gr to kg
#remaining_grams = 

print("The weight in modern units:" + str(total_grams))
#print() 
#The program should output the kilograms and grams in the form "[kilograms] kilograms and [grams] grams."

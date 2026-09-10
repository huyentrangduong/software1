
#airports = {"EFHK":"Helsinki-Vantaa Airport","KJFK":"John F. Kennedy Airport"}
airports = {}

option = ""

while option != "3":
    option = input ("\nAirport Data Management\n1. Enter a new airport\n2. Fetch airport information\n3. Quit\nPlease choose an option (1-3): ")
    
    if option == "1":
        code = input("Enter the ICAO code: ")
        name = input("Enter the airport name: ")
        airports[code]= name
        print(f"Airport {name} with ICAO code {code} has been added.")

    elif option == "2":
        code = input("Enter the ICAO code: ")
        if code in airports:
            print(f"The airport with ICAO code {code} is {name}.")
            
        else:
            print(f"No airport found with ICAO code {code}.")
        
print ("Thank you for using the Airport Data Management system. Goodbye!")



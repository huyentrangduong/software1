gender = input("Enter biological gender (male/female): ")
gender_lowercase = gender.lower()
value = float(input("Enter hemoglobin value (g/l): "))


if gender_lowercase == "male" and value <= 133:
    print("Your hemoglobin is low.")
elif gender_lowercase == "male" and 134 <= value <= 167:
    print("Your hemoglobin is normal.")
elif gender_lowercase == "male" and 167 < value:
    print("Your hemoglobin is high.")

elif gender_lowercase == "female" and value <= 116:
    print("Your hemoglobin is low.")
elif gender_lowercase == "female" and 117 <= value <= 155:
    print("Your hemoglobin is normal.")
elif gender_lowercase == "female" and 155 < value:
    print("Your hemoglobin is high.")
elif gender_lowercase != "male" or gender != "female":
    print("Invalid gender.")
else:
    print("Your hemoglobin is high.")


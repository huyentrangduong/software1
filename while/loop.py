
#while
rounds = 3
while rounds >= 0:
    print("Hi")
    rounds = rounds -1

rounds = int(input("How many greetings: "))
finished_rounds = 0
while finished_rounds<rounds:
    print("Good morning")
    finished_rounds = finished_rounds + 1

num = 3
while num <= 1000:
    if num % 3 == 0: #% is divisible by 3
        print(num)
    num += 1

num = 3
while num <= 1000:
    if num % 3 == 0: #% is divisible by 3
        print(num)
    num += 4
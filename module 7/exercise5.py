
original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter_even_numbers =[]

def filter_even_numbers(original):
    filter_even_numbers =[]
    original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for number in original:
        if number % 2 == 0:
            filter_even_numbers.append(number)
    return filter_even_numbers

filtered = filter_even_numbers(original)
print("Original list:", original)
print("List with even numbers only:", filtered)
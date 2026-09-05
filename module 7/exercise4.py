def sum_of_list(numbers):
    sum = 0

    for number in numbers:
        sum = sum + number

    return sum

numbers = [1, 2, 3, 4, 5]

result = sum_of_list(numbers)

print(f"The sum of the numbers in the list is: {result}")
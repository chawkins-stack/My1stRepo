# Test data
data_set_1 = [10, 20, 30, 40, 50]
data_set_2 = [5, -3, 12, 0, -8]
data_set_3 = [100, 250, 75, 420, 130]

# Assign first dataset to numbers
numbers = data_set_1

# Print numbers
print(numbers)

# Find sum
total_sum = 0
for num in numbers:
    total_sum = total_sum + num

# Find average
average = total_sum / len(numbers)

# Find smallest number
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num

# Find largest number
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

# Required formatted output (FIXED FORMAT)
print(f"Sum: {total_sum}, Average: {average}, Smallest: {smallest}, Largest: {largest}")


# Function version
def analyze_numbers(numbers):

    print(numbers)

    total_sum = 0
    for num in numbers:
        total_sum = total_sum + num

    average = total_sum / len(numbers)

    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num

    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num

    # Required formatted output (FIXED FORMAT)
    print(f"Sum: {total_sum}, Average: {average}, Smallest: {smallest}, Largest: {largest}")


# Run function on all datasets
analyze_numbers(data_set_1)
analyze_numbers(data_set_2)
analyze_numbers(data_set_3)
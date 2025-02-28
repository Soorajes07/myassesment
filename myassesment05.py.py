# Function to find the largest number in a list
def find_largest(numbers):
    largest = numbers[0]  # Assume the first number is the largest
    for number in numbers:
        if number > largest:
            largest = number
    return largest

# Sample list of numbers
numbers = [3, 45, 2, 78, 12, 99, 56]

# Call the function and print the result
largest_number = find_largest(numbers)
print(f"The largest number in the list is: {largest_number}")

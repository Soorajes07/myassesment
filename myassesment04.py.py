# Function to calculate sum of even numbers in a given range
def sum_of_evens(start, end):
    total = 0
    for number in range(start, end + 1):
        if number % 2 == 0:
            total += number
    return total

# Define the range
start = 1
end = 10

# Call the function and print the result
result = sum_of_evens(start, end)
print(f"The sum of even numbers between {start} and {end} is: {result}")

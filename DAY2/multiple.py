# "If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below the provided parameter value number."//
# Define the limit
limit = 10  # Change this to your desired limit

# Loop through numbers and print multiples of 3 or 5
for number in range(limit):
    if number % 3 == 0 or number % 5 == 0:
        print(number)

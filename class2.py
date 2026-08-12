# import random
# random_number = random.randint(1, 100)
# print(random_number)
# chances = 6
# # print(chances)


# for loop
# for i in range (0, 11):
#     print(i)

# for i in range(1, 6):
#     print(i)

# fruits = ["mango","pawpaw","quava"]
# for fruits in fruits:
#     print(fruits)

# chances = 3
# while chances > 0:
#     print(f"You have   ")

# milk_ounces = 16
# pour_amount = 6
# remaining = milk_ounces - pour_amount
# print(remaining)

# milk_per_serving = 1.5      # 1.5 cups
# scoops_per_serving = 3      # 3 scoops
# total_guests = 2

# # Multiply to calculate the total ingredients needed
# total_milk_needed = milk_per_serving * total_guests      # 3.0 cups
# total_scoops_needed = scoops_per_serving * total_guests  # 6 scoops

# # Subtract to find the remaining inventory
# remaining_milk = 12.0 - total_milk_needed 
# print(remaining_milk)   

# cereal_in_box = 10
# required_scoops = 3
# print(cereal_in_box >= required_scoops)

# print(2 + (3 * 4))
# print((2 + 3) * 4)


# x = 2
# y = 12

# if y != 0 and (y / x) < 12:
#     print("invalid response")
# else:
#     print("good")

# If Python didn't use short-circuit evaluation, it would evaluate y / x (10 / 0) and crash the entire script instantly.

# and operator
# Guard against None
# user = None
# if user is not None and user.name == "Alice":
#     print("Welcome, Alice")

# user = None

# # Checks 'user is not None' first -> False. 
# # SKIPS checking user.name!
# if user is not None and user.name == "Alice":
#     print("Welcome, Alice")

# result = 0 and "Hello"
# print(result)  # Output: 0  (Short-circuited at 0, "Hello" was never touched)

# result = "Python" and "Hello"
# print(result)  # Output: "Hello" (First was truthy, evaluated and returned the second)

# OR (or) OPERATOR
# user_input = "David"  # Empty string (Falsy)

# # Since user_input is empty, Python moves to the second value and assigns "Guest"
# display_name = user_input or "Guest"
# print(display_name)  # Output: Guest

# scores = [95, 88, 72] #try 0, 49, to have attension neeeded

# # If scores is empty (len == 0), the second condition isn't checked, 
# # preventing an IndexError if accessing scores[0] on an empty list.
# if len(scores) == 0 or scores[0] < 50:
#     print("Attention needed!")
# else:
#     print("Good")

# banana_count = "2"      # text string
# milk_cups = "1.5"       # text string

# # Convert the text variables into numeric variables
# banana_number = int(banana_count)   # Becomes the integer 2
# milk_number = float(milk_cups)      # Becomes the float 1.5

# # Perform mathematical addition on the numbers
# total = banana_number + milk_number  # 2 + 1.5 = 3.5
# print(total)

# print(float("1.5"))
# # Now try:
# print(int("5"))

# banana_count = 2
# message = "I have " + str(banana_count) + " bananas"
# # message becomes "I have 2 bananas"
# print(message)

# ounces = 8.5
# print("Pouring " + str(ounces) + " ounces of milk.")


# # using .isdigit. 
# age = input("Enter your age: ")

# if age.isdigit(): 
#     age_num = int(age)  # Safe to convert now!
#     print(f"In 5 years, you will be {age_num + 5}.")
# else:
#     print("Invalid input! Please enter numbers only (e.g., 25).")

# user_input = "banana"

# # Check if the string consists entirely of digits (0-9)
# if user_input.isdigit():
#     banana_count = int(user_input)
#     print("Conversion successful!")
# else:
#     print("Warning: That is not a valid number! Defaulting to 0.")
#     banana_count = 0

# value1 = "15"
# value2 = "banana"
# print(value1.isdigit())
# print(value2.isdigit())

# quantity = int("3")
# price = float("2.99")
# total_cost = quantity * price
# print(total_cost)

# value = "23.45"
# num = int(float(value))
# print(num)


# using .replace - it is used to search for specific piece of text, symbol , etc in a string
# price = "$100.45".replace("$", "")
# num = int(float(price))
# print(num)

# age = "45 years".replace("years", "")
# num_age = int(age)
# print(num_age)

# try:
#     number = int(input("Enter a number to divide 100: "))
#     result = 100 / number
# except ValueError:
#     print("You must type a number!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# else:
#     print(f"Success! The answer is {result}.")
# finally:
#     print("Calculation check complete.\n")

# total_score = 100
# student =  -0
# try:
#     average = total_score / student
# except:
#     ZeroDivisionError
#     print("Cannot calculate average: Student cannot be zero ")
#     average = 0

# print(f"Average Score: {average} ")




# if student > 0:
#     average = total_score / student 

# else:
#     average = 0
# print(f"Average score: {average}")

# selected_drink = "Green Tea"
# target_temp = 100
# if selected_drink == "Green Tea":
#     target_temp = 80

# print(target_temp)

# selected_product = "Rice"
# price_tag = "$540"

# if selected_product == "Chicken":
#     price_tag = "$412"
# elif selected_product == "Rice":
#     price_tag = "$345"

# print(price_tag)

# using and / or operator 

# role = "admin"
# role = "manager"
# is_logged_in = True
# is_premium = True
# if role == "admin" or role == "manager" or (is_logged_in and is_premium):
#     print("Access granted")
# else:
#     if role != "admin" or role!= "manager" :
#         print("Access denied")

# if role == "admin" or (is_logged_in and is_premium):
#     print("Welcome")


# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(f"{n} equals {x} * {n//x}")
#             break

# a = ['My', 'name', 'is', 'Bassey']
# for i in range(len(a)):
#     print(i, a[i])


#     # Break 
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(f"{n} equals {x} * {n//x}")
#             break

#     # Continue statement
# for num in range(2, 10):
#     if num % 2 == 0:
#         print(f"Found an even number {num}")
#         continue
#     print(f"Found an odd number {num}")

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# money = 100

# if money >= 300:
#     print("KFC!!!")
# else:
#     print("byebye")

# user = input("Enter Your Username ")
# passw = input("Enter Your Password ")

# if user == "admin" and passw == "1234":
#     print("Done")
#     print("1 = Vat Cal")
#     print("2 = cal")
#     num = input("Select Number>>")
#     if num == "1":
#         price = int(input("Enter Your Price"))
#         vat = 7/100
#         print(price + (price * vat))
#     elif num == "2":
#         x = int(input("enter number"))
#         y = int(input("enter number"))
#         print(x + y)
# else:
#     print("false")

# x = 0
# while x<5:
#     x = x+1
#     print(x)

# while True:
#     print("hello")

user = input("Enter Your Username ")
passw = input("Enter Your Password ")


# while user != "admin" and passw != 1234:
#     print("invalid username and password")
#     user = input("Enter Your Username ")
#     passw = input("Enter Your Password ")
# print("done")

x = 0
while x == 0:
    user = input("Enter Your Username ")
    passw = input("Enter Your Password ")
    if user == "admin" and passw == "1234":
        print("done")
        x = 1
    else:
        print("wrong")
        

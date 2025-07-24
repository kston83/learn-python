
user_name = input("Enter your unsername: ")


# length = len(user_name)
# if length > 12 or not user_name.isalpha() or user_name.count(" ") > 1 :
#     print("The username entered is invalid")
# else:
#     print("The username is valid")


if len(user_name) > 12:
    print("Your username cannot contain more than 12 characters.")
elif not user_name.find(" ") == -1:
    print("Your username cannot contain spaces")
elif not user_name.isalpha():
    print("Your username cannot contain digits")
else: 
    print(f"Welcome {user_name}")




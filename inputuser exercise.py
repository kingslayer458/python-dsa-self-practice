#validate user inout exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username=input("enter your name:")

username
if len(username) > 12:
    print("username is too long")

elif not username.find(" ") == -1:
    print("username must not contain spaces")

elif not username.isalpha():
    print("your username cant contain digits")    
else:
    print(f"welcome user:{username}")    
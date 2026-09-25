# username=input("Enter your username: ")
# password=input("Enter your password: ")

# if username=="admin" and password=="password":
#     print("Login Successful")
# else:
#     print("Login failed! Try again.")


def login_status(username, password):
    if username=="admin" and password=="password":
        return True
    else:
        return False

status=login_status("admin", "password")

if status:
    print("login success")

else:
    print("Login failed")
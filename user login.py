#user log in system in python
user = input("Enter User ID.: ")
passwd = input("Enter Passcode,: ")
if(user and passwd in "admin"):
    print("You Are LoggedIn.")
else:
    print("Login Failed.")

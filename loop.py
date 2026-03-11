users = ("admin", "root", "developer", "sec", "operator")
login = input("What user are you?: ")
for user in users:
    if user == login:
        print("ATTENTION: This is the admin")
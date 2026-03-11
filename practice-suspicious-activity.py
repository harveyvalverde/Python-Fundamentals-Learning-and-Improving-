emails = ["user@gmail.com", "hacker@malware.com", "admin@empresa.com", "guest@yahoo.com"]
amenaza = "hacker@malware.com"
for e in emails:
    if e == amenaza:
        print("Es una amenaza")
    else:
        print("All good!")

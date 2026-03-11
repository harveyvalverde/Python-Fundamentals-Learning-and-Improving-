languages = ["English", "Spanish", "French"]
languages.insert(1, "Chinese")
print(languages)
languages.remove("Spanish")
print(languages)
print("English" in languages)
print(len(languages))
languages.clear()

print(languages)
#we ask the user to enter a phrase (or some)
phrase = input("Enter a phrase and I'll calculate how long it would take you to say it: ")
#we separate each word creating a list per each space
separated_words = phrase.split(" ")
#we use len to see how many elements are in the list
word_counter = len(separated_words)
if word_counter > 120:
    print("That's a lot of words!")
elif word_counter > 10:
    print("That's pretty normal!")
else:
    print("Come on! You can speak more!")
print(f"You said {word_counter} words and you'd last {word_counter / 2} seconds saying them")
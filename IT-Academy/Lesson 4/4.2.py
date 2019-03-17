text = input("Enter your text:")
text_to_list = text.split()
check = {"A", "a", "E", "e", "Y", "y", "U", "u", "I", "i", "O", "o"}
minimal_word = (min(text_to_list, key=lambda x: len(x)))
minimal_word = set(minimal_word)
print(minimal_word.intersection(check))

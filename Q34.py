def find_number_of_word(sentence: str):
    words = sentence.split()
    word_count = len(words)
    return word_count
   

print(find_number_of_word("My name is nisha khan"))
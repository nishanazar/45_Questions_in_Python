def word_exits(word , sentence: str):
    if word in sentence:
        print(f"YES {word} present in the {sentence}")
    else:
        print(f"NO {word} present in the {sentence}")


word_exits("ali", "my name is ali" )
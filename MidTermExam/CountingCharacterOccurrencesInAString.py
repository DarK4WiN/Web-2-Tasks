def counting_character(sentence , given_character):
    sentence = sentence.lower()
    count = 0
    for char in sentence:
        if char == given_character:
            count += 1
    print(f"{given_character} occurs {count} times")
sentence = input("Input sentence: ")
given_character = input("Input character: ")
counting_character(sentence, given_character)

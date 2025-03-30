def replacing_substring(sentence, given_substring):
    if given_substring in sentence:
        new_substring = input("Input new substring: ")
        return sentence.replace(given_substring, new_substring)
    else:
        return "Don't find that substring"
sentence = input("Input sentence: ")
given_substring = input("Input substring: ")
print(replacing_substring(sentence, given_substring))
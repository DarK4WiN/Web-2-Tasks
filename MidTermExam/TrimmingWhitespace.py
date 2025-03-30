def trimming_whitespace(sentence):
    return sentence.strip()
sentence = input("Input sentence: ")

print(repr(sentence))
print(repr(trimming_whitespace(sentence)))
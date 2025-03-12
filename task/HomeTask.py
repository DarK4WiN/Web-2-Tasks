sentence = "I study in Khazar University"
# # words = sentence.split(" ")
# # print (len(words))
# sentence2 ="".join(sentence.split())
# print(sentence2)
# print(sentence2[::3])
# word = input("Enter a word: ")
# if ("aa" in word):
#     print("Yes, the word is true")
# else:
#     print("No, the word is false")
sentence = sentence.lower()
u = sentence.count("u")
i = sentence.count("i")
if u > i:
    print("In the sentence have u more than i")
else :
    print("In the sentence have i more than u")
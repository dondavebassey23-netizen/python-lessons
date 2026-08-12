# print("Hello World!")

sentence = "latte and espresso"
words = sentence.split(" and ")
print(words)
rejoined = "-".join(words)
print(rejoined)

sentence2 = "espresso with milk and caramel and chocolate"
new_sentence2 = sentence2.split(" with ", 1) # 1 is  The maxsplit parameter defines the maximum number of splits to perform on a string.
print(new_sentence2)

sentence3 = "espresso with milk and caramel and chocolate"
new_sentence3 = sentence2.rsplit(" and ", 1) # 1 is  The maxsplit parameter defines the maximum number of splits to perform on a string.
print(new_sentence3)
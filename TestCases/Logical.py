from builtins import input

print("Logical")
str = input("Enter a Message")
words= str.split()
words.sort()

for word in words:
    print(word)


'''a = int(input())
b = int(input())
c = a + b
f = 123.45609
name = "Bhavya"

print("%d,%s,%f,%.2f" % (c, name, f, f))'''



# Write a program to print no. of words & each word from the given sentence.

sentence = "python programming is fun and easy too"
words = sentence.split()
print(words)
i = 1
for word in sentence.split():
    i += 1
    print(word)
print(i - 1)

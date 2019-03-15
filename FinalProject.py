''''''
# Final Project
# Kristian Shyiak
# 3.7.19
# This program is doing


name = input("What is your name: ")

def greeting():
    print("Hi there " + name + "!")
    print("Nice to meet you, here are your numbers.")
    for i in range(1, 50):
        print("Number: " + str(i))
        x = i
        if i == 3:
            break
        while x >= 0:
            print(name + str(x))
            x = x - 1
        print("")

greeting()         # This makes all the code appear

'''
Final Project
Kristian Shyiak
3.7.19
This program is doing
'''

try:
    name = input("What is your name: ")
    print('Your name:', name)

except ValueError:
    print('\n''That is not a name!')

# Function part
# 3.15.19

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
            x = x - 2
        print("")

greeting()        # This makes all the code appear

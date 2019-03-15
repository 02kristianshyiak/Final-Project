''''''
# Final Project
# Kristian Shyiak
# 3.7.19
# In this program you type in your name and you get a number 


name = input("What is your name: ")  #This is where you type your name

def greeting():      # This is where the function starts
    print("Hi there " + name + "!") # This prints "Hi there" and the typed in name
    print("Nice to meet you, here are your numbers.")  # This prints "Nice to meet you, here are your numbers."
    for i in range(1, 50):       # This starts the for loop
        print("Number: " + str(i)) # This prints the number and the string
        x = i   # This is x=i
        if i == 3: # Both these lines tell when to break
            break
        while x >= 0:       # This starts the while loop
            print(name + str(x))    # This prints the name and the string
            x = x - 1    # This tells how many lines there will be
        print("")     # This helps print

greeting()        # This makes all the code appear

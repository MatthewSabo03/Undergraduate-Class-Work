# Question 05
#
# Code takes a counting number from the user and increments that input to
# display 100 lines of output. For any number not divisible by 4 or 6, the 
# number itself is printed. If the number is divisible by 4, "Flippity" is
# displayed. If the number is divisible by 6, "Floppity" is displayed.
# If the number is divisible by both 4 and 6, "FlippityFloppity" is displayed.
# After a line is displayed, the number will be incremented.
#
# You may assume that any variables used are appropriately scoped and
# initialized.

def main():
    # I) Take input from the user
    userInput = input("Please input a counting number to start at: "))

    # II) If the number is valid
    if userInput >= 0

        # A) Set up your loop to run 100 times. For each number...
        for currentNumber in range(100)
            
            # A) Begin checking conditions which will print out appropriately
            if currentNumber % 4 != 0 or currentNumber % 6 != 0
                print(currentNumber)
                
            if currentNumber % 4 == 0
                print("Flippity")

            elif currentNumber % 6 == 0
                print("Floppity")

            elif currentNumber % 4 != 0 or currentNumber % 6 != 0
                print("Flippity Floppity")

main()

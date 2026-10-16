# ------------------------------------------------------
#        Name: Julia Bergles
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """ Ask for a sentence until the secret word, dog, or Dog is found """
    while True: 
        sentence = input("Give me a word: ") #get sentence from user
        if secret_word in sentence: #check if secret word in sentence
            print("You used the secret word!") #print text if secret word in sentence
            break
        elif "dog" in sentence or "Dog" in sentence: #check if Dog or dog in sentence
            print("You used the word \"dog\" or the word \"Dog\"!") #if dog or Dog in sentence print text
            break
        else: #otherwise print try again and repeat loop
            print("Try again")



# Task 2
def check_greater():
    """ Compare two integers until one is greater than the other """
    while True:
        number1 = input("Give me a number: ") #have user input 2 numbers
        number2 = input("Give me a second number: ")
        if number1 > number2: #if first number is greater than the second print text
            print("First is Greater")
            break 
        elif number2 > number1:  #if second number is greater than first print text
            print("Second is Greater")
            break
        else: #if numbers are equal user must try again
            print("Try again")


# Task 3
def get_special_numbers():
    """ Print odd numbers that are mutiples of 3 between 1 and 40 excluding multiples of 5 """
    for num in range(1, 41): #examine integers from 1-40
        if num % 2 == 0: #discard even numbers
            continue
        elif num % 3 != 0: #discard non multiples of 3
            continue
        elif num % 5 == 0: #discard multiples of 5
            continue
        print(num)
        


# Task 4.a
def my_for_loop():
    """ Ask for a valid string and classify its letters """
    word = input("Give me a string: ") # get a string from the user
    if len(word) <2 or len(word) > 5 or " " in word:  # stop if the string length is invalid or it contains spaces
        print("bad word")
        return
    for letter in word: # go through each letter in the string
        if letter.lower() in "aeiou": #check if letter is vowel
            print(f"{letter} is a vowel")
        else: #if not vowel classify it as a consonant
            print(f"{letter} is a consonant")


# Task 4.b
def my_while_loop():
    """ Ask the user to pick an option and keep asking for a menu choice until the user picks the exit option  """
    while True:
        choice = input("Pick an option a, b, or c: ")  # ask the user to choose an option
        if choice == "a":   # repeat the menu if the user chooses a
            continue
        elif choice == "b":  # print goodbye and return if the user chooses b
            print("Goodbye")
            return
        elif choice == "c": # exit the entire program if the user chooses c
            sys.exit()
        else:  # print try again if the user enters an invalid option
            print("try again")
            continue


# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")

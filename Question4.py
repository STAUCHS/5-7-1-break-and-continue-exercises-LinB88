#-------------------------------------------------------------------------
# Name:
# Purpose:
# Author:     Last Name. First Initial
# Created:    dd/mm/yyyy
#-------------------------------------------------------------------------
#define variables
input_word = input("Enter a word: ")

# loop
while True:
    if input_word == "stop":
        break
    print(f"Your word: {input_word}")
    input_word = input("Enter a word: ")
print("Goodbye!")

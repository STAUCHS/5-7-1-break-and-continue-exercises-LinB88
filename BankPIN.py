#-------------------------------------------------------------------------
# Name:       BankPin
# Purpose:
# Author:     Lin.B
# Created:    05/06/2024
#-------------------------------------------------------------------------
# header
print(f"WELCOME TO STA BANK!")

# Initiate variables
correct_pin = 1938

entered_pin = int(input("Enter your PIN: "))

# Loop
while entered_pin != correct_pin:
# check if pin correct
    if entered_pin == correct_pin:
        break
    print(f"Incorrect PIN. Please try again.")
    entered_pin = int(input("Enter your PIN: "))
print(f"Correct PIN. You may now access your account.")
    

#-------------------------------------------------------------------------
# Name:
# Purpose:
# Author:     Last Name. First Initial
# Created:    dd/mm/yyyy
#-------------------------------------------------------------------------

# ask user for starting number
start_num = int(input("Enter a number:"))
end_num = int(input("Enter end number: "))

num = start_num
total = 0

while num in range(start_num,end_num+1):
    total += num
    num += 1
    continue
print(total)

    

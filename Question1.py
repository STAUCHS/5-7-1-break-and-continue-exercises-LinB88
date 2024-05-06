#-------------------------------------------------------------------------
# Name:       Loop that prints 0-10 skips 7
# Purpose:
# Author:     Last Name. First Initial
# Created:    dd/mm/yyyy
#-------------------------------------------------------------------------

#Set value of num
num = 1

#when num reach 7, break and then new loop starting from 7
while num in range(1,11):
    print(num)
    num += 1
    if num == 7:
        break
while num in range (7,10):
    num += 1
    print(num)


    


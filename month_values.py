#Write a python script to take the month value in numeric format and display the
#number of days in it.

Month=int(input("Enter a month number:"))
if Month==2:
    print("28 days or 29 days")
elif Month==4 or Month==6 or Month==9 or Month==11 :
    print("30 days")
elif Month>12 or Month<1:
    print("invalid Month entered")
else:
    print("31 Days")
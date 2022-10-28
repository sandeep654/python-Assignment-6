#Write a python script to check whether a given year is a leap year or not.

Year=int(input("Enter year :"))
if Year%4==0 and Year%100!=0 or  Year%400==0:
        print("this is a leap year")
else:
    print("this is not a leap year")
#Write a python script to print two given words in dictionary order

first=str(input ("Enter first letter:"))
second=str(input("Enter second letter:"))
if first>second:
    print(first,second)
elif second>first:
    print(second,first)
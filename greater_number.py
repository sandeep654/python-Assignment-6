#Write a python script to print greater between two numbers. Print number only once
#even if the numbers are the same

num_1=int(input("Enter the first number:"))
num_2=int(input("Enter the second number:"))
if num_1>num_2:
    print('num_1 is greater')
elif num_1==num_2:
    print('both are equal')
else:
    print("num_2 is greater")    
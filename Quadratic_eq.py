#Write a python script to check whether a given quadratic equation has two real &
#distinct roots, real & equal roots or imaginary roots

a = int(input('Enter values of a: '))
b = int(input('Enter values of b: '))
c = int(input('Enter values of c: '))

d = b*b - 4*a*c

if d == 0:
    print('Roots are real & equal')
else:
    print('Roots are imaginary')
'''Write a python script to accept one complex number from the user and display the
greater number between real part and imaginary part'''

c1=complex(input('Enter complex number format[x+yj] :'))

if c1.real>c1.imag:
    print(c1.real ,"is a real part and is greater imaginary part.")
else:
    print(c1.imag,"is a imaginary part and is grater than real part.")
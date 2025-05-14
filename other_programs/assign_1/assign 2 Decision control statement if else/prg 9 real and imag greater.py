comp = input("enter a complex number : ")
print(comp[0])
real = comp[0]
imag = comp[len(comp) -2]
if(real > imag):
    print(f"real part {real} is greater than imaginary part {imag}")
elif(real < imag):
     print(f"imaginary part {imag} is greater than real part {real}")
else:
    print(f"imaginary part {imag} and real part {real} are equal")




comp = complex(input("enter a complex number : "))
real = comp.real
imag = comp.imag
if(real > imag):
    print(f"real part {real} is greater than imaginary part {imag}")
elif(real < imag):
     print(f"imaginary part {imag} is greater than real part {real}")
else:
    print(f"imaginary part {imag} and real part {real} are equal")
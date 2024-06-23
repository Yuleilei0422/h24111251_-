h=input("Input the height of the 1st ball:")
h=float(h)
m1=float(input("Input the mass of the 1st ball:"))
m2=float(input("Input the mass of the 2nd ball:"))
g=9.8
v1=(2*g*h)**0.5
print("The velocity of the 1st ball after slide:",v1)
v2 = 2 * m1 / (m1 + m2) * v1
print("The velocity of the 2nd ball after collision:",v2, "m/s")


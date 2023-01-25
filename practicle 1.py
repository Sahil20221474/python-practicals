import math

print ("please Enter the numbers a b c as shown in this standra form of eqn")
print("ax^2 +bx +c")
a = int(input("a :"))
b = int(input("b :"))
c = int(input("c :"))


d = ((b*b) - (4*a*c))
if d<0:
    print("this equation has no real roots")

else:
    t = math.sqrt(d)
    sol1 = ((-1 * b)+ t)/(2*a)
    sol2 = ((-1 * b)- t)/(2*a)
    print("solutions of this equation are:")
    print(sol1,sol2)
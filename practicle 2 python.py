n=int(input("enter a number:"))

if n > 1:

    for i in range(2, int(n/2)+1):

        if (n % i) == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")
else:
    print(n, "is not a prime number")
lower_value = 0
upper_value=n
print("The Prime Numbers in the range are: ")
for number in range(lower_value, upper_value + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number)

c = 2
while n!=0:
  for i in range(2,c):
    if c%i==0:
      break
  else:
    print(c,end=" ")
    n-=1
  c+=1
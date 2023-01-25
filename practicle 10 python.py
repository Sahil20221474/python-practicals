str1 = input("Please enter first string : ")
str2 = input("Please enter second string : ")

n = int(input("How many characters you want to swap: "))

x = str2[:n] + str1[n:]
y = str1[:n] + str2[n:]

print("Your first has become :- ", x)
print("Your second has become :- ",y)
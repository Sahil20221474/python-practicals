string = 'hello world! this is qwerty'
new_string = string.replace("w", "u" )
print(string)
print(new_string)
freq = {}
for i in string:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print("Count of all characters in",string, "is :", "\n " + str(freq))
str2=string.replace("l",'',1)
print(str2)
str3=string.replace("l",'')
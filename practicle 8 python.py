ch = input('Please enter a character: ')
no_names = ["zero", "one", "two",   "three", "four",
            "five", "six", "seven", "eight", "nine"]

if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <='Z')):
    print('The Given Character ', ch, "is an Alphabet")
    if(ch.islower()):
        print('The alphabet is in Lowercase')
    else:
        print('The alphabet is in Uppercase')

elif(ch >= '0' and ch <= '9'):
    print('The Given Character ', ch, "is a DIgit")
    print('In words', no_names[int(ch)])

else:
    print('The Given Character ', ch, "is a Special Character")
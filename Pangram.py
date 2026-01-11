num = input("Enter a number: ")


numcount = {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0,
}

for num1 in num:
    if num1 in numcount:
        numcount[num1] += 1
    
pangram = True
for count in numcount.values():
    if count == 0:
        pangram = False

if pangram:
    print("{} is a Pangram Number".format(num))

else:
    print("{} is not a Pangram Number".format(num))
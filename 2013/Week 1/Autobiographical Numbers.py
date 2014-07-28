num = input("Number: ")
isBiographical = True
for i in range(len(num)):
    lookupDigit = i
    digitCount = 0
    expectedNum = int(num[i])
    for j in range(0, len(num)):
        if (int(num[j]) == lookupDigit):
            digitCount+=1
    if (digitCount != expectedNum):
        isBiographical = False
if (isBiographical):
    print(num + " is autobiographical")
else: print(num + " is not autobiographical")
input()

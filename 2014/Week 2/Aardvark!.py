s = "aardvark"
c = 0
for char in input():
    if s[c] == char or s[c].upper() == char:
        c+=1
    if (c >= len(s)):
        print("Aardvark!")
        break
else:
    print("No aardvarks here :(")

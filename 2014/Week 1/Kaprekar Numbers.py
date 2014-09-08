def is_kaprekar(num):
    n = num**2
    s = str(n)
    for i in range(len(s)-1):
        n1 = int(s[0:i+1])
        n2 = int(s[i+1:])
        if n1 + n2 == num and n2 > 0:
            return True
    return False

print(is_kaprekar(2))

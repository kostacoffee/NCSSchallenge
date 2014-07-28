import math
def main():
    f = open("ncss-modified.bmp","rb")
    f.seek(10)
    offset = int.from_bytes(f.read(4), 'little')
    hSize = int.from_bytes(f.read(4), "little")
    width = int.from_bytes(f.read(4), "little")
    height = int.from_bytes(f.read(4), "little")
    f.seek(f.tell()+8)
    size = int.from_bytes(f.read(4), 'little')
    f.seek(offset)
    dataWidth = width*3
    padding = 4 - dataWidth%4
    if (padding ==4): padding = 0
    totalRowSize = dataWidth + padding
    i = 0
    number = 0
    text = ""
    currentByte = 0
    while (i < size):
        if (currentByte + padding == totalRowSize):
            i+=padding
            currentByte = 0
            f.seek(f.tell()+padding)
        byte = f.read(8)
        i+=8
        currentByte += 8
        LSB = [(b&1) for b in byte]
        LSB.reverse()
        for bit in LSB:
            number = (number << 1) | bit
        character = chr(number)
        if (character == "\x00"):
           break
        text += character
        number = 0
    print(text)

main()

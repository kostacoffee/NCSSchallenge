# Enter your code for "Triple-Double-Letter" here.
import re

def main():
    words = [word.strip() for word in open("words.txt",'r').readlines()]
    finalWords = []
    pattern = re.compile(r'([a-z])\1+')
    for word in words:
        matches = set(re.findall(pattern,word))
        if (len(matches) >= 3):
            finalWords.append(word)
    finalWords.sort()
    for word in finalWords:
        print(word)

main()

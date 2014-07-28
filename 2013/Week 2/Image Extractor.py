# Enter your code for "Image Extractor" here.
import re

def main():
    with open("site.html", 'r') as f: lines = f.readlines()
    for line in lines:
        line = re.findall(r'<img .*?src="(.*?)".*?>', line)
        for s in line:
            print(s)

main()

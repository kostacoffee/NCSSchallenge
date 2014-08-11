divs = []
for i in range(int(input())):
	divs.append(int(input()))

beats = int(input()) + 1
for i in range(1, beats):
	s = str(i) + ':'
	for div in divs:
		if (i%div == 0):
			s += 'X'
		else:
			s+= ' '
	s = s.strip(" ")
	print(' '*(len(str(beats))-len(str(i))) + s)






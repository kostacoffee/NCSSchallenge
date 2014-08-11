def count_collisions(text, keypad):
	words = text.split(' ')
	keyMaps = {}
	for word in words:
		word = word.lower()
		wordMap = []
		for c in word:
			wordMap.append(str(keypad[c]))
		wordMap = "".join(wordMap)
		if (wordMap not in keyMaps.keys()):
			keyMaps[wordMap] = 1
		else: keyMaps[wordMap] += 1
	colls = 0
	for val in keyMaps.values():
		if val > 1:
			colls += val
	return colls

def make_mapping(l):
	mapping = {}
	for i in range(len(l)):
		for letter in l[i]:
			mapping[letter] = i
	return mapping

mapping = make_mapping('  abc def ghi jkl mno pqrs tuv wxyz'.split())
print('This should be 4:', count_collisions('In a brief aside the bride cried', mapping))

mapping = make_mapping('  aei ou bcgh jkl mnd pqrs tfv wxyz'.split())
print('This should be 0:', count_collisions('In a brief aside the bride cried', mapping))
VOWELS = "aeiouAEIOU"
def removeVowels(word):
    return [c for c in word if c not in VOWELS]


def novowelsort(l):
    return sorted(l,key = removeVowels)

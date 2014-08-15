prefLines = open('preferences.txt').readlines()
preferences = {}
for pref in prefLines:
    pref = pref.strip().split(',')
    preferences[pref[0]] = int(pref[1])
sandwiches = list(enumerate(open('sandwiches.txt').readlines()))


for i in range(len(sandwiches)):
    sandwich = sandwiches[i]
    ingredients = sandwich[1].strip().split(',')
    score = 0
    for ingred in ingredients:
        if ingred not in preferences:
            next
        else:
            score += preferences[ingred]
    sandwiches[i] += (score,)

sandwiches.sort(key=lambda x: x[1])
sandwiches.sort(key=lambda x: len(x[1].split(',')), reverse=True)
sandwiches.sort(key=lambda x: x[2], reverse=True)
for s in sandwiches:
    print(s[1].strip())
if len(sandwiches) == 0:
    print("devo :(")

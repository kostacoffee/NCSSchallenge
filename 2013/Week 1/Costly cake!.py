# Enter your code for "Costly cake!" here.
sideLength = []
cakeCost = []
for i in range(1,3):
  side = input("Cake %i side length (cm): " %(i))
  sideLength.append(float(side))

  cost = input("Cake %i cost ($): " % (i))
  cakeCost.append(float(cost))

cake1Area = sideLength[0]**2
cake2Area = sideLength[1]**2
cake1Value = cakeCost[0]/cake1Area
cake2Value = cakeCost[1]/cake2Area
print("Cake 1 costs $%.2f per cm2 for %i cm2" % (cake1Value, cake1Area))
print("Cake 2 costs $%.2f per cm2 for %i cm2" % (cake2Value, cake2Area))
if cake1Value > cake2Value:
  print("Get cake 2!")
elif cake2Value > cake1Value:
  print("Get cake 1!")
else: print("Get either!")

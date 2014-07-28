# Enter your code for "Interleaving" her
results = []

def recInterleavings(str1,str2,result):
  if (len(str1) == 0 and len(str2) == 0):
    results.append(result)
  else:
    if (len(str1) >=1):
      recInterleavings(str1[1:],str2,result+str1[0])
    if (len(str2) >= 1):
      recInterleavings(str1,str2[1:],result+str2[0])

def interleavings(a,b):
  recInterleavings(a,b,"")
  return results


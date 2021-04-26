import random

# Generate alphabet characters list
letters = [chr(i) for i in range(ord('a'),ord('z')+1)]
letters = letters + [chr(i) for i in range(ord('A'),ord('Z')+1)]

lenLetters = len(letters)

counts = {}
for i in letters:
  counts[i] = 0

txt = ''
for i in range(10000):
  txt += letters[random.randint(0,lenLetters-1)]
  counts[txt[-1]]+=1

keys = list(counts.keys())
vals = list(counts.values())

zipped = zip(keys,vals)
zippedSorted = sorted(zipped, key=lambda x:x[1], reverse=True)

for i,j in enumerate(zippedSorted):
  print('{:02} | {:}: {:4}'.format(i,j[0],j[1]))

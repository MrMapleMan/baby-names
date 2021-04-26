import os
import sys

topDir = os.path.expanduser('~/Downloads/baby-names/')
with open(topDir+'names-unique.txt') as f:
  txt = f.read().splitlines()

names = txt
lengths = [0]*len(names)
for i,j in enumerate(names):
  try:
    lengths[i] = len(j)
  except:
    print("exception at "+str(i))
    sys.exit()

zipped = zip(names,lengths)
results = sorted(zipped, key=lambda x:x[1], reverse=True)

with open(topDir+'names-lengths.txt','w+') as f:
  for i,j in results:
    f.write('{:20} {:}\n'.format(i,j))
for i,j in results[:10]:
  print('',i,j)

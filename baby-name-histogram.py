# Author:      John Henrie
# Date:        04/09/2021
# Description: Read names & counts, determine total for all names,
#              write into report ('results.txt') with sorted results. 

import time
import os

print('Reading and processing name counts.')

t1 = time.time()
topDir = os.path.expanduser('~/Downloads/baby-names/')
with open(topDir + 'names-unique.txt') as f:
  txt = f.read().splitlines()

nameCounts = {}

# Initialize counts for all names at zero
t2 = time.time()
for line in txt:
  nameCounts[line] = 0
t3 = time.time()

# Process combined record for all years
with open(topDir + 'combined.txt') as f:
  txt = f.readlines()
for i in txt:
  vals = i.split(',')
  nameCounts[vals[0]] += int(vals[2])
t4 = time.time()

k = nameCounts.keys()
v = nameCounts.values()
results = list(zip(k,v))
results = sorted(results, key = lambda x:(x[1],x[0]),reverse=True)

t5 = time.time()
# Save results
with open(topDir + 'results.txt','w+') as f:
  s = '{:^10} {:^30} {:^10}\n'.format('Rank','Name','Count')
  f.write(s)
  f.write('-'*10+' '+'-'*30+' '+'-'*10+'\n')
  for i,j in enumerate(results):
    s = '{:^10,} {:^30} {:^10,}\n'.format(i+1,j[0],j[1])
    f.write(s)
t6 = time.time()
print('Results written to ' + topDir + 'results.txt.')
print()
print((t5-t1)*1000.,(t6-t5)*1000.)
print()

for i,j in enumerate(results[:10]):
  print('  {:2} {:10} {:10,}'.format(i+1,j[0],j[1])) 

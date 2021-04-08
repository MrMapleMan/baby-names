import time
import os

t1 = time.time()
topDir = os.path.expanduser('~/Downloads/baby-names/')
with open(topDir + 'names-unique.txt')) as f:
  txt = f.read().splitlines()

nameCounts = {}

# Initialize counts for all names at zero
t2 = time.time()
for line in txt:
  nameCounts[line] = 0
t3 = time.time()

# Process combined record for all years
with open(topDir + 'combined.txt')) as f:
  txt = f.readlines()
for i in txt:
  vals = i.split(',')
  nameCounts[vals[0]] += int(vals[2])
t4 = time.time()

k = nameCounts.keys()
v = nameCounts.values()
results = list(zip(k,v))
results = sorted(results, key = lambda x:x[1],reverse=True)

t5 = time.time()
# Save results
with open(topDir + 'results.txt'),'w+') as f:
  for i,j in enumerate(results):
    s = '{:^10,} {:^30} {:^10,}\n'.format(i+1,j[0],j[1])
    f.write(s)
t6 = time.time()
print((t5-t1)*1000.,(t6-t5)*1000.)
print(results[-10:])


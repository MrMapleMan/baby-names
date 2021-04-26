import time
t1 = time.time()
with open('/usr/local/google/home/jhenrie/Downloads/baby-names/yob2019.txt') as f:
  txt = f.readlines()

nameCounts = {'M':0,'F':0}
mNames = set()
fNames = set()

# Process lines
t2 = time.time()
for line in txt:
  vals= line.split(',')
  nameCounts[vals[1]] += int(vals[2])
  if vals[1] == 'M':
    mNames.add(vals[0])
  else:
    fNames.add(vals[0])
t3 = time.time()
print('\n{:8} {:,} {:4.1f}%\n{:8} {:,} {:4.1f}%\n{:8} {:,}'.format('Male:',nameCounts['M'],
     100.0*nameCounts['M']/(nameCounts['M']+nameCounts['F']),
     'Female:',nameCounts['F'],
     100.0*nameCounts['F']/(nameCounts['M']+nameCounts['F']),
     'Total:',nameCounts['M']+nameCounts['F']))
t4 = time.time()
print('\nUnique male names:   {:>7,} {:4.1f}%\nUnique female names: {:>7,} {:4.1f}%\n'.format(len(mNames),
      100.*len(mNames)/(len(mNames)+len(fNames)),len(fNames),
      100.*len(fNames)/(len(mNames)+len(fNames))))
# print((t3-t1)*1000.,(t3-t2)*1000.,(t4-t1)*1000.)

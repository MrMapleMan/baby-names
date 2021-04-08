import time
t1 = time.time()
with open('/usr/local/google/home/jhenrie/Downloads/baby-names/yob2019.txt') as f:
  txt = f.readlines()

nameCounts = {'M':0,'F':0}

# Process lines
t2 = time.time()
for line in txt:
  vals= line.split(',')
  nameCounts[vals[1]] += int(vals[2])
t3 = time.time()
print('{:8} {:,}\n{:8} {:,}\n{:8} {:,}'.format('M:',nameCounts['M'],'F:',nameCounts['F'],'Total:',nameCounts['M']+nameCounts['F']))
t4 = time.time()
print((t3-t1)*1000.,(t3-t2)*1000.,(t4-t1)*1000.)

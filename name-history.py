# Plot the popularity of a name over time

import os
import sys
import subprocess
import re
import matplotlib.pyplot as pp

fa = re.findall

if len(sys.argv) > 1:
  name = sys.argv[1]
else:
  warning('Need to provide a name as first argument.')
  sys.exit()

# Generate list of names from each file
downloadDir = os.path.expanduser('~/Downloads/baby-names/')
directory = downloadDir + 'yob*txt'
command = 'grep ' + name + ' ' + directory + ' > /tmp/name-results.txt'
subprocess.run(command,shell=True)

# Get all years
command = 'ls ' + directory +' | grep -oP "\d+" > /tmp/year-results.txt'
subprocess.run(command, shell=True)

# Save years in variable
years = {}
with open('/tmp/year-results.txt') as f:
  yearLines = f.read().splitlines()
for i in yearLines:
  years[i] = 0
    
# Add values from name-results
with open('/tmp/name-results.txt') as f:
  nameResultsText = f.read()
vals = re.findall('yob(\d+)\.txt.*?,(\d+)',nameResultsText)
for i in vals:
  years[i[0]] += int(i[1])
  
keys = list(years.keys())
values = list(years.values())

pp.plot([int(i) for i in keys],values)
pp.title('Popularity of Name ' + name + ' Over Time')
pp.show()
"""
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
print(results[:10])
"""

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
  
doSave = False
if len(sys.argv) > 2:
  if(sys.argv[2] == 'True'):
    doSave = True
  elif(sys.argv[2] == 'False'):
    doSave = False

# Generate list of names from each file
downloadDir = os.path.expanduser('~/Downloads/baby-names/')
directory = downloadDir + 'yob*txt'
command = 'grep ' + name + ', ' + directory + ' > /tmp/name-results.txt'
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

print("\nTotal count for " + name + ": {:,}".format(sum(values)))

pp.plot([int(i) for i in keys],values)
pp.title('Popularity of Name ' + name + ' Over Time')
pp.savefig(os.path.expanduser('~/Python/Misc/2021/Plots/' + name + '.png'))
pp.show()

# Get name rank from results.txt report
with open(downloadDir+'results.txt') as f:
  resultsTxt = f.read()
rank = re.findall('([\d,]+)(?: )+'+name+'\\b',resultsTxt)[0]
numNames = re.findall('\n.*?([\d,]+).*?\n',resultsTxt)[-1]
percent = float(rank.replace(',','')) / float(numNames.replace(',','')) * 100.
print('Name popularity ranking for ' + name + ': ' + rank + ' of ' + numNames + ' (top %.1f%%).'%(percent))

'''
# Groups all names with same count as single rank entry
counts = fa('.{15}.*?([\d,]+).*?\n',resultsTxt)
counts = list(set(counts)) # Remove duplicates
counts = [int(i.replace(',','')) for i in counts]
counts = sorted(counts,reverse=True)
properRanking = counts.index(sum(values)) + 1
numNames = len(counts)
percent = float(properRanking) / float(numNames) * 100.
print('Name popularity ranking for ' + name + ': {:,} of {:,} (top {:.1f}%)'.format(properRanking,numNames,percent))
'''

print('')
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

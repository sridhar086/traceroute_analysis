#!/usr/bin/python
#!/usr/bin/python
import os
import shlex, subprocess
import sys
import networkx
import scipy
import numpy as ny
import pylab as pl

from collections import defaultdict
#IP_list = defaultdict(list)
hop1 = defaultdict(list)
hop2 = defaultdict(list)
hop3 = defaultdict(list)
hop4 = defaultdict(list)
hop5 = defaultdict(list)

f= open('full_file.txt', 'r')
cmp1='T'
hello = 0
for line in f:
	hello = hello+1
	args = line.split()
	length = len(args)

	if args[0] != cmp1:			#To get to the first set of data
		continue

	i = (length - 12) + 1
	j = 13
	#print "The length is ",i
	iterator=i-2
	
	for z in range(0,iterator):
		#print j
		
		if args[j] == 'q':
			j=j+1
			if z == iterator-1:
				break
			else:
				continue
		
		arg=args[j].split(",")
		if j==13:
			hop1[str(arg[0])].append(arg[1])
			j=j+1
		elif j==14:
			hop2[str(arg[0])].append(arg[1])
			j=j+1
		elif j==15:
			hop3[str(arg[0])].append(arg[1])
			j=j+1
		elif j==16:
			hop4[str(arg[0])].append(arg[1])
			j=j+1
		elif j==17:
			hop5[str(arg[0])].append(arg[1])
			j=j+1



		if z == 4:
			break
		

IP1=defaultdict(list)

IP2=defaultdict(list)
IP3=defaultdict(list)
IP4=defaultdict(list)
IP5=defaultdict(list)
sort=dict()
for element in hop1:
	IP1[element]=min(hop1[element])
	
for element in hop2:
	IP2[element]=min(hop2[element])

for element in hop3:
	IP3[element]=min(hop3[element])

for element in hop4:
	IP4[element]=min(hop4[element])

for element in hop5:
	IP5[element]=min(hop5[element])

'''
print IP1
print IP2
print IP3
print IP4
print IP5
'''

h1="129.186.6.252"
h2="129.186.254.131"
h3="192.245.179.4"
h4="192.245.179.166"
h5="65.77.99.177"

m1=IP1[h1]
m2=IP2[h2]
m3=IP3[h3]
m4=IP4[h4]
m5=IP5[h5]


print h1,"\t",m1
print h2,"\t",m2
print h3,"\t",m3
print h4,"\t",m4
print h5,"\t",m5

#print ny.std(hop1[h1])

pl.plot(hop1[h1],'ro') 
pl.show()

pl.plot(hop2[h2],'ro') 
pl.show()


pl.plot(hop3[h3],'ro') 
pl.show()


pl.plot(hop4[h4],'ro') 
pl.show()


pl.plot(hop5[h5],'ro') 
pl.show()





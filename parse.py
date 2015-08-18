#!/usr/bin/python
import os
import shlex, subprocess
import sys

#This commented part of code is to execute command to read warts file using the scamper tool



'''
print "--------Program to analyse the traceroute data-------- \n"
print "Enter the path of sc_analysis_dump tool and the warts.creating file that is to be analysed with a space inbetween \n"
print "For example, if path of tool is scamper/utils/sc_analysis_dump/sc_analysis_dump and file is daily.l7.t1.c000027.20070913.amw-us.warts.creating \nThen input is scamper/utils/sc_analysis_dump/sc_analysis_dump daily.l7.t1.c000027.20070913.amw-us.warts.creating"
command_line = raw_input()

#cmd = "./scamper/utils/sc_wartsdump/sc_wartsdump daily.l7.t1.c000027.20070913.amw-us.warts.creating"
#args = shlex.split(cmd)

command_line  = "./" + command_line + " | cat > parsed_file.txt"
os.system(command_line)

'''
#print args
#command += args[0]
#p = subprocess.Popen(args)

'''
from subprocess import Popen, PIPE
process = Popen(["./scamper-cvs-20141101/utils/sc_wartsdump/sc_wartsdump", "daily.l7.t1.c000027.20070913.amw-us.warts.creating"], stdout=PIPE)
(output, err) = process.communicate()
sprint output
exit_code = process.wait()
'''

#cmp = 'R'
cmp1 = 'T'
mat_2d = []
f = open('file.txt', 'r')
print "Reading fromt the parsed file - 'file.txt'"
print "Working on the parsing the data"
os.system("date")
check = 0
check_cmp = 0
line_check = 0
for line in f:
	#print line;
	args = line.split()
	length = len(args)
	iterator = 13
	
	if args[0] != cmp1:			#To get to the first set of data
		continue 
	#print "The existing length is ", check_cmp
	#print "The length of new line is" , length
	check = check_cmp			#retaining the previous high (in case a new high comes) 	
	if length > check_cmp:
		check_cmp = length		#becomes the new high value
						#the new length (new IP addresses that would be added to the existing 2D matrix)	

	'''
	if args[6] == cmp:
		print "This one has a reply"
		print line
		break
	'''
	
	if not mat_2d:				#If the elements are added for the first time			
		#print "2D array is totally empty, adding the first element"
		#print "The changed length is ", check_cmp
		inner_iterator = 0		#inner iterator for second dimension
		while (iterator < length):
			mat_2d.append([])	#adding a new list in the first index
			arg_split = args[iterator].split(',')
			#print iterator
			#print length
			#print arg_split
			if not mat_2d:		#Again, if the element is added for the first time
				mat_2d[inner_iterator].append(arg_split[0])
				inner_iterator += 1
			else:
				mat_2d[inner_iterator].append(arg_split[0])
				inner_iterator += 1
			iterator += 1
	
	else:
	
		#print "The changed length is ", check_cmp
		
		#If the new line has less or equal elements then this block of code will work
		if (length < check or length == check):
			inner_iterator = 0
						
			while (iterator < length):
				arg_split = args[iterator].split(',')
				trans = 0
				for i in range(len(mat_2d[inner_iterator])):
					#print "Element in this ", mat_2d[inner_iterator][i]					
					if mat_2d[inner_iterator][i] == arg_split[0]:
						#print "Element is present"						
						trans = 1
				if trans == 0:				
					mat_2d[inner_iterator].append(arg_split[0])
								
				inner_iterator += 1
				iterator += 1
		
		#If the new line has more elements than the existing ones, will append new lists dynamically
		elif (length > check):
			#print iterator
			#print length			
			#print elements_to_add
			inner_iterator = 0
			while (iterator < length):
				#print "The iterator value is", iterator				
				arg_split = args[iterator].split(',')				
				if (iterator >= check):
					#print iterator, inner_iterator
					mat_2d.append([])
					mat_2d[inner_iterator].append(arg_split[0])
					inner_iterator += 1	
					iterator += 1
					#print "new element is added continued with next IP addr"					
					continue
					
				trans = 0		
				for i in range(len(mat_2d[inner_iterator])):
					#print "Element in this ", mat_2d[inner_iterator][i]					
					if mat_2d[inner_iterator][i] == arg_split[0]:
						#print "element is present"
						trans = 1
				if trans == 0:				
					mat_2d[inner_iterator].append(arg_split[0])
				
				inner_iterator += 1	
				iterator += 1
		else:
			print "Both failed, Mistake in programming"
	line_check += 1
	
	
		
print mat_2d, "\n"

print "writing to file - 'analyse.txt'"	
os.system("date")
write_file = open('analyse.txt', 'w')
write_file.write(str(mat_2d))


# End of program #


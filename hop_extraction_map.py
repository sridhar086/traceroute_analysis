#!/usr/bin/python
import os
import shlex, subprocess
import sys
import networkx
import scipy
import numpy



def graph_plot():
	import networkx as nx
	import matplotlib.pyplot as plt
	G=nx.Graph()

	for key in new_dict:
		x,y=key
		if new_dict[key] == 1:
			G.add_edge(x, y, weight=new_dict[key])


	graph_pos=nx.spring_layout(G)
	#graph_pos=nx.random_layout(G)
	nx.draw(G,graph_pos)
	#nx.draw_networkx_nodes(G,graph_pos)
	#nx.draw_networkx_edges(G,graph_pos)
	#nx.draw_networkx_labels(G, graph_pos)
	plt.show()



def print_matrices():
	from pprint import pprint
	res1 = dict((v,k) for k,v in src_dict.iteritems())
	pprint(res1, f_src)
	res2 = dict (zip(des_dict.values(),des_dict.keys()))
	pprint(res2,f_des)
	pprint(new_dict,f_mat)





cmp1 = 'T'
src = []
src_dict = {}
des = []
des_dict = {}
matrix = []
hop = []
new_dict = {}	#
flag = 0
f= open('file4.txt', 'r')
f1 = open('file_parse.txt','w')
f_src = open('source_ip.txt','w')
f_des = open('dest_ip.txt','w')
f_mat = open('matrix.txt','w')
print "Reading from the parsed file - 'file.txt'"
print "Working on the parsing the data"
os.system("date")

for line in f:
	args = line.split()
	length = len(args)
	ip = []
	
	if args[0] != cmp1:			#To get to the first set of data
		continue 
	if flag == 0:
		flag = 1
		#if args[6] == 'R':
		i = (length - 12) + 1
		j = 13;
		#print "The length is ",length
		#print "The number of IP addresses is ",i
		for num in range(0,i):
			if num == 0:
				ip.append(args[1])
			elif num < (i-1):
				arg = args[j].split(',')
				ip.append(arg[0])
				j = j + 1
			if num == (i-1):
				ip.append(args[2])				
						
		for nu in range(0,i):
			#f_src.write(ip[nu])
			#f_src.write("\n")
			src_dict[ip[nu]]=nu
			p = nu
			check = 0
			for num in range(0,i):
				if args[6] == 'R':
					if nu == 0:
						#f_dst.write(ip[num])
						des_dict[ip[num]]=num
						#f_dst.write("\n")	
					#File adding at the end
					'''
					src.append(ip[nu])
					f1.write("\t")
					des.append(ip[num])
					f1.write(ip[num])
					f1.write("\t")
					f1.write(str(nu))
					f_mat.write(str(nu))
					f_mat.write("\t")
					f1.write("\t")
					f1.write(str(num))
					f_mat.write(str(num))
					f_mat.write("\t")
					f1.write("\t")
					f1.write(str(p))
					f_mat.write(str(p))
					f_mat.write("\n")
					f1.write("\n")
					'''
					mat = str(nu) +' '+str(num)
					matrix.append(mat)
					key = nu,num
					new_dict[key] = p
					hop.append(p)
					if ((nu == 0) or (check == 1)):
						p = p + 1
					elif nu > 0:
						if p == 0:
							p = p + 1
							check = 1
						else:
							p = p - 1
	
				if args[6] == 'N':
					
					if nu == 0:
						#f_dst.write(ip[num])
						des_dict[ip[num]]=num
						#f_dst.write("\n")	
					if i == nu+1:
						if (i == nu+1) and (i == num+1):
							#I am gonna add it to file at the end
							'''
							src.append(ip[nu])
							f1.write(ip[nu])
							f1.write("\t")
							des.append(ip[num])
							f1.write(ip[num])
							f1.write("\t")
							f1.write(str(nu))
							f_mat.write(str(nu))
							f_mat.write("\t")
							f1.write("\t")
							f1.write(str(num))
							f_mat.write(str(num))
							f_mat.write("\t")
							f1.write("\t")
							f1.write('0')
							f_mat.write('0')
							f_mat.write("\n")
							f1.write("\n")
							'''
							mat = str(nu) +' '+str(num)
							matrix.append(mat)
							key = nu,num
							new_dict[key] = 0
							hop.append('0')				

						else:
							#this is not needed because its special character
							'''
							src.append(ip[nu])
							f1.write(ip[nu])
							f1.write("\t")
							des.append(ip[num])
							f1.write(ip[num])
							f1.write("\t")
							f1.write(str(nu))
							f_mat.write(str(nu))
							f_mat.write("\t")
							f1.write("\t")
							f1.write(str(num))
							f_mat.write(str(num))
							f_mat.write("\t")
							f1.write("\t")
							special_char = "?"
							f1.write(special_char)
							f_mat.write(special_char)
							f_mat.write("\n")
							f1.write("\n")
							mat = str(nu) +' '+str(num)
							matrix.append(mat)
							key = str(nu) +','+str(num)
							new_dict[key] = special_char
							hop.append(special_char)
							'''
										
								
					elif i == num+1:
						#this is not needed becauseif its no reply just leave it	
						'''						
						src.append(ip[nu])
						f1.write(ip[nu])
						f1.write("\t")
						des.append(ip[num])
						f1.write(ip[num])
						f1.write("\t")
						f1.write(str(nu))
						f_mat.write(str(nu))
						f_mat.write("\t")
						f1.write("\t")
						f1.write(str(num))
						f_mat.write(str(num))
						f_mat.write("\t")
						f1.write("\t")
						special_char = "?"
						f1.write(special_char)
						f_mat.write(special_char)
						f_mat.write("\n")
						f1.write("\n")
						mat = str(nu) +' '+str(num)
						matrix.append(mat)
						key = str(nu) +','+str(num)
						new_dict[key] = special_char
						hop.append(special_char)
						'''
						
					else:	
						#This part is to print on file which I am gonna do at end
						'''
						
						src.append(ip[nu])
						f1.write(ip[nu])
						f1.write("\t")
						des.append(ip[num])
						f1.write(ip[num])
						f1.write("\t")
						f1.write(str(nu))
						f_mat.write(str(nu))
						f_mat.write("\t")
						f1.write("\t")
						f1.write(str(num))
						f_mat.write(str(num))
						f_mat.write("\t")
						f1.write("\t")
						f1.write(str(p))
						f_mat.write(str(p))
						f_mat.write("\n")
						f1.write("\n")
						'''
						mat = str(nu) +' '+str(num)
						matrix.append(mat)
						key = nu,num
						new_dict[key] = p
						hop.append(p)
						if ((nu == 0) or (check == 1)):
							p = p + 1
						elif nu > 0:
							if p == 0:
								p = p + 1
								check = 1
							else:
								p = p - 1					
									
	else:
		#print "This is next iteration"
		i = (length - 12) + 1
		k = j
		j = 13;
		outer_index = j 
		#print "The length is ",length
		#print "The number of IP addresses is ",i
		
		for nu in range(0,i):
			outer_iterator = nu
			inner_iter=j
			for num in range(0,i):
				#inner_iter=j
				if nu == 0:
					#print "first set"
					
					if num == 0:
						arg=args[1].split(",")
						ip1 = arg[0]
						ip2 = arg[0]
						if ip1 in src_dict and ip2 in des_dict:
							#print "not adding any ip address"
							index1=src_dict.get(ip1)
							index2=des_dict.get(ip2)
							mat_key=index1,index2
							if not mat_key in new_dict:
								new_dict[mat_key] = 0
							
						else:
							#source is same and hence it will enever enter here! still
							print "It will not come here because source is same"
							index = len(src_dict.keys())							
							src_dict[ip1]=index
							des_dict[ip2]=index
							mat_key=index,index
							new_dict[mat_key] = 0
							
							
							
					elif num+1 == i:
						if args[6] == 'R':
							arg1=args[1].split(",")
							arg2=args[2].split(",")
							ip1 = arg1[0]
							ip2 = arg2[0]
							if ip1 in src_dict:
								index1=src_dict.get(ip1)
								if ip2 in src_dict:
									index2=des_dict.get(ip2)
									#provision to change the existing value
									mat_key=index1,index2
									if not mat_key in new_dict:
										new_dict[mat_key] = num
								else:
									index2 = len(src_dict.keys())
									src_dict[ip2]=index2
									des_dict[ip2]=index2
									mat_key=index1,index2
									new_dict[mat_key] = num		
							elif ip2 in src_dict:
								No#This condition will not be necessary
							else:
								No #This is also not necessary
								true =1
						elif args[6] == 'N':
							arg1=args[1].split(",")
							arg2=args[2].split(",")
							ip1 = arg1[0]
							ip2 = arg2[0]
							if not (ip1 in src_dict and ip1 in des_dict):
								#this part of code might not be used
								index = len(src_dict.keys())
								src_dict[ip1] = index
								des_dict[ip1] = index
							if not (ip2 in src_dict and ip2 in des_dict):
								#print "The unknown element added"
								index = len(src_dict.keys())
								src_dict[ip2] = index
								des_dict[ip2] = index
							#provision for changing exisitng value
					else:
						#condition for other iterations
						arg1=args[1].split(",")
						arg2=args[inner_iter].split(",")
						ip1 = arg1[0]
						ip2 = arg2[0]
						#print ip2
						inner_iter = inner_iter + 1
						if ip1 in src_dict:
							index1=src_dict.get(ip1)
							if ip2 in src_dict:
								#print "No element added"
								index2=des_dict.get(ip2)
								mat_key=index1,index2
								#provision to change exisitng value should be done here
								if not mat_key in new_dict:
									new_dict[mat_key] = num	
															
							else:
								#print "adding new element"
								index2 = len(src_dict.keys())
								src_dict[ip2]=index2
								des_dict[ip2]=index2
								mat_key=index1,index2
								new_dict[mat_key] = num
						elif ip2 in src_dict:
								No#This condition will not be necessary
						else:
							No #This is also not necessary

				elif nu+1 == i:
					#print "third set"
					if args[6] == 'R':
						if num == 0:
							arg1=args[2].split(",")
							arg2=args[1].split(",")
							ip1 = arg1[0]
							ip2 = arg2[0]
							
							index1=src_dict.get(ip1)
							index2=des_dict.get(ip2)
							mat_key=index1,index2
							if not mat_key in new_dict:	
								new_dict[mat_key]=outer_iterator
							outer_iterator = outer_iterator - 1
					
						elif num+1 == i:
							arg1=args[2].split(",")
							arg2=args[2].split(",")
							ip1 = arg1[0]
							ip2 = arg2[0]
							index=src_dict.get(ip1)
							mat_key=index,index
							if not mat_key in new_dict:
								new_dict[mat_key]=0
							
						else:
							arg1=args[2].split(",")
							arg2=args[inner_iter].split(",")
							ip1 = arg1[0]
							ip2 = arg2[0]
							inner_iter = inner_iter + 1
							index1=src_dict.get(ip1)
							index2=des_dict.get(ip2)
							mat_key=index1,index2
							if not mat_key in new_dict:	
								new_dict[mat_key]=outer_iterator
							outer_iterator = outer_iterator - 1
							

					if args[6] == 'N':
						if num+1 == i:
							arg1=args[2].split(",")
							arg2=args[2].split(",")
							ip1 = arg1[0]
							ip2 = arg2[0]
							index=src_dict.get(ip1)
							mat_key=index,index
							if not mat_key in new_dict:
								new_dict[mat_key]=0

				else:
					
					#print nu,num, i, outer_index
					
					if num == 0:
						
						arg1=args[outer_index].split(",")
						ip1 = arg1[0]
						
						arg2=args[1].split(",")
						ip2=arg2[0]
						index1 = src_dict.get(ip1)
						index2 = src_dict.get(ip2)
						mat_key = index1,index2
						if not mat_key in new_dict:
							new_dict[mat_key] = abs(nu-num)
						
					elif num+1 == i:
						
						arg1=args[outer_index].split(",")
						ip1 = arg1[0]
						
						arg2=args[2].split(",")
						ip2=arg2[0]
						if args[6] == 'N':
							no =1	#print "If its a no reply"
						if args[6] == 'R':
							index1 = src_dict.get(ip1)
							index2 = src_dict.get(ip2)
							mat_key = index1,index2
							if not mat_key in new_dict:
								new_dict[mat_key] = abs(nu-num)
							#provision to see old value and add new one
					else:
						
						arg1=args[outer_index].split(",")
						ip1 = arg1[0]
						
						
						arg2=args[inner_iter].split(",")
						ip2=arg2[0]
						inner_iter = inner_iter + 1
						index1 = src_dict.get(ip1)
						index2 = src_dict.get(ip2)
						mat_key = index1,index2
						if not mat_key in new_dict:
							new_dict[mat_key] = abs(nu-num)
									
			if nu != 0:
				outer_index = outer_index+1



graph_plot()
print_matrices()




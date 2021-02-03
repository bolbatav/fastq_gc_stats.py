#!/usr/bin/env python3
import itertools
import argparse

parser=argparse.ArgumentParser(description='''The script splits Fastq files by specified ranges of GC-content in reads. Reads that don't match any specified range will be moved to the "unassigned.fastq" file. Be careful: the sctipt does NOT overwrite files, but appends them. Be sure not to end up with files with duplicate reads.''')
parser.add_argument('-f', '--file', type=str, metavar='', required=True, help='Input file to analyze.')
parser.add_argument('-r', '--ranges', type=str, metavar='', required=True, help="Non-overlapping ranges of reads' GC-content for read sorting. Use a single non-spaced line. Example: 0.2:0.3,0.4:0.5")
parser.add_argument('-p', '--prefix', type=str, metavar='', required=False, help='Prefix (usually path to directory) of the output files.')
arguments=parser.parse_args()

ranges=arguments.ranges
ranges=ranges.split(',')
for i in range(len(ranges)):
	ranges[i]=ranges[i].split(':')
if not arguments.prefix:
	prefix=''
else:
	prefix=arguments.prefix
outlist=[]
for r in ranges:
	outlist+=[prefix+r[0]+'-'+r[1]+'.fastq']
for i in range(len(ranges)):
	ranges[i][0]=float(ranges[i][0])
	ranges[i][1]=float(ranges[i][1])
outlist+=[prefix+'unassigned.fastq']
with open(arguments.file, 'r') as infile:
	for i in range(len(outlist)):
		outlist[i]=open(outlist[i], 'a')
	while True:
		lines=[]
		for _ in range(4):
			lines+=[infile.readline()]
		if '' in lines:
			for i in range(len(outlist)):
				outlist[i].close()
			break
		gc=(lines[1].upper().count('G')+lines[1].upper().count('C'))/len(lines[1].strip())
		assigned=False
		for i in range(len(ranges)):
			if ranges[i][0] <= gc <= ranges[i][1]:
				lines=''.join(lines)
				outlist[i].write(lines)
				assigned=True
				break
			else:
				continue
		if not assigned:
			lines=''.join(lines)
			outlist[-1].write(lines)
	

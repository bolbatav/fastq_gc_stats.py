#!/usr/bin/env python3
import itertools
import argparse
import os
import seaborn as sns

parser=argparse.ArgumentParser(description='The script is designed to analyze GC-content of reads in Fastq-files.')
parser.add_argument('-f', '--file', type=str, metavar='', required=True, help='Input file to analyze.')
parser.add_argument('-o', '--out', type=str, metavar='', required=False, help='Name of the output file. If not specified the output file will not be saved.')
arguments=parser.parse_args()

inputf=arguments.file
output=arguments.out
gc=[]
with open(inputf, 'r') as inf:
	for line in itertools.islice(inf, 1, None, 4):
		gc+=[(line.upper().count('G')+line.upper().count('C'))/len(line.strip())]
#Plotting
plot = sns.displot(gc, kind = "kde", fill=True)
plot.set(xlabel = 'GC - content', 
		 ylabel = 'Density', title='Distribution of GC-content')
plot.savefig('G_C_Distribution.png')

if output:
	for i in range(len(gc)):
		gc[i]=str(gc[i])
	gc='\n'.join(gc)
	with open((output), 'w') as outf:
		outf.write(gc)

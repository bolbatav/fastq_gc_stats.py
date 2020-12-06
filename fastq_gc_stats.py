#!/usr/bin/env python3
import itertools
import argparse
import os
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

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
title_font = {'size':'20', 'color':'black', 'weight':'bold'}
axis_font = {'size':'14', 'color':'black', 'weight':'bold'}
sns.displot(gc, kind = "kde", fill=True)
sns.despine( trim=True)
plt.xlabel('GC content', **axis_font)
plt.ylabel('Density', **axis_font)
plt.title('Distribution of GC content', **title_font)
plt.xticks(np.arange(0,1,0.025), rotation = 60)
plt.gcf().set_size_inches(16, 10)
plt.savefig('G_C_Distribution.png', dpi = 300)

if output:
	for i in range(len(gc)):
		gc[i]=str(gc[i])
	gc='\n'.join(gc)
	with open((output), 'w') as outf:
		outf.write(gc)

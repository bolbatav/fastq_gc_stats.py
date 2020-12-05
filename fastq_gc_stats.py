#!/usr/bin/env python3
import itertools
import argparse
import os

parser=argparse.ArgumentParser(description='The script is designed to analyze GC-content of reads in Fastq-files.')
parser.add_argument('-f', '--file', type=str, metavar='', required=True, help='Input file to analyze.')
parser.add_argument('-o', '--out', type=str, metavar='', required=False, help='Name of the output file. If not specified the output file will not be saved.')
arguments=parser.parse_args()

inputf=arguments.file
output=arguments.out
gc=[]
with open(inputf, 'r') as inf:
	for line in itertools.islice(inf, 1, None, 4):
		gc+=[str((line.upper().count('G')+line.upper().count('C'))/len(line))]

if output:
	gc='\n'.join(gc)
	with open((output), 'w') as outf:
		outf.write(gc)

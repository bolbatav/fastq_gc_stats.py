# fastq_sort_GenHack2020

This code was made by "Seriously?" team as a part of Metagenome Binning assignment for GenHack 2020.

fastq_gc_stats.py is designed to collect statistics of raw reads' GC-content in FASTQ files. The output may contain just an image or a file with raw GC-content stats.

fastq_gc_split.py is designed to split FASTQ files by specified ranges of reads' GC-content. The output is at least two files: the one that contains reads with specified GC-content and the one for the remaining reads. You may split a file for into as many parts as you want.

Use -h option for description.

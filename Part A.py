import sys
import scipy
import numpy as np
import matplotlib.pyplot as plt
import pandas.plotting as scatter_matrix
import pandas as pd
dataset = pd.read_csv('gene_table.txt',names=['gene_name','gene_biotype','chromosome','strand','transcript_count'])
#1
print("Point 1 :")
number_of_gene=dataset.shape[0]
print("The total number of genes = "+ str(number_of_gene))
Grouped=dataset.groupby(dataset['gene_biotype'])
print("The number of diffrent gene biotypes = "+str(len(Grouped))+"\n")

#2
print("Point 2 :")
Minimum=dataset.transcript_count.min()
Maximum=dataset.transcript_count.max()
Average=dataset.transcript_count.mean()
Median=dataset.transcript_count.median()
print("The Minimum number of known isoforms = " +str(Minimum))
print("The Maximum number of known isoforms = "+str(Maximum))
print("The Average number of known isoforms = "+str(Average))
print("The Median number of known isoforms = "+str(Median)+"\n")


#3
print("Point 3 : ")
#plotting
Grouped_Chromo=dataset.groupby(dataset['chromosome']).size()

Grouped_Chromo.plot.bar(figsize=(20, 5))
plt.xlabel('Chromosome')
plt.ylabel('Number of genes')
plt.show()

#number of gene for each chromosome
print("The number of genes of eah chromosome = ")
arr=[]
for chromosome,iterate in dataset.groupby(dataset['chromosome']):
    arr.append((len(iterate),chromosome))
arr.sort()
print(arr)

#4
print("Point 4 : ")
print("The precentage of genes located on strand + of each chromose :")
for chromosome,iterate in dataset.groupby(dataset['chromosome']):
    number_plus=float(len(iterate[iterate['strand']=="+"]))
    percentage=100* number_plus/len(iterate)
    print (chromosome)
    print(percentage)
print("\n")
    
#5
print("Point 5 :")
print("The average number of transcripts associated to genes belonging to the biotype : ")
Grouped=dataset.groupby(dataset['gene_biotype'],as_index=False).aggregate(pd.DataFrame.mean)[['gene_biotype','transcript_count']]
print(Grouped)
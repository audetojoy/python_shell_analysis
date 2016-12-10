
# coding: utf-8

# In[8]:

import pandas as pd
import matplotlib.pyplot as plt
# get_ipython().magic('matplotlib inline')
import sys

# In[7]:
filename = sys.argv[1]
print( "you are using file:")
print(filename)
# import data using pandas
human_chr21 = pd.read_csv(filename, sep="\t")
human_chr21



# In[9]:

# calculate proportions
# save them as new column in existing dataframe

human_chr21['gc_content'] = human_chr21["gc_bases"] /    (human_chr21['win_end'] - human_chr21['win_start'])

human_chr21['gene_content'] = human_chr21['exon_bases'] /    (human_chr21['win_end'] - human_chr21['win_start'])


# In[11]:

# make a nice plot of GC content vs. Gene Content
plt.plot(human_chr21['gc_content'], human_chr21['gene_content'], 'o')
plt.xlabel('GC Content')
plt.ylabel('Gene Content')
# save figure to an appropriate file
plt.savefig('gene_vs_gc1.png')
#plt.show()
plot_file_name = filename + '.plot.png'
plt.savefig(plot_file_name)



import os
import pandas as pd 

path = './covidonly x-rays'
full_path = './Complete Data Set'
metadata = pd.read_csv('metadata_processed.csv')

print(metadata.groupby(['finding']).agg({'filename':'count'}))


## Check if covidonly & complete have same images
cfiles = os.listdir(path)
for filename in metadata.filename:
	check = metadata[(metadata['filename']==filename) & (metadata['finding']=='COVID-19')]
	if not check.empty and filename not in cfiles:
		print(filename)
		metadata = metadata.drop(metadata[metadata['filename']==filename].index, axis=0)


## Delete rows for deleted files
# files = os.listdir(full_path)

# for filename in metadata['filename']:
# 	if filename not in files:
# 		metadata = metadata.drop(metadata[metadata['filename']==filename].index, axis=0)

## For extra files
# for f in os.listdir(path):
# 	if f not in metadata['filename']:
# 		metadata=metadata.append(pd.DataFrame({'filename':[f], 'finding': ['COVID-19']}))

print(metadata.groupby(['finding']).agg({'filename':'count'}))
metadata.to_csv('metadata_processed.csv')


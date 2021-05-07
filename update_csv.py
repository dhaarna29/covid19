import os
import pandas as pd 

path = './covidonly x-rays'
metadata = pd.read_csv('metadata_processed.csv')

print(metadata.groupby(['finding']).agg({'filename':'count'}))

for f in os.listdir(path):
	if f not in metadata['filename']:
		metadata=metadata.append(pd.DataFrame({'filename':[f], 'finding': ['COVID-19']}))

print(metadata.groupby(['finding']).agg({'filename':'count'}))
metadata.to_csv('metadata_new.csv')
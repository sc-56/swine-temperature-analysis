#%%

import pandas as pd
import os
import matplotlib.pyplot as plt
print("all imported.")

#%%
# set the file path
# read tmperature information
# file_path = '0-data/sum_coyote_sjz_21010626001_88001026.csv'
# df = pd.read_csv(file_path, header=None, usecols=[0, 1])

def calculate_base_info(df):

    # change first column to data
    df.loc[:, 0] = pd.to_datetime(df.loc[:,0])

    # select ones later than 03-15
    df_late = df.loc[df[0] > pd.to_datetime('2022-03-15 00:00:00')]

    # select 2nd column
    df_late = df_late.loc[:, 1]

    # calculate min, max
    max = df_late.max()
    min = df_late.min()

    # calculate median
    median = df_late.median()

    # calculate standard deviation
    std = df_late.std()

    # num of null
    num_null = int(df_late.isnull().sum())

    return max, min, median, std, num_null

directory_path = '/mnt/c/Users/zhanyich/OneDrive - Boehringer Ingelheim/Desktop/tmp/0-data'
directory = os.fsencode(directory_path)

files = os.listdir(directory)
results = []


for file in files:
    file = str(file)
    file = file[2: -1]

    file_path = '0-data/' + file
    df = pd.read_csv(file_path, header=None, usecols=[0, 1])

    result = calculate_base_info(df)
    results.append(result)

#%%

df_results = pd.DataFrame(results)
df_results.columns = ['max', 'min', 'median', 'deviation', 'number of null']



# display one hist
plt.hist(df_results['number of null'], bins=10, color='darkblue')
plt.grid(linestyle='-', linewidth=0.5)
plt.savefig('./null.jpg')






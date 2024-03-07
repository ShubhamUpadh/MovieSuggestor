import pandas as pd
import os
import sys
from datetime import datetime
'''
currentDate = datetime.now()
df = pd.read_csv('movies.csv')
df['release_date'] = pd.to_datetime(df['release_date'])
releasedMovies = df[df['release_date'] < currentDate]
releasedMovies.to_csv('releasedMovies.csv',index=False)

df1 = pd.read_csv('releasedMovies.csv')
uniqueLang = df1['original_language'].unique()
for lang in uniqueLang:
    print(lang,end= " | ")

df1 = pd.read_csv('releasedMovies.csv')
print(df1[df1['original_language'].str.lower() == 'hi']['title'].head())
print("Done")
#print(df['release_date'].head())


df1 = pd.read_csv("releasedMovies.csv")
df2 = df1[df1['original_language'].str.lower().isin(['en','hi'])]
print(df2['title'].head())

df2.to_csv("releasedMovieEnHi.csv",index=False)
'''
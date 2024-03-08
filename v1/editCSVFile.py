import pandas as pd
import os
import sys
from datetime import datetime, timedelta
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

df3 = pd.read_csv("releasedMovieEnHi.csv")
df3['release_date'] = pd.to_datetime(df3['release_date'])
cutoffDate = datetime.now() - timedelta(365.25*30)      # 30 represents that cutoff date is last 30 years

df4 = df3[df3['release_date']>=cutoffDate]
df4.to_csv("releasedMoviesEnHiLast30Years.csv",index=False)

df5 = pd.read_csv('releasedMoviesEnHiLast30Years.csv')
for column in df5.columns:
    print(column)
    print(df5[column].head())
    print("\n")

df1 = pd.read_csv("processedMovieNames.csv")
print(df1.shape[0])
df2 = pd.read_csv("Last30yearsSorted.csv")
mergedDf = pd.merge(df1, df2, left_on="title", right_on="movie_name",how="inner")
print(mergedDf.shape[0])
mergedDf.to_csv("movieWithDirectors.csv")

df1 = pd.read_csv("movieWithDirectors.csv")
for column in df1.columns:
    print(column,end =" | ")
selectedColumns = ['title',"genres", "original_language", "overview", "keywords","poster_path","processedTitle","director","star"]
selectedDf = df1[selectedColumns]

print(selectedDf.head(),selectedDf.shape[0])
selectedDf.to_csv("cleanedMovieWithDirectors.csv",index=False)

selectedDf = selectedDf.drop_duplicates(['title'])
selectedDf.to_csv('noduplicates.csv',index = False)
print(selectedDf.head(),selectedDf.shape[0])
print(selectedDf)
'''
df1 = pd.read_csv('noDuplicates.csv')
print(df1['original_language'].unique())
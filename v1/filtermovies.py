'''
import pandas as pd
from datetime import datetime, timedelta
import os

listOfFiles = os.listdir(r"archive2/")
listOfFiles = [ x for x in listOfFiles if x[-3:] == "csv"]
print(listOfFiles)

currentDate = datetime.now()
df = pd.DataFrame()
for file in listOfFiles:
    tempdf = pd.read_csv(r'archive2/'+file)
    tempdf['year'] = pd.to_datetime(tempdf['year'],  errors='coerce')
    releasedMovies = tempdf[tempdf['year'] < currentDate]
    df = pd.concat([df,releasedMovies])

df.to_csv("Last30years.csv",index=False)
print(df.head())
'''
import pandas as pd
df = pd.read_csv("Last30years.csv")
print(df.shape[0])
df = df.dropna(subset=['year'])
print(df.shape[0])
df = df.sort_values(by=['movie_name'],ascending=True)
df.to_csv("Last30yearsSorted.csv")

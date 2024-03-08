from fuzzywuzzy import process
import pandas as pd
from preprocessMovieNames import preprocess
'''

df['release_date'] = pd.to_datetime(df['release_date'])
latestReleaseDate = df['release_date'].max()
latestMovie = df[df['release_date'] == latestReleaseDate]
print(latestMovie, latestReleaseDate)

'''
df = pd.read_csv('processedMovieNames.csv')
userInput = input("Enter movie name : ")
processedInput = preprocess(userInput)
print(processedInput)

processedMovieTitles = df['processedTitle'].tolist()

closestMatch, score = process.extractOne(processedInput,processedMovieTitles)

print("Closest match:", df[df['processedTitle'] == closestMatch]['title'].iloc[0])
print("Matching score:", score)



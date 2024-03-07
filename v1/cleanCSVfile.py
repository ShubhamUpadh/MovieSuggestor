import pandas as pd
df = pd.read_csv("cleanedMovieTitles.csv")
notStringIndex = []
for index, row in df.iterrows():
    if not isinstance(row['title'], str):
        print(f"Title at index {index} is not a string:", row['title'],row['overview'])
        notStringIndex.append(index)
if len(notStringIndex) == 0:
    print("All the titles are strings")
df = df.drop(notStringIndex)
df.to_csv('cleanedMovieTitles.csv',index=False)
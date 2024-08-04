import pandas as pd

df = pd.read_csv('chords.csv')
chords_column = df['Chords']

allchords = set()
for song in chords_column:
    split = song.split()
    mset = set(split)
    # print(mset)
    allchords.update(mset)

print(allchords)


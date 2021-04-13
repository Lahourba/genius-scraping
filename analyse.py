import pandas as pd
import matplotlib.pyplot as plt

hen = 'Hennessy'
hen2 = 'Hennessey'
hen3 = 'Henny'

tracklist = pd.read_csv('lyrics_df.csv')

# add a column with the count per song 
tracklist['count'] = tracklist['lyrics'].apply(lambda x: x.count(hen) + x.count(hen2) + x.count(hen3))
# create new dataframe with only count > 0
tracklist_hen = tracklist[tracklist['count'] > 0]
# create table with ranking of rappers based on Hennessy count
hen_ranking = tracklist_hen.groupby('artist')['count'].sum().to_frame().sort_values('count', ascending=False)
# create a table with ranking of rappers based on total # of songs recorded 
song_ranking = tracklist.groupby('artist')['title'].count().to_frame().sort_values('title', ascending=False)

# create a table with artist name, nb Hennessy mentions, nb songs recorded, and ratio Hennessy / songs recorded 
final_ranking = hen_ranking.join(song_ranking, on='artist')
final_ranking.columns = ['count_hen', 'count_songs']
final_ranking['ratio_hen'] = final_ranking['count_hen'] / final_ranking['count_songs']
final_ranking = final_ranking.round(3)

# top 10 songs with most Hennessy mentions
ranking_songs = tracklist_hen[tracklist_hen['count'] > 1]
ranking_songs = ranking_songs[['artist', 'title', 'count']].sort_values('count', ascending=False).head(10)\
.reset_index()[['artist', 'title', 'count']]

# barplot - ranking Hennessy mentions 
final_ranking['count_hen'].head(10).plot.\
bar(rot=70, title="Hennessy ranking", figsize=(7,7), color=['#0066CC'])

# barplot - ranking Hennessy mentions RATIO
final_ranking['ratio_hen'].to_frame().head(10).sort_values('ratio_hen', ascending=False).plot.\
bar(rot=70, title="Hennessy ratio ranking", figsize=(7,7), color=['#0066CC'])


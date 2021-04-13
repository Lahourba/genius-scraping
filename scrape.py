import pandas as pd
import time
import lyricsgenius
import requests
from bs4 import BeautifulSoup
from requests.exceptions import Timeout

GENIUS_API_TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


# SCRAPING THE REDDIT PAGE TO GET THE LIST OF 50 RAPPERS

# using a user agent (Chrome)
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

# url of the post 
url = 'https://www.reddit.com/r/hiphop101/comments/ezvc0r/top_50_rappers_of_all_time/'

# pulling out HTML of the page  
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# putting the 50 rappers in a list, and replacing Biggie with The Notorious B.I.G. and André 3000 with OutKast
list_50_rappers = [rapper.p.getText() for rapper in soup.find_all('li')]
list_50_rappers = [rapper.replace("Biggie", "The Notorious B.I.G.") for rapper in list_50_rappers]
list_50_rappers = [rapper.replace("Andre 3000", "OutKast") for rapper in list_50_rappers]

# adding Drake and Kanye to the list
list_50_rappers.extend(['Kanye West', 'Drake'])

# CONNECTION TO GENIUS API, AND DOWLOADING LYRICS FOR ALL ARTISTS

# Keep only the songs, and exclude Remix, Live, etc.
genius = lyricsgenius.Genius(GENIUS_API_TOKEN, remove_section_headers=True,
                 skip_non_songs=True, excluded_terms=["Remix", "Live", "Edit", "Mix", "Club"])

#Starting the song search for the artists in question and seconds count
query_number = 0
time1 = time.time()
#Setting empty lists
artists = []
titles = []
lyrics = []
for artist in list_50_rappers:
    query_number += 1
    print('\nQuery number:', query_number)
    # initiating a while loop in order to "force" the download of the songs (avoid TimeOut errors)
    while True:
        try:
            #Search for max_songs = 1000 and sort them by popularity
            artist = genius.search_artist(artist, max_songs = 1000, sort='popularity')
            songs = artist.songs
            song_number = 0
            #Append all information for each song in the previously created lists
            for song in songs:
                if song is not None:
                    song_number += 1
                    print('\nSong number:', song_number)
                    artists.append(song.artist)
                    titles.append(song.title)
                    lyrics.append(song.lyrics)
            time2 = time.time()
            print('\nQuery', query_number, 'finished in', round(time2-time1,2), 'seconds.')
            break
        except:
            pass

# store all the lyrics in a dataframe 
tracklist = pd.DataFrame({'artist':artists, 'title':titles,'lyrics':lyrics})

# export CSV 
tracklist.to_csv('lyrics_df.csv')

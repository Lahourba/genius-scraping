# genius-scraping

Genius-scraping aims to count the number of times US rappers mention the brand Hennessy - quite popular among their community - in their songs. 

Genius-scraping is split in 2 files:
1) srape.py: script allowing you to scrape song lyrics from 52 US rap artists thanks to the Genius API, store them in a dataframe and export in CSV  
This requires you to go to the Genius API management page in order to get a token. Everything you need to know is explained right here:
https://docs.genius.com/#/getting-started-h1

2) analyse.py: script allowing you to count the number of times the words 'Hennessy', 'Hennessey' and 'Henny' appear in each of the lyrics, and to establish a ranking. 


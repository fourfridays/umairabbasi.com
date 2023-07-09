The code pulls movies and tv shows calling TMDB API's rated movies and rated tv calls.

The code only checks for a single MovieIndexPage or a single TvIndexPage. If you have created multiple movie or tv index pages it will work based off the most recent page that was created.

Poster size can be set by changing the value of the variable `poster_size`. The size
must be one of the following sizes:
- "92",
- "154",
- "185",
- "342",
- "500",
- "780",
- "original"
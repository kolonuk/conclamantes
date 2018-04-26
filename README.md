# conclamantes

The aim of this project is to create a fully functional alternative to Sonarr/Radarr.  The difference will be that:
 - it is not dependant on .Net (mono)
 - has a separate front- and back- ends
 - has the features that are missing from sonnar/radarr like custom series/genre filesizes, media expiry dates, specific exclusions/includsions per search, post-search filtering from Jackett, and more.

THIS IS CURRENTLY IN PRE-PRE-ALPHA!!  This is my first big project to try to learn Python properly, work on RESTapi interfaces, program plugins and figure out how a real build system works.  Oh and play with Docker!

* Features
The core will be fixed, but all features will be plugins:
  - each media type will be a plugin (series, movies, ebooks, comics, audio, and even some remote media tools such as get_iplayer and youtubedl)
  - each search method/db will be a plugin (nzb, torrent, bbc iplayer, etc.)
    - (this will include in the automated download section the ability to
  - each transfer client will be a plugin (nzb, transmission, azureus, rtorrent, ctorrent, utorrent, etc.)
  - each media db will be a plugin (imdb, tvdb, omdb, etc.)
  - each media client will be a plugin (xbmc, emby, plex, etc.)
  - plugins for external actions (RESTful apis, command line scripts, etc) for various internal actions

(I can see this using Jackett for searching for the time being, as they have and are doing a fantastic job keeping track of torrent trackers!)

* Open API
The idea will be that there will be a simple API interface to do searches, trigger downloads from remote systems, etc.  This way, you can write your own frontend!

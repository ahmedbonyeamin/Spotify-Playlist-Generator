# Spotify-Playlist-Generator

## Installing 'requests' library

**Install requests library from the command line:**

**python3.7 -m pip install requests** 

Replace 'python3.7' with whatever python version you have.

NOTE - PIP

## Spotify API

[https://developer.spotify.com/console/get-recommendations/](https://developer.spotify.com/console/get-recommendations/) 

Scroll to the bottom and click '**Get Token Button**' and click '**playlist-modify-private**' as the scope you need. You will also need to sign in to Spotify. 

## APIs

APIs (Application Programming Interface) list a bunch of operations that a programmer can use

What we are doing: 

1. an HTTP GET request to the /recommendations endpoint, to get the tracks;

2. an HTTP POST request to the /playlists endpoint to create a new playlist;

3. an HTTP POST request to the /playlist endpoint to add the songs.

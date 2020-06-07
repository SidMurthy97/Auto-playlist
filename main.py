from __future__ import print_function
import sys
import spotipy
import spotipy.util as util
import json
from datetime import date, datetime
from time import sleep


#schedule using cron on raspberry pi. 0 8 1 * *

scope = 'user-top-read playlist-modify-private playlist-modify-public' #scope must be given as a single string

# if len(sys.argv) > 1:
#     username = sys.argv[1]
# else:
#     print("Usage: %s username" % (sys.argv[0],))
#     sys.exit()


username = input("enter your user id: ")

token = util.prompt_for_user_token(username,scope,client_id='',client_secret='',redirect_uri='') # put your own credentials here, or use the main.exe under the dist folder
sp = spotipy.Spotify(auth=token)

now = datetime.now()
playlist_name = now.strftime("%m/%y")

if token: #If authorised

    sp.user_playlist_create(username,playlist_name) #creates playlist with given name

    playlist = sp.user_playlists(username,limit = 1)
    playlist_id = playlist['items'][0]['id'] #gets id of the newly created playlist

    results = sp.current_user_top_tracks(limit=15,offset = 0,time_range='short_term') #gets top 15 tracks
    track_list = []

    for item in results['items']:

        track_list.append(item['id']) # all track ids are added to a list

    sp.user_playlist_add_tracks(username,playlist_id,track_list) #adds songs to created playlist

    sleep(1)



else:
    print("Can't get token for", username)

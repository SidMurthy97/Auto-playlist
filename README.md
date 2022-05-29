# Auto-playlist

## The Project

This project was made to automate my love for making a new spotify playlist every single month. Previously, I used to make a new playlist every month and add all the songs that I enjoyed in that month to the playlist. When the next month came along, I would port some songs over from the current month's playlist and continue adding new songs to the next month's playlist. Rise and repeat.

I soon realised that using the Spotify API, I could query Spotify's data on me and get a list of my most listened to songs in the last month! Based off of this, I could then create a new month-titled playlist on the first of every month at 8am automatically - thus reducing the manual porting of songs every month to a newly created playlist. 

I hosted this script on an EC2 instance in AWS and used the Linux scheduler, Cron, to schedule the script to run every month. This program has been running for more than 2 years now, and gives me a great record of all the songs I have ever enjoyed. Want to listen to music that sounds like August 2019? It's already there! 

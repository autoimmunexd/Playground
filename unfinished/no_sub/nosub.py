import feedparser

def load():
    try:
        with open('subscriptions.txt', 'r') as file:
            subscriptions = file.readlines()
            return subscriptions
    except FileNotFoundError:
        print('subscriptions.txt not found, creating subscriptions.txt')
        with open('subscriptions.txt', 'w') as file:
            file.write("")
        with open('subscriptions.txt', 'r') as file:
            subscriptions = file.readlines()
            return subscriptions

#returns a list of all of the latest videos for every subscribed channel
#looping and returning doesn't work for each loop, pass all information to variable once loop is done return that array variable
def get_feed(subscriptions):
    all_entry_info = []
    for subscription in subscriptions:
        channel = feedparser.parse(subscription)
        first_entry = channel.entries[0]
        title = channel.feed.get("title", "")
        entry_info = {
            "Channel Name": title,
            "Title": first_entry.get('title', ''),
            "Link": first_entry.get('link', ''),
            "Thumbnail": first_entry.get('media_thumbnail', [{}])[0].get('url', ''),
            "Published Date": first_entry.get('published', '')
        }
        all_entry_info.append(entry_info)
    return all_entry_info
    # TO DO, only parse the feed once every 2 hours
    # make another variable and display the data from that to speed up loading
    #add timestamp to all_entry_info, if it's older than 2 hours update it

def get_subscriptions(subscriptions):
    channel_names = []
    for subscription in subscriptions:
        channel = feedparser.parse(subscription)
        channel_name = channel.feed.get("title", "")
        channel_names.append(channel_name)
    return channel_names

def add_subscription(new_sub, subscriptions):
    pass
    #take the new sub channel url
    #get the RSS feed url
    #append the rss feed url to the subscriptions array in memory
    #save to the subscriptions.txt
    #print updated subscriptions
    #flash subscription added on page!

def play_video():
    # Create a new VLC instance
    instance = vlc.Instance()
    # Create a new MediaPlayer
    player = instance.media_player_new()
    # Replace 'VIDEO_URL' with the URL of the YouTube video
    media = instance.media_new('VIDEO_URL')
    # Set the media to the player
    player.set_media(media)
    # Start playing the media
    player.play()
    # Render a template or return a response indicating that the video is playing
    return 'Playing YouTube video...'
    
    #FLASK VIDEO STREAMING
    #CREATE VLC INSTANCE, STREAM TO FLASK VIDEO STREAMING SERVER




#FUTURE FEATURES

#def unwatched():
    #list all unwatched videos

#def download():
    #

#use local files and only pull rss feeds on time intervals
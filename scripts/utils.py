import requests
import feedparser
import re

class Youtube:
    def __init__(self, channelId):
        self.link = "https://www.youtube.com/feeds/videos.xml?"
        self.channel = "channel_id=" + channelId
        self.url = self.link + self.channel
    def call(self):
        r = requests.get(self.url)
        rcode = True if r.status_code == 200 else False
        if(rcode):
            feed = feedparser.parse(r.text)
        return rcode, feed
    def pullTitle(feed, i):
        for entry in feed.entries:
            i = i+1
            print("Entry Title: ", entry.title)
            print("Entry Link:", entry.link)
            print("Entry Published Date:", entry.published)
            if i >= 1:
                return

class Twitter:
    def __init__(self):
        self.link = "https://api.twitter.com/2/tweets"
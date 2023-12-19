from scripts.utils import Youtube as yt

channelId = "UCAVojJ1k03GZzjSbdXXunkw"

YT = yt(channelId)
rcode, feed = yt.call(YT)
yt.pullTitle(feed, 1)
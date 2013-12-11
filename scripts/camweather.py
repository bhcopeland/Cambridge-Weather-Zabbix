import feedparser
import re

d = feedparser.parse('http://www.cl.cam.ac.uk/research/dtg/weather/rss.xml');

wlist = d['entries'][0]['description'];

print re.sub('<[^<]+?>', ' ', wlist)


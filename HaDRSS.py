#! /usr/bin/python
import feedparser

url = "http://feeds.feedburner.com/hackaday/LgoM?format=rss"
feed = feedparser.parse( url )
for item in feed["items"]:
	title = item["title"]
	if (len(title) > 40):
		#print title[0:40] + "\n\t" + title[41:]
		words = title.split()
		line = '-'
		secondline = ''
		while(((len(line)+len(words[0])) <=40) and (len(words) > 0)):
			line += words[0] + " "
			words.pop(0)
		while (len(words) > 0):
			secondline += words[0] + " "
			words.pop(0)
		if(secondline == ""):
			print line
		else:
			#print line + "\t\n" + secondline
			print line[0:-1] + "..."
		
	else:
		print "-" + title
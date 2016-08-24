import sys
import time
import telepot
from pprint import pprint
from urllib2 import urlopen

#generate list of memecodes
helpText = ""
for i in xrange(int(raw_input())):
	helpText += raw_input() + "\n"

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if 'entities' in msg:
    	if msg['text'] == "/start":
    		bot.sendMessage(chat_id, "Greetings! Use this bot to generate memes quickly. Write your meme as follows:\n<code>/<top text>/<bottom text>\nType /help for meme codes")
    	elif msg['text'] == "/help":
    		bot.sendMessage(chat_id, helpText)
    
    elif content_type == 'text':
        #split message text into memecode, upper text and lower text
    	memeCode, upText, downText = msg['text'].split('/')

        #form url to generate meme using memegen
    	link = "http://memegen.link/" + memeCode + "/" +  upText + "/" + downText + ".jpg"
    	link = link.replace(' ', '-')
    	link = link.lower()

        a = urlopen(link)

        #return meme to user
        bot.sendPhoto(chat_id, ("out.jpg", a))

bot = telepot.Bot("255762769:AAFCAGSw-w--nEwNgftP1DcycchWXHJksao")
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
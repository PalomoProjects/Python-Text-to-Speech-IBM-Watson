#!/usr/bin/env python

import oauth2 as oauth

import json

import time

import unicodedata

from tts_watson.TtsWatson import TtsWatson

textoTw = ""
usernameTw = ""

CONSUMER_KEY = "#YourConsumerKeyFromTwitter" 
CONSUMER_SECRET = "#YourConsumerSecretFromTwitter" 
ACCESS_KEY = "#YourAccesKeyFromTwitter" 
ACCESS_SECRET = "#YourAccesSecretFromTwitter" 

AUX1 = ""
AUX2 = ""

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer,access_token)

timeline_endpoint = "https://api.twitter.com/1.1/search/tweets.json?q=%23SaturdayIBMProgramming"

ttsWatson = TtsWatson('userfromwatson', 'passwordfromwatson', 
'en-US_AllisonVoice') 

def remove_accents(input_str):
    nkfd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nkfd_form.encode('ASCII', 'ignore')
    return only_ascii

while 1:

    try:
        response, data = client.request(timeline_endpoint)
        data = json.loads(data)
        usernameTw = remove_accents(data['statuses'][0]['user']['screen_name'])
        textoTw = remove_accents(data['statuses'][0]['text'])
        if AUX1!=textoTw or AUX2!=usernameTw:
            print "Read Twitter"
            AUX1=textoTw
            AUX2=usernameTw
            ttsWatson.play(textoTw + " " + usernameTw)
        else:
            time.sleep(6)
    except:
        data = ""
        print "Nothing to show"
        time.sleep(6)
        continue
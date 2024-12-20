# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:02:54 2024

@author: user
"""

from chat_downloader import ChatDownloader
import pytchat
from gtts import gTTS
from mutagen.mp3 import MP3
import os
import threading
import time

def read_TTS(text_str:str):
    
    TTS = gTTS(text = text_str, lang = "en",slow = False)
    
    TTS.save("t.mp3")
    
    os.system("start t.mp3")
    
    audio = MP3("t.mp3")
    
    duration = audio.info.length
    
    return(duration)


def Wait_list(Chat:str,
              User:str,
              Message:str,
              list_chat:list):
        
    if len(Message) < 160:
        list_chat.append(f"{Chat} {User} said: {Message}")
    else:
        list_chat.append(f"{Chat} {User} wrote a message that was longer than 160 characters")


def Twitch_Chat(URL_Twitch:str,
                list_chat:list):
    
    print("Conecting to Twitch...")
    
    chat = ChatDownloader().get_chat(URL_Twitch)
    
    print("Connected to Twitch!")
    
    for message in chat:
        
        name = message.get("author",{}).get("name","")
        
        message_text = message.get("message","")
        
        Wait_list(
            "Twitch",
            name,
            message_text,
            list_chat
            )
        
def Main(URL_Youtube:str,
         URL_Twitch:str,
         delay:int):
    
    list_chat = []
    
    threading.Thread(target = lambda: Twitch_Chat(URL_Twitch,list_chat),
                     daemon = True).start()
    
    youtube_code = URL_Youtube[URL_Youtube.find("=") + 1 : ]
    
    print("Conecting to Youtube...")
    
    chat_y = pytchat.create(video_id = youtube_code)
    
    print("Connected to Youtube!")
    
    while chat_y.is_alive():
        
        try:
                
            for c in chat_y.get().sync_items():
                
                Wait_list("Youtube",
                          c.author.name,
                          c.message,
                          list_chat)
        
        except AttributeError:
            
            chat_y = pytchat.create(video_id = youtube_code)
        
        if len(list_chat) > 0:
            
            read_this = list_chat[0]
            
            list_chat.pop(0)
            
            read_time = read_TTS(read_this)
            
            print("__________________________________________________________________________")
            print(read_this)
            
            time.sleep(read_time)
            
            time.sleep(delay)
        
            

if __name__ ==  "__main__":
    
    URL_Youtube = "https://www.youtube.com/watch?v=akNQoGRV4w4"
    URL_Twitch = "https://www.twitch.tv/softval"
    
    delay = 3
    
    Main(URL_Youtube,
         URL_Twitch,
         delay)
    
    
























        
        
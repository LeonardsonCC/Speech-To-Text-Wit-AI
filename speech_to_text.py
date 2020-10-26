#!/bin/python3.8

import threading
import requests
import json
import io
import os
import configparser
from datetime import datetime
from Recorder import record_audio, read_audio

# Getting config parameters
config = configparser.ConfigParser()
config.read("config.ini")
API_ENDPOINT = config['WIT_AI']['API_ENDPOINT']
wit_access_token = config['WIT_AI']['ACCESS_TOKEN']

def start_record_audio():
    # record audio of specified length in specified audio file
    temp_file = io.BytesIO()
    audio_bytes = record_audio(temp_file)
    
    # reading audio
    audio = read_audio(audio_bytes)

    thread_text_from_audio = threading.Thread(target=get_text_from_audio, args={audio: audio})
    thread_text_from_audio.start()


def get_text_from_audio(audio):
    # defining headers for HTTP request
    headers = {'authorization': 'Bearer ' + wit_access_token,
               'Content-Type': 'audio/wav'}

    # making an HTTP post request
    resp = requests.post(API_ENDPOINT, headers = headers,
                         data = audio)
    
    # converting response content to JSON format
    data = json.loads(resp.content)
    
    # get text from data
    if 'text' not in data:
        print(data)
    text = data['text']
    
    # return the text
    write_text_to_file(text)


def write_text_to_file(text):
    date_now = datetime.now()
    filename = "{}{}{}.txt".format(date_now.year, date_now.month, date_now.day)

    TEXT_FOLDER = config['TEXT']['FOLDER']

    if os.path.exists(TEXT_FOLDER) is not True:
        os.mkdir(TEXT_FOLDER)
    filename = os.path.join(TEXT_FOLDER, filename)

    with open(filename, 'a') as text_file:
        text_file.write(text + " ")
    print("Finished write in {}".format(filename))

if __name__ == "__main__":
    while True:
        audio = start_record_audio()

import json
import requests
import smtplib

TOKEN = "975334004:AAEVotz_4_bsfHY_lGc1AzMDwhySgqBCFDw"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js

def get_last_chat_id(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return chat_id

def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

text = "Good evening! Don't forget to push today's status update.\nUse the following format: \n\n\tSUBJECT: Status Update [DD-MM-YYYY]\n\tWork Done: *****\n\tPlanned: *****\n\tBlockers: *****\n\nRemember to send detailed updates about your progress today. Thank you!"
chat = get_last_chat_id(get_updates())
send_message(text, chat)

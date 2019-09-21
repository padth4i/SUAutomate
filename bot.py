import json
import requests
import smtplib

TOKEN = "975334004:AAEVotz_4_bsfHY_lGc1AzMDwhySgqBCFDw"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
sender_id = "senders_email_id"
sender_password = "senders_password"
thread_id = "recievers_email_id"
s.login(sender_id, sender_password)

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


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)
    message = text
    s.sendmail(sender_id, thread_id, message)


text, chat = get_last_chat_id_and_text(get_updates())
send_message(text, chat)

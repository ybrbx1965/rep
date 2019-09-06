import requests
from time import sleep

url = 'https://api.telegram.org/bot974040312:AAH9DLDjhc_hgvXj79ynLl4sd0kmmyDfp4o/'
repeat = False
my_mess = ''

def get_updates_json(request):
    params = {'timeout': 100, 'offset': None}
    response = requests.get(request + 'getUpdates', data=params)
    return response.json()

def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

def check_if_command(update):
    global repeat
    global my_mess
    hi = False
    my_mess = ''
    chat_text = update['message']['text']
    chat_name = update['message']['chat']['username']

    if repeat:
        my_mess = chat_text
        if chat_text == 'Бот не повторяй':
            repeat = False


    if not repeat:
        if chat_text == 'Бот скажи привет':
            hi = True
        elif chat_text == 'Бот повторяй':
            repeat = True
        else:
            my_mess = 'No comm'
        if hi == True:
            my_mess = 'Привет' + ' ' + chat_name
            hi = False




    print(chat_name,':',chat_text)
    print('Bot:', my_mess)
    logged = False

def main():
    global my_mess
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
           check_if_command(last_update(get_updates_json(url)))
           send_mess(get_chat_id(last_update(get_updates_json(url))), my_mess)
           my_mess = ''
           #send_mess(get_chat_id(last_update(get_updates_json(url))), 'ЗДАРОВА')
           update_id += 1
        sleep(1)

if __name__ == '__main__':
    main()
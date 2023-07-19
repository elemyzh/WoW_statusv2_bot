import requests
import telebot

#este codigo es para linux
# en la version 6 puse un try: para cuando el server este caido o con problema no de error y mande una except: con server off

API_TOKEN = '6342601545:AAEBTt-f9JlgLOLOee_xVADM8W-vsV2H9KQ'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['mop'])
def handle_mop_command(message):
    try:
        response = requests.get('https://api.rogwow.com/realm/mop/status/v3/')
        data = response.json()
        realm_status = data['realm_status']
        if realm_status == 'Offline':
            bot.send_message(message.chat.id, 'Server mop: Offline')
        else:
            realm_characters = data['realm_characters']
            alliance = realm_characters['alliance']
            horde = realm_characters['horde']
            realm_diff = data['realm_diff']
            bot.send_message(message.chat.id, '\nServidor MoP: {}\nPj Alianza🦁: {}\nPj Horda🚩: {}\nLatencia Mundo⌛: {}'.format(realm_status, alliance, horde, realm_diff))
    except:
        bot.send_message(message.chat.id, 'Server mop: Offline')


@bot.message_handler(commands=['lk'])
def handle_mop_command(message):
    try:
        response = requests.get('https://api.rogwow.com/realm/lk/status/v3/')
        data = response.json()
        realm_status = data['realm_status']
        if realm_status == 'Offline':
            bot.send_message(message.chat.id, 'Server LK: Offline')
        else:
            realm_characters = data['realm_characters']
            alliance = realm_characters['alliance']
            horde = realm_characters['horde']
            realm_diff = data['realm_diff']
            bot.send_message(message.chat.id, '\nServidor LK: {}\nPj Alianza🦁: {}\nPj Horda🚩: {}\nLatencia Mundo⌛: {}'.format(realm_status, alliance, horde, realm_diff))
    except:
        bot.send_message(message.chat.id, 'Server LK: Offline')




if __name__ == '__main__':
    bot.polling(timeout=60)
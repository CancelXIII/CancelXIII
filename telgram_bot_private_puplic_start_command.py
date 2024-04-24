start_private_msg = ' welcome to private chat'
start_supergroup_msg = ' welcome to our public chat'

help_msg = 'how help you?'

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    if message.chat.type == 'supergroup':
        start_command = '/start'+'@nameOFBot'
        help_command = '/help'+'@nameOFBot'
        if message.text == start_command:
            bot.reply_to(message, f' welcome to our {message.chat.title} chat')
        elif message.text == help_command:
            bot.reply_to(message, help_msg)
    elif message.chat.type == 'private':
        start_command = '/start'
        help_command = '/help'
        if message.text == start_command:
            bot.reply_to(message, ' welcome to private chat')
        elif message.text == help_command:
            bot.reply_to(message, help_msg)

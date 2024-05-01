

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    start_private_msg = ' welcome to private chat'
    help_private_msg = 'how help you?'
    start_supergroup_msg = f' welcome to our {message.chat.title} chat'
    help_supergroup_msg = 'how help you?'
    if message.chat.type == 'supergroup':
        start_command = '/start'+'@MrMemosBot'
        help_command = '/help'+'@MrMemosBot'
        if message.text == start_command:
            bot.reply_to(message, start_supergroup_msg)
        elif message.text == help_command:
            bot.reply_to(message, help_supergroup_msg)
        #set option to /mention_admin to send (help message) to online admins
    elif message.chat.type == 'private':
        start_command = '/start'
        help_command = '/help'
        if message.text == start_command:
            bot.reply_to(message, start_private_msg)
        elif message.text == help_command:
            bot.reply_to(message, help_private_msg)

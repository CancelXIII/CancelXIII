#source_channel_id = -1.....
destination_channel_id = -1.....
@bot.message_handler(content_types=['text'])
def forward_message(message):
    #if message.chat.id == source_channel_id:
    if message.chat.id != destination_channel_id:
        if message.from_user.is_bot is False:
            def note_order(send_box_message=None):
                noted = False
                send_box_message = send_box_message.strip().replace("  ", " ")
                middle = " note "
                start = "note "
                if len(send_box_message) >= len(middle) or len(send_box_message) >= len(start):
                    if middle in send_box_message:
                        text_note = send_box_message.index(middle) + len(middle)
                        final_text_note = send_box_message[text_note:].strip()
                        noted = True
                    elif start in send_box_message:
                        text_note = send_box_message.index(start) + len(start)
                        final_text_note = send_box_message[text_note:].strip()
                        noted = True
                    else:
                        #"-note order start = none"
                        pass
                else:
                    #"-note order len = None-"
                    pass
                if noted == True:
                    archive_message_form = 'ctitle::'+message.chat.title+'\n'+'cUName::'+message.chat.username+'\n'+'cId::'+str(message.chat.id)+'\n'+'fName::'+message.from_user.first_name+'\n'+'uName::'+message.from_user.username+'\n'+'uId::'+str(message.from_user.id)+'\n'+'uMessage::'+final_text_note 
                    bot.send_message(destination_channel_id, archive_message_form)
                    note_report_to_user = f"{final_text_note} is saved"
                    bot.reply_to(message, note_report_to_user)
            send_box_message= note_order(message.text)

#1
def sbm_rule():
    middle = " note "
    start = "note "
    return middle, start
def note_order(send_box_message=None):
    send_box_message = send_box_message.strip().replace("  ", " ")
    middle, start = sbm_rule()
    if len(send_box_message) >= len(middle) or len(send_box_message) >= len(start):
        if middle in send_box_message:
            text_note = send_box_message.index(middle) + len(middle)
            final_text_note = send_box_message[text_note:].strip()
            return final_text_note
        elif start in send_box_message:
            text_note = send_box_message.index(start) + len(start)
            final_text_note = send_box_message[text_note:].strip()
            return final_text_note
        else:
            #"-note order start = none"
            pass
    else:
        #"-note order len = None-"
        pass

#2        
print("------ 1")
send_box_message= note_order("note read book at 8:00 am")
print(f"{send_box_message} is saved")
print("------ 2")
send_box_message= note_order("i want note read book at 8:00 am ")
print(f"{send_box_message} is saved")

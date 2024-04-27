#words.txt
'''
hello,hola,merhaba,你好,שלום
good morning,Buenos días,Günaydın,早上好,בוקר טוב 
thanks,gracias,teşekkürler,谢谢,תודה
'''
open_words = open('words.txt','r', encoding='utf-8')
read_ = open_words.readlines()

default = 0  #en

select = "ch"
content = "good morning"
if select == "en":
    word = 0
elif select == "span":
    word = 1
elif select == "tr":
    word = 2
elif select == "ch":
    word = 3
elif select == "he":
    word = 4

for value in read_:
    value = value.split(",")
    for found_similar in value:
        if found_similar == content:
            print(value[word])
###
d = {
    1 : ['hello','hola','merhaba','你好','שלום'],
    2 : ['good morning','Buenos días','Günaydın','早上好','בוקר טוב'],
    3 : ['thanks','gracias','teşekkürler','谢谢','תודה']
     }
default = 0  #en

select = "tr"
content = "שלום"

if select == "en":
    word = 0
elif select == "span":
    word = 1
elif select == "tr":
    word = 2
elif select == "ch":
    word = 3
elif select == "he":
    word = 4
for key,value in d.items():
    for found_similar in value:
        if found_similar == content:
            print(value[word])
###
#words.txt
'''
hello,hola,merhaba,你好,שלום
good morning,Buenos días,Günaydın,早上好,בוקר טוב 
thanks,gracias,teşekkürler,谢谢,תודה
'''
open_words = open('words.txt','r', encoding='utf-8')
read_ = open_words.readlines()

default = 0  #en

select = "ch"
content = "good morning"
if select == "en":
    word = 0
elif select == "span":
    word = 1
elif select == "tr":
    word = 2
elif select == "ch":
    word = 3
elif select == "he":
    word = 4

for value in read_:
    value = value.split(",")
    for found_similar in value:
        if found_similar == content:
            print(value[word])
###
from eng_lang import *

def trans(lang_selected):
    if lang_selected == "en":
        import eng_lang
    elif lang_selected == "span":
        import span_lang

lang_selected = 'span'
trans(lang_selected)

print(f'{hello} sir')
print(f'{father}')

lang_selected = 'span'
if lang_selected == "span":
    from span_lang import *

print(f'{hello} sir')
print(f'{father}')
###
part1 = "na"
part2 = "me"
value = "UAE"
'''
name = "UAE"
'''

exec(f"{part1+part2} = '{value}'")

print(name)

###
d = {
    1 : ['hello','hola','merhaba','你好','שלום'],
    2 : ['good morning','Buenos días','Günaydın','早上好','בוקר טוב'],
    3 : ['thanks','gracias','teşekkürler','谢谢','תודה']
     }
default = 0  #en

select = "tr"
content = "שלום"

if select == "en":
    word = 0
elif select == "span":
    word = 1
elif select == "tr":
    word = 2
elif select == "ch":
    word = 3
elif select == "he":
    word = 4
for key,value in d.items():
    for found_similar in value:
        if found_similar == content:
            print(value[word])
###
#words.txt
'''
hello,hola,merhaba,你好,שלום
good morning,Buenos días,Günaydın,早上好,בוקר טוב 
thanks,gracias,teşekkürler,谢谢,תודה
'''
open_words = open('words.txt','r', encoding='utf-8')
read_ = open_words.readlines()

default = 0  #en

select = "ch"
content = "good morning"
if select == "en":
    word = 0
elif select == "span":
    word = 1
elif select == "tr":
    word = 2
elif select == "ch":
    word = 3
elif select == "he":
    word = 4

for value in read_:
    value = value.split(",")
    for found_similar in value:
        if found_similar == content:
            print(value[word])
###
from eng_lang import *

def trans(lang_selected):
    if lang_selected == "en":
        import eng_lang
    elif lang_selected == "span":
        import span_lang

lang_selected = 'span'
trans(lang_selected)

print(f'{hello} sir')
print(f'{father}')

lang_selected = 'span'
if lang_selected == "span":
    from span_lang import *

print(f'{hello} sir')
print(f'{father}')
###
part1 = "na"
part2 = "me"
value = "UAE"
'''
name = "UAE"
'''

exec(f"{part1+part2} = '{value}'")

print(name)

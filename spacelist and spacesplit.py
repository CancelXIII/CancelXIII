
def spacesplit(string_:str = None):
    list_ = []
    new_string = ''
    for i in string_:
        new_string += ''.join(i)
        if i == ' ' :
            list_.append(new_string)
            list_.append(' ')
            new_string = ''
    return list_

def spacelist(list_:list = None):
    list_new = []

    for i in list_:
        list_new.append(i)
        list_new.append(' ')
    return list_new
x = ['gff','dfgdf','dfgd']
z = spacelist(x)
print(z)

def cspacealpha(str_= None, specific_str = None,specific_type:bool= None):
    if specific_type is None:
        specific_type = True
    elif specific_type != True and specific_type != False:
        specific_type = True
    if specific_type == False and specific_str is None:
        specific_type = True
    str_ip = str_.strip() 
    x2 = ''
    for key,value_1 in enumerate(str_ip):
        x2 = x2.replace('  ', ' ')
        if not value_1.isalpha():
            if value_1 == ' ':
                x2+= ''.join(' ')
               
            elif value_1 != ' ':
                if key != 0  and key+1 < len(str_ip)-1 :
                    if str_ip[key-1].isalpha() and str_ip[key+1].isalpha():
                        if specific_type == False:
                            if specific_str is not None:
                                tru_ = False
                                for value_2 in specific_str:
                                    if value_1 == value_2:
                                        x2 += "".join(value_1)
                                        tru_ = True
                                        break
                                if tru_ == True:
                                    continue
                                elif tru_ == False:
                                    x2 += ''.join(' '+value_1+' ')
                        elif specific_type == True:
                            if specific_str is not None:
                                foundo_ = False
                                for value_3 in specific_str:
                                    if value_1 == value_3:
                                        x2 += ''.join(' '+value_1+' ')
                                        foundo_ = True
                                        break
                                    else:
                                        continue

                                if foundo_ == False:
                                    x2 += ''.join(value_1)
                            elif specific_str is None:
                                x2 += ''.join(' '+value_1+' ')
                    else:
                        x2 += ''.join(value_1)
                else:
                    x2 += ''.join(value_1)
        else:
            x2+= ' '.join(value_1)
        
    return x2
def rspacealpha(str_= None, specific_str = None,specific_type:bool= None):
    if specific_type is None:
        specific_type = True
    elif specific_type != True and specific_type != False:
        specific_type = True
    if specific_type == False and specific_str is None:
        specific_type = True
    str_ip = str_.strip() 
    x2 = ''
    for key,value_1 in enumerate(str_ip):
        x2 = x2.replace('  ', ' ')
        if not value_1.isalpha():
            if value_1 == ' ':
                x2+= ''.join(' ')
               
            elif value_1 != ' ':
                if key != 0  and str_ip[key-1].isalpha() :
                    if key == len(str_ip)-1 or not str_ip[key+1].isalpha():
                        if specific_type == False:
                            if specific_str is not None:
                                tru_ = False
                                for value_2 in specific_str:
                                    if value_1 == value_2:
                                        x2 += "".join(value_1)
                                        tru_ = True
                                        break
                                if tru_ == True:
                                    continue
                                elif tru_ == False:
                                    x2 += ''.join(' '+value_1)
                        elif specific_type == True:
                            if specific_str is not None:
                                foundo_ = False
                                for value_3 in specific_str:
                                    if value_1 == value_3:
                                        x2 += ''.join(' '+value_1)
                                        foundo_ = True
                                        break
                                    else:
                                        continue

                                if foundo_ == False:
                                    x2 += ''.join(value_1)
                            elif specific_str is None:
                                x2 += ''.join(' '+value_1)
                    else:
                        x2 += ''.join(value_1)
                else:
                    x2 += ''.join(value_1)
        else:
            x2+= ' '.join(value_1)
        
    return x2
def lspacealpha(str_= None, specific_str = None,specific_type:bool= None):
    if specific_type is None:
        specific_type = True
    elif specific_type != True and specific_type != False:
        specific_type = True
    if specific_type == False and specific_str is None:
        specific_type = True
    str_ip = str_.strip() 
    x2 = ''
    for key,value_1 in enumerate(str_ip):
        x2 = x2.replace('  ', ' ')
        if not value_1.isalpha():
            if value_1 == ' ':
                x2+= ''.join(' ')
               
            elif value_1 != ' ':
                if key+1 < len(str_ip)-1 and str_ip[key+1].isalpha():
                    if key == 0 or not str_ip[key-1].isalpha():
                        if specific_type == False:
                            if specific_str is not None:
                                tru_ = False
                                for value_2 in specific_str:
                                    if value_1 == value_2:
                                        x2 += "".join(value_1)
                                        tru_ = True
                                        break
                                if tru_ == True:
                                    continue
                                elif tru_ == False:
                                    x2 += ''.join(value_1+' ')
                        elif specific_type == True:
                            if specific_str is not None:
                                foundo_ = False
                                for value_3 in specific_str:
                                    if value_1 == value_3:
                                        x2 += ''.join(value_1+' ')
                                        foundo_ = True
                                        break
                                    else:
                                        continue

                                if foundo_ == False:
                                    x2 += ''.join(value_1)
                            elif specific_str is None:
                                x2 += ''.join(value_1+' ')
                    else:
                        x2 += ''.join(value_1)
                else:
                    x2 += ''.join(value_1)
           
        else:
            x2+= ' '.join(value_1)
        
    return x2
def spacealpha(str_= None, specific_str = None,specific_type:bool= None):
    if specific_type is None:
        specific_type = True
    elif specific_type != True and specific_type != False:
        specific_type = True
    if specific_type == False and specific_str is None:
        specific_type = True
    str_ip = str_.strip() 
    x2 = ''
    for key,value_1 in enumerate(str_ip):
        x2 = x2.replace('  ', ' ')
        if not value_1.isalpha():
            if value_1 == ' ':
                x2+= ''.join(' ')
            elif value_1 != ' ':
                if key != 0  and key+1 < len(str_ip)-1 :
                    if str_ip[key-1].isalpha() and str_ip[key+1].isalpha():
                        if specific_type == False:
                            if specific_str is not None:
                                tru_ = False
                                for value_2 in specific_str:
                                    if value_1 == value_2:
                                        x2 += "".join(value_1)
                                        tru_ = True
                                        break
                                if tru_ == True:
                                    continue
                                elif tru_ == False:
                                    x2 += ''.join(' '+value_1+' ')
                                    continue
                        elif specific_type == True:
                            if specific_str is not None:
                                foundo_ = False
                                for value_3 in specific_str:
                                    if value_1 == value_3:
                                        x2 += ''.join(' '+value_1+' ')
                                        foundo_ = True
                                        break
                                    else:
                                        continue
                                if foundo_ == True:
                                    continue
                                elif foundo_ == False:
                                    x2 += ''.join(value_1)
                                    continue
                            elif specific_str is None:
                                x2 += ''.join(' '+value_1+' ')
                                continue
                if key != 0 and str_ip[key-1].isalpha():
                    if specific_type == False:
                        if specific_str is not None:
                            tru_ = False
                            for value_2 in specific_str:
                                if value_1 == value_2:
                                    x2 += "".join(value_1)
                                    tru_ = True
                                    break
                            if tru_ == True:
                                continue
                            elif tru_ == False:
                                x2 += ''.join(' '+value_1)
                                continue
                    elif specific_type == True:
                        if specific_str is not None:
                            foundo_ = False
                            for value_3 in specific_str:
                                if value_1 == value_3:
                                    x2 += ''.join(' '+value_1)
                                    foundo_ = True
                                    break
                                else:
                                    continue
                            if foundo_ == True:
                                continue
                            elif foundo_ == False:
                                x2 += ''.join(value_1)
                                continue
                        elif specific_str is None:
                            x2 += ''.join(' '+value_1)
                            continue
                if key+1 < len(str_ip)-1 and str_ip[key+1].isalpha():
                    if specific_type == False:
                        if specific_str is not None:
                            tru_ = False
                            for value_2 in specific_str:
                                if value_1 == value_2:
                                    x2 += "".join(value_1)
                                    tru_ = True
                                    break
                            if tru_ == True:
                                continue
                            elif tru_ == False:
                                x2 += ''.join(value_1+' ')
                                continue
                    elif specific_type == True:
                        if specific_str is not None:
                            foundo_ = False
                            for value_3 in specific_str:
                                if value_1 == value_3:
                                    x2 += ''.join(value_1+' ')
                                    foundo_ = True
                                    break
                                else:
                                    continue
                            if foundo_ == True:
                                continue
                            elif foundo_ == False:
                                x2 += ''.join(value_1)
                                continue
                        elif specific_str is None:
                            x2 += ''.join(value_1+' ')
                            continue
                else:
                    x2 += ''.join(value_1)
        else:
            x2 += ''.join(value_1)
        
    return x2
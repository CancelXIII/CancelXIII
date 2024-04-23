
def replace_index(list_:list = None, index_ = None, text = None)->list:
    if list_ == None:
        return None
    lines = list_
    modified_lines = []
    for key,line in enumerate(lines):
        if key == index_:
            line = text
        modified_lines.append(line)
    return modified_lines
def remove_index(list_:list = None, index_ = None):
    if list_ == None:
        return None
    lines = list_
    modified_lines = []
    for key,line in enumerate(lines):
        if key == index_:
            continue
        modified_lines.append(line)
    return modified_lines
def isnumbername(number_name:str = None, number_value:bool = None, message:bool = None) -> bool:
    """Return the bool value
        this version support number names from 0 to 100
    Args:
        number_name (str)   : The name you want check if number name.
        number_value (bool) : Optional; to return name value.
        message(bool)         : Optional; message explain why return for.
    Returns:
        (None) if error or name not updateed yet in this version
        number_name (bool): True if number name, False if not.
    """
#     print('number_name:\n',number_name)
#     try:
    number_name = number_name.strip()
    number_name = spacealpha(number_name)
    print(number_name)
    number_name_split = number_name.split()
    number_names_dict_all = {
            "zero" : 0,
            "one"  : 1 ,
            "two"  :  2 ,
            "three"  : 3 ,
            "four"  :  4 ,
            "five"  : 5 ,
            "six"  :  6 ,
            "seven"  : 7 ,
            "eight"  :  8 ,
            "nine"  : 9 ,
            "ten"  :  10 ,
            "eleven"  : 11 ,
            "twelve"  :  12 ,
            "thirteen"  : 13 ,
            "fourteen"  :  14 ,
            "fifteen"  : 15 ,
            "sixteen"  :  16 ,
            "seventeen"  : 17 ,
            "eighteen"  :  18 ,
            "nineteen"  : 19 ,
            "twenty"  :  20 ,
            "twentyone"  : 21 ,
            "twentytwo"  :  22 ,
            "twentythree"  : 23 ,
            "twentyfour"  :  24 ,
            "twentyfive"  : 25 ,
            "twentysix"  :  26 ,
            "twentyseven"  : 27 ,
            "twentyeight"  :  28 ,
            "twentynine"  : 29 ,
            "thirty"  :  30 ,
            "thirtyone"  : 31 ,
            "thirtytwo"  :  32 ,
            "thirtythree"  : 33 ,
            "thirtyfour"  :  34 ,
            "thirtyfive"  : 35 ,
            "thirtysix"  :  36 ,
            "thirtyseven"  : 37 ,
            "thirtyeight"  :  38 ,
            "thirtynine"  : 39 ,
            "forty"  :  40 ,
            "fortyone"  : 41 ,
            "fortytwo"  :  42 ,
            "fortythree"  : 43 ,
            "fortyfour"  :  44 ,
            "fortyfive"  : 45 ,
            "fortysix"  :  46 ,
            "fortyseven"  : 47 ,
            "fortyeight"  :  48 ,
            "fortynine"  : 49 ,
            "fifty"  :  50 ,
            "fiftyone"  : 51 ,
            "fiftytwo"  :  52 ,
            "fiftythree"  : 53 ,
            "fiftyfour"  :  54 ,
            "fiftyfive"  : 55 ,
            "fiftysix"  :  56 ,
            "fiftyseven"  : 57 ,
            "fiftyeight"  :  58 ,
            "fiftynine"  : 59 ,
            "sixty"  :  60 ,
            "sixtyone"  : 61 ,
            "sixtytwo"  :  62 ,
            "sixtythree"  : 63 ,
            "sixtyfour"  :  64 ,
            "sixtyfive"  : 65 ,
            "sixtysix"  :  66 ,
            "sixtyseven"  : 67 ,
            "sixtyeight"  :  68 ,
            "sixtynine"  : 69 ,
            "seventy"  :  70 ,
            "seventyone"  : 71 ,
            "seventytwo"  :  72 ,
            "seventythree"  : 73 ,
            "seventyfour"  :  74 ,
            "seventyfive"  : 75 ,
            "seventysix"  :  76 ,
            "seventyseven"  : 77 ,
            "seventyeight"  :  78 ,
            "seventynine"  : 79 ,
            "eighty"  :  80 ,
            "eightyone"  : 81 ,
            "eightytwo"  :  82 ,
            "eightythree"  : 83 ,
            "eightyfour"  :  84 ,
            "eightyfive"  : 85 ,
            "eightysix"  :  86 ,
            "eightyseven"  : 87 ,
            "eightyeight"  :  88 ,
            "eightynine"  : 89 ,
            "ninety"  :  90 ,
            "ninetyone"  : 91 ,
            "ninetytwo"  :  92 ,
            "ninetythree"  : 93 ,
            "ninetyfour"  :  94 ,
            "ninetyfive"  : 95 ,
            "ninetysix"  :  96 ,
            "ninetyseven"  : 97 ,
            "ninetyeight"  :  98 ,
            "ninetynine"  : 99 ,
            "hundred"  :  100,
            "thousand"  :  1000,
            "million"  :  1000000
            }
    number_names_dict = {
        "zero" : 0,
        "one"  : 1 ,
        "two"  :  2 ,
        "three"  : 3 ,
        "four"  :  4 ,
        "five"  : 5 ,
        "six"  :  6 ,
        "seven"  : 7 ,
        "eight"  :  8 ,
        "nine"  : 9 ,
        "eleven"  : 11 ,
        "twelve"  :  12 ,
        "thirteen"  : 13 ,
        "fourteen"  :  14 ,
        "fifteen"  : 15 ,
        "sixteen"  :  16 ,
        "seventeen"  : 17 ,
        "eighteen"  :  18 ,
        "nineteen"  : 19 ,
        "ten"  :  10 ,
        "twenty"  :  20 ,
        "thirty"  :  30 ,
        "forty"  :  40 ,
        "fifty"  :  50 ,
        "sixty"  :  60 ,
        "seventy"  :  70 ,
        "eighty"  :  80 ,
        "ninety"  :  90 ,
        "hundred"  :  100 ,
        "thousand"  :  1000,
        "million"  :  1000000
        }
    ahad_number_names_dict = {
        "zero" : 0,
        "one"  : 1 ,
        "two"  :  2 ,
        "three"  : 3 ,
        "four"  :  4 ,
        "five"  : 5 ,
        "six"  :  6 ,
        "seven"  : 7 ,
        "eight"  :  8 ,
        "nine"  : 9
        }
#     ahadnext_number_names_dict = {
#         "ten"  :  10 ,
#         "eleven"  : 11 ,
#         "twelve"  :  12 ,
#         "thirteen"  : 13 ,
#         "fourteen"  :  14 ,
#         "fifteen"  : 15 ,
#         "sixteen"  :  16 ,
#         "seventeen"  : 17 ,
#         "eighteen"  :  18 ,
#         "nineteen"  : 19
#         }
    ashrat_number_names_dict = {
        "twenty"  :  20 ,
        "thirty"  :  30 ,
        "forty"  :  40 ,
        "fifty"  :  50 ,
        "sixty"  :  60 ,
        "seventy"  :  70 ,
        "eighty"  :  80 ,
        "ninety"  :  90
        }
    zeros_number_names_dict = {
        "hundred"  :  100 ,
        "thousand"  :  1000 ,
        "million"  :  1000000
        }
    words = ["zero","one","two","three","four","five","six","seven","eight","nine","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety","hundred","thousand","million"]
    zy_not_yxlist:list = []
    zy_not_yxlist2:list = []
    zy_not_yxstr:str = ''
    zy_not_yxstr2:str = ''
    zy_not_yxcoun:int = 0
    zy_not_yx_bool:bool = False
    one_multi_list:list = []
    one_multi_bool:bool = False
    zy_yx_bool:bool = False
    matching_words = ''
    y2 = ''
    matching_words2 = ''
    z = ''

    y = ''
    for key,x in enumerate(number_name_split):
#         getit_alp = False
#         getit_counter = 0
#         getit_str = ''
#         for keyge, getit_ in enumerate(x):
#             if getit_.isalpha():
#                 getit_alp = True
#                 getit_str += ''.join(getit_)
#                 
#             else:
#                 if getit_alp:
#                     getit_counter += 1
#                     if getit_counter == 1:
#                         if keyge < len(x)-1:
#                             getit_str += ''.join(getit_)
#                             getit_alp = False
#         x = getit_str
                   
                    
        
        
        z = ''
        y = ''
        y2 = ''
        zy_not_yxstr = ''
        zy_not_yxstr2 = ''
        zy_not_yxlist = []
        zy_not_yxlist2 = []
        
#         if not x.isalpha():
#             continue
        y = ''
        for i in x :
            
            y += ''.join(i)
            matching_words = '' # test remove this
            for word in words:
                if y in word.lower():
                    matching_words = [word]
            z = ''.join(matching_words)
            
            if not i.isalpha():
                y = ''
            if z == '':
                z = i
                y = i
            if z  == y and y == x and z.isalpha():
#                 print('y == x')
                
                if key < len(number_name_split)-1:
                    if key == 0:
                        y2 = ''
                    for i2 in number_name_split[key+1] :
                        y2 += ''.join(i2)
                        for word2 in words:
                            if y2 in word2.lower():
                                matching_words2 = [word2]
                        z2 = ''.join(matching_words2)
                    if number_name_split[key+1] == z2:
                        if z2.isalpha() and z.isalpha():
                            one_multi_list = [z]+[z2]
                            
                            one_multi_bool = True
                            zy_yx_bool = True

                if not one_multi_bool:
                    
#                     print('\nfound1_alone\n')
                    found1_alone = False
                    for n in number_names_dict.items():
                        if n[0] == x:
                            found1_alone = True
                            text1_alone =  n[1]
                            result1_alone = replace_index(number_name_split,key,str(text1_alone))
                            string_1_alone = ' '.join(result1_alone)
                            break
                    if found1_alone:
                        found1_alone = False
                        return isnumbername(string_1_alone)
            
            if z  == y and y != x:
                
                
                zy_not_yxcoun += 1
                zy_not_yxlist2.append(z)
                if z.isalpha():
                    
                        
                    zy_not_yxlist.append(z)
                zy_not_yxstr += ''.join(z)
                
                    
#                 if key == 1:
#                     print('zy_not_yxlist: ',zy_not_yxlist)
#                     print('zy_not_yxstr: ',zy_not_yxstr)
                if zy_not_yxstr == x:
#                     if len(zy_not_yxlist2) > 2
                    n = ''.join(zy_not_yxlist)
                    if len(n) == len(zy_not_yxstr) or len(n)+1 == len(zy_not_yxstr):
#                         if key == 1:
#                             print('\n y != x  2\n')
                        one_multi_list = zy_not_yxlist
                        zy_not_yx_bool = True
                        one_multi_bool = True
                        zy_not_yxlist: list = []
                        zy_not_yxstr: str = ''
                y = ''
            elif z != y  and y == x:
                # not number
                pass
            if one_multi_bool:
#                 if key == 1:
#                     print('\n one_multi_bool\n')
                for o_m_key_1,o_m_value_1 in enumerate(one_multi_list):
                    if o_m_key_1 == 1:
                        zy_not_yx_bool = False
                        zy_yx_bool = False
                        one_multi_bool = False
                        break
                    found = False
                    for i_2 in ahad_number_names_dict.items():
                        if i_2[0] == o_m_value_1:
                            found = True
                            found2 = False
                            
                            for i_3 in zeros_number_names_dict.items():
#                                 if not zy_yx_bool:
#                                     print('yes')
#                                 else:
#                                     print('no')
                                if i_3[0] == one_multi_list[o_m_key_1+1]:
                                    found2 = True
                                    o_m_text_1 =  str(i_2[1])+str(i_3[1])[1:]
                                    if zy_yx_bool:
                                        number_name_split = remove_index(number_name_split,key+1)
                                    o_m_result_1 = replace_index(number_name_split,key,str(o_m_text_1))
                                    o_m_new_str_1 = ' '.join(o_m_result_1)
                                    break
                            if found2:
                                found2 = False
                                return isnumbername(o_m_new_str_1)
                    if not found:
                        for i_4 in ashrat_number_names_dict.items():
                            if i_4[0] == o_m_value_1:
                            
                                found = True
                                for i_5 in ahad_number_names_dict.items():
                                    if i_5[0] == one_multi_list[o_m_key_1+1]:
                                        found2 = True
                                        textfound2 =  str(i_4[1])[0]+str(i_5[1])
                                        if zy_yx_bool:
                                            number_name_split = remove_index(number_name_split,key+1)
                                        resultfound2 = replace_index(number_name_split,key,str(textfound2))
                                        new_string_found2 = ' '.join(resultfound2)
                                        break
                                if found2:
                                    found2 = False
                                    return isnumbername(new_string_found2)

                                zy_not_yx_bool = False
                zy_yx_bool = False
                one_multi_bool = False
                found1_alone = False
                for n in number_names_dict.items():
                    if n[0] == x:
                        found1_alone = True
                        text1_alone =  n[1]
                        result1_alone = replace_index(number_name_split,key,str(text1_alone))
                        string_1_alone = ' '.join(result1_alone)
                        break
                if found1_alone:
                    found1_alone = False
                    return isnumbername(string_1_alone)


    return number_name
#     except Exception as e:
        
#         return '\nError:\n'+str(e)
to_print =isnumbername('one-hundred, one,  one-hundred two five and five hundred two and one thousand and one and two') # make 11 , 12
print('to_print:\n',to_print)
# use isnumber def -> True , False if str.split so len of it > 1, and numbername value = True, then use this trans def
# short ahad and ashrat for loop

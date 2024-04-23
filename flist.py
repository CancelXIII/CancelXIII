def flist(target_main_name = None):
    """Return list without \n in end from file
        only .py and .txt
    Args:
        target_main_name (str): type = txt default.
    Returns:
        (None) if error, target_main_name missing, another file types else .py or .txt
        list: without \n in end. 
    """
    
    if target_main_name==None:
        return None
    else:
        if type(target_main_name) == str:
            target_main_name = target_main_name.strip()
            if not target_main_name.endswith('.py') and not target_main_name.endswith('.txt'):
                target_main_name = target_main_name+'.txt'
                
            elif target_main_name.endswith('.py') or target_main_name.endswith('.txt'):
                pass
            else:
                return None
        else:
            return None
    open_ = open(target_main_name,'r',encoding='utf-8-sig')
    read_lines = open_.readlines()
    read_lines2 = []
    for i in read_lines :
        read_lines2.append(i.strip())
    open_.close()
    return read_lines2

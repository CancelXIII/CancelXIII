def isPrime(get_it = None, message_ = None):
  list_ = False
  bool_values = []
  if type(get_it) is list:
    n = get_it
    list_ = True
  else:
    if type(get_it) is int:
      n = [get_it]
  for i in n:
    result =  i / 2 
    all_remian_zero = True
    found_dot = False
    if '.' in str(result):
      for key,value in enumerate(str(result)):
        if value == '.':
          found_dot = True
          index_ = key
          for ii in  str(result)[index_+1:]:
            if ii != '0':
              all_remian_zero = False
              break
        if all_remian_zero == False:
          break
        if found_dot == True:
          break
    if list_ == False:
      if all_remian_zero == False:
        if message_ == True:
          print(i , ': Prime')
        return True
      else:
        if message_ == False:
          print(i , ': not Prime')
        return False
    elif list_ == True:
      if all_remian_zero == False:
        if message_ == True:
          print(i , ': Prime')
        bool_values.append(True)
      else:
        if message_ == True:
          print(i , ': not Prime')
        bool_values.append(False)
  return bool_values

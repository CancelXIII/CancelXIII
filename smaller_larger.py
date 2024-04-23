print('welcome in get larger/smaller numbers\n|s| start  --  |e|exit')
user_select = 'a'
while True:
    if user_select == 'a':
        user_select = input ()
    if user_select == 'e':
        break
    elif user_select == 's':
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        numbers_list = []
        while True:
            get_input = input('|e| end -- |f|finish all program \n').strip()
            if get_input.strip() == '' :
                continue
            if get_input == 'f':
                break
            if get_input == 'e' :
                break
            else:
                not_number = False
                for ii in get_input:
                    if ii == '.' or ii == '':
                        continue
                    if ii not in numbers:
                        not_number = True
                        break
                if not_number == False :
                    numbers_list.append(get_input)
        if get_input == 'f':
            break
        if len(numbers_list) >1 :
            similar = True
            first_number = numbers_list[0]
            for iii in numbers_list[1:]:
                if iii != first_number:
                    similar = False
                    break
            if similar == False:
                larger = numbers_list[0]
                smaller = numbers_list[0]
                for value in numbers_list[1:]:
                    if value > larger:
                        larger = value
                    if value < smaller:
                        smaller = value
                print('larger is :',larger,' ','smaller is :',smaller)
                
            elif similar == True:
                print('all numbers is similar')
                      
        elif len(numbers_list) <=1 :
            print('there are not enough numbers')
        user_select = input('start enter new numbers again?\n|s| start again  --  |e|exit\n')
        if user_select != 's':
            print('end')
            break
    else:
        print('wrong input, try again')
        user_select = 'a'
    



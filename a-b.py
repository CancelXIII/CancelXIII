import sys
path = sys.argv[0]
while True:
    A = input ()
    cancel = input()
    if cancel != A:
        open_file = open('a_b.py','r')
        read_file = open_file.readlines()
        open_file.close()
        old_line = '    A = input ()\n'
        new_line = '    B = input ()\n'
        new_list = []
        for ii in read_file:
            if ii == old_line:
                new_list.append(new_line)
            else:
                new_list.append(ii)
        write_file = open(path,'w')
        for iii in new_list:
            write_file.write(iii)
        write_file.close()

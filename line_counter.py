files_counted = []
total_text = 0
total_exec = 0
while 1:
    try:
        valin = str(input('file to count:'))
        file = open(valin)
        split_list = file.read().split('\r\n')
        text_lines = 0
        exec_lines = 0
        for line in split_list:
            
            #check if artifact of splitting
            if line != '':
                text_lines += 1
                if valin not in files_counted:
                    total_text += 1
                
                #check if comment
                if line[0] != '#':
                    exec_lines += 1
                    if valin not in files_counted:
                        total_exec += 1
        files_counted.append(valin)
        print('files counted: ', files_counted )
        print('number of counted files: ', len(files_counted))
        print('----')
        print('number of lines w/ text: ',text_lines )
        print('number of executable lines:', exec_lines)
        print('----')
        print('total counted lines w/ text: ',total_text )
        print('total counted executable lines:', total_exec)
        
        print('----------------------------')
    except OSError:
        print("EROR: input file not found: try using '/' not '.' as seperator, try adding '.py' if looking at one file")
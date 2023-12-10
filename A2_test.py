from A2 import stp_client, stp_server, get_file_parameters, \
    valid_commands_format, close_socket, prepare_socket, \
    validate_configuration, SERVER_ADDRESS, get_parameter_value, write
from threading import Thread
from socket import socket, SOCK_STREAM, AF_INET

files = [None for _ in range(17)]

commands = [['tricky!'],
            ['?name:text1.txt?','$size:104$','$type:text$'],
            ['$type:pic$','(size:6501)','$name:text2.txt$'],
            ['$type:pic$','$name:text3.txt$','*size:7899*'],
            ['$type:text$','$name:text4.txt$','%size:6501%','$count=7$'],
            ['$type:text$'],
            ['$type:text$','$size:512$'],
            ['$name:file3.txt$','$count:30$','$size:512$'],
            ['$type:pic$','$size:6501$','$name:text2$'],
            ['$size:-4$','$name:file2.pdf$','$type:text$'],
            ['$name:pic1.png$','$size:1024$','$type:mov$'],
            ['$type:text$','$size:607$','$name:sample1.txt$'],
            ['$name:sample2.html$','$type:text$','$size:428$'],
            ['$name:sample3.rtf$','$type:text$','$size:42859$'],
            ['$type:pic$','$size:4520$','$name:sample4.png$'],
            ['$name:sample5.jpg$','$type:pic$','$size:7876$']]

def wipe_files(filelist):
    """
    ----------------------------------------------------
    Parameters:   filelist (list)
    Return:       -
    Description:  clear the contents of all given files
    Errors:       If operation fails, an exception is raised
    ---------------------------------------------------
    """
    try:
        for file in filelist:
            outfile = open(file,'w')
            outfile.close()
    except Exception as e1:
        print('clear_files(Exception): {}'.format(e1))
    return

# get_file_parameters
def task1():
    filenames = ['sample1.txt','sample2.html','sample3.rtf',
                 'sample4.png','sample5.jpg','sample6.gif','sample7.pdf',
                 'readme','readme.txt','readme.pdf']
    try:    
        file = 'A2_student_basic.txt'
        write(file,"-" * 40)
        write(file,"\nStart of task1 Testing\n\n")

        for filename in filenames:
            parameters = get_file_parameters(filename)
            write(file,'get_file_parameters({:12s}) = {}\n'.format(filename,parameters))
        write(file,'\n')
    except Exception as e:
        write(file,'Exception(task1): {}\n'.format(e))

    write(file,'End of task1 Testing\n')
    write(file,"-" * 40)
    write(file,'\n')
    return

# valid_commands_format
def task2():
    commands_list = ['',[],['tricky!'],
                     ['?name:text1.txt?','$size:104$','$type:text$'],
                     ['$type:pic$','(size:6501)','$name:text2.txt$'],
                     ['$type:pic$','$name:text3.txt$','*size:7899*'],
                     ['$type:pic$','$name:t.pic$','%size:7%','$n=7$'],
                     'hackathon', '?name:text1.txt?$size:104$$type:text$',
                     '$type:pic$(size:6501)$name:text2.txt$',
                     '$type:pic$$name:t.pic$%size:7%$n=7$',
                     '$name:sam6.gif$$type:pic$$size:7642$',
                     ['$name:sam6.gif$', '$type:pic$','$size:7642$'],
                     ['$size:7642$','$name:sam6.gif$', '$type:pic$'],
                     ['$name:r.jpg$','$type:pic$','$pad:q$','$size:7$']]
    try:    
        filename = 'A2_student_basic.txt'
        write(filename,"-" * 40)
        write(filename,"\nStart of task2 Testing\n\n")

        for commands in commands_list:
            result = valid_commands_format(commands)
            write(filename,'valid_commands_format({}) = {}\n'.format(commands,result))
        write(filename,'\n')
    except Exception as e:
        write(filename,'Exception(task2): {}\n'.format(e))

    write(filename,'End of task2 Testing\n')
    write(filename,"-" * 40)
    write(filename,'\n')
    return

#close_socket
def task3():
    try:
        filename = 'A2_student_basic.txt'
        write(filename,"-" * 40)
        write(filename,"\nStart of task3 Testing\n\n")
    
        s1 = socket()
        write(filename,'Case 1: invalid socket type\n')
        write(filename,str(close_socket(filename,s1,'framework')))
        write(filename,'\n')
        
        write(filename,'Case 2: socket of type server\n')
        write(filename,str(close_socket(filename,s1,'server')))
        write(filename,'\n')
        
        write(filename,'Case 3: socket of type client\n')
        s2 = socket()
        write(filename,str(close_socket(filename,s2,'client')))
        write(filename,'\n')
        
        write(filename,'Case 4: connected socket\n')
        s3 = socket()
        s3.connect(('www.google.com',80))
        write(filename,str(close_socket(filename,s3,'client')))
        write(filename,'\n')
        
        write(filename,'Case 5: closed socket\n')
        write(filename,str(close_socket(filename,s3,'client')))
        write(filename,'\n')
        
        write(filename,'Case 6: listening socket\n')
        s4 = socket()
        s4.bind(('127.0.0.1',4444))
        s4.listen()
        write(filename,str(close_socket(filename,s4,'server')))
        write(filename,'\n')
        
    except Exception as e:
        write(filename,'Exception(task3): {}\n'.format(e))
    
    write(filename,'\nEnd of task3 Testing\n')
    write(filename,"-" * 40)
    write(filename,'\n')
    return

#prepare_socket
def task4():
    try:
        filename = 'A2_student_basic.txt'
        write(filename,"-" * 40)
        write(filename,"\nStart of task4 Testing\n\n")
    
        write(filename,'Case 0: Invalid type\n')
        sock = prepare_socket(filename,'supercomputer',None)
        if sock == None:
            write(filename,'validated\n')
        else:
            write(filename,'validation failed\n')            
        write(filename,'\n')
        
        write(filename,'Case 1: Client socket\n')
        sock = prepare_socket(filename,'client',None)
        if type(sock) == socket and sock.type == SOCK_STREAM and sock.family == AF_INET:
            write(filename,'validated\n')
            close_socket(filename,sock)
        else:
            write(filename,'validation failed\n')
        write(filename,'\n')
        
        write(filename,'Case 2: Server socket\n')
        sock = prepare_socket(filename,'server',('localhost',4100))
        if type(sock) == socket and sock.type == SOCK_STREAM and \
            sock.family == AF_INET and sock.getsockname() == ('127.0.0.1',4100):
            write(filename,'validated\n')
            close_socket(filename,sock)
        else:
            write(filename,'validation failed\n')
        write(filename,'\n')
        
        write(filename,'Case 3: Server socket with invalid bound\n')
        sock = prepare_socket(filename,'server',('localhost',420000))
        if sock == None:
            write(filename,'validated\n')
        else:
            write(filename,'validation failed\n')    
    
    except Exception as e:
        write(filename,'Exception(task4): {}\n'.format(e))
    
    write(filename,'\nEnd of task4 Testing\n')
    write(filename,"-" * 40)
    write(filename,'\n')
    return

# validate_configuration
def task5():
    try:
        filename = 'A2_student_basic.txt'
        write(filename,"-" * 40)
        write(filename,"\nStart of task5 Testing\n\n")
    
        commands_list = [['?name:text1.txt?','$size:104$','$type:text$'],
                     ['$name:file1.txt$','$type:text$'],
                     ['$pad:q$','$name:r.jpg$','$size:7$'],
                     ['$name:file1.txt$','$type:text$','$size:0$'],
                     ['$type:text$','$name:file1.t.xt$','$size:78$'],
                     ['$name:file1.txt$','$type:text$','$size:75$'],
                     ['$name:r.jpg$','$type:pic$','$pad:q$','$size:7$']]

        for commands in commands_list:
            result = validate_configuration(commands)
            write(filename,'validate_configuration({}):\n'.format(commands))
            write(filename,str(result))
            write(filename,'\n\n')
    except Exception as e:
        write(filename,'Exception(task5): {}\n'.format(e))

    write(filename,'End of task5 Testing\n')
    write(filename,"-" * 40)
    write(filename,'\n')
    return

# get_parameter_value
def task6():
    commands = [['$name:file1.txt$','$type:text$','$size:0$'],
                ['$type:pic$','$size:150$','$name:file2.png$'],
                ['$size:4180$','$name:file3.jpg$','$type:pic$'],
                ['$size:791$','$name:file4.html$','$type:text$'],
                '$name:file1.txt$$type:text$$size:14$',
                '$type:pic$$size:150$$name:file2.png$',
                ['$size:4180$','?name:file3.jpg?','$type:pic$']]
    parameters = ['type','size','name','length','size','name','type']
    try:    
        filename = 'A2_student_basic.txt'
        write(filename,"-" * 40)
        write(filename,"\nStart of task6 Testing\n\n")

        for i in range(len(parameters)):
            value = get_parameter_value(commands[i],parameters[i])
            write(filename,'get_parameter_value({},{}) = {}\n'.format(commands[i],parameters[i],value))
        write(filename,'\n')
    except Exception as e:
        write(filename,'Exception(task6): {}\n'.format(e))

    write(filename,'End of task6 Testing\n')
    write(filename,"-" * 40)
    write(filename,'\n')
    return

#Testing for tasks 7 - 13
# Task 7: '#10:ILLEGAL_COMMAND#'
# Task 8: '#20:COMMAND_MISSING#'
# Task 9: '#30:BAD_CONFIGURATION#'
# Task 10: Transfer Text files
# Task 11: Transfer pic files
def task(args):
    num,count,start = args

    server_file = 'A2_student_server.txt'
    write(server_file,"-" * 40)
    write(server_file,"\nStart of task{} Testing\n\n".format(num))
    server_thread = Thread(target=stp_server,args=(server_file,SERVER_ADDRESS,count))
    server_thread.start()
    
    client_file = 'A2_student_client.txt'
    write(client_file,"-" * 40)
    write(client_file,"\nStart of task{} Testing\n\n".format(num))
    
    for i in range(start,start+count):
        stp_client(client_file,SERVER_ADDRESS,files[i],commands[i])
        write(client_file,'\n')
    
    write(client_file,'End of task{} Testing\n'.format(num))
    write(client_file,"-" * 40)
    write(client_file,'\n')

    write(server_file,'\nEnd of task{} Testing\n'.format(num))
    write(server_file,"-" * 40)
    write(server_file,'\n')
    server_thread.join()

    return

# Task 12: Transfer files with no commands
def task12():

    server_file = 'A2_student_server.txt'
    write(server_file,"-" * 40)
    write(server_file,"\nStart of task12 Testing\n\n")
    server_thread = Thread(target=stp_server,args=(server_file,SERVER_ADDRESS,3))
    server_thread.start()
    
    client_file = 'A2_student_client.txt'
    write(client_file,"-" * 40)
    write(client_file,"\nStart of task12 Testing\n\n")
    
    files = ['sample2.html','sample4_copy.png','sample7.pdf']
    for i in range(len(files)):
        stp_client(client_file,SERVER_ADDRESS,files[i],None)
        write(client_file,'\n')
        
    write(client_file,'End of task12 Testing\n')
    write(client_file,"-" * 40)
    write(client_file,'\n')

    write(server_file,'\nEnd of task12 Testing\n')
    write(server_file,"-" * 40)
    write(server_file,'\n')
    server_thread.join()

    return
  
def main():
    print('Starting Testing')
    
    files = ['A2_student_basic.txt','A2_student_client.txt','A2_student_server.txt',
             'sample1_copy.txt','sample2_copy.html','sample3_copy.rtf','sample4_copy.png',
             'sample4_copy_copy.png','sample5_copy.jpg']
    wipe_files(files)

    try:    
        task1()
        print('Task 1 Testing Complete')
    except Exception as e1:
        print('Unhandled exception in task1: {}'.format(e1))
        
    try:
        task2()
        print('Task 2 Testing Complete')
    except Exception as e2:
        print('Unhandled exception in task2: {}'.format(e2))
    
    try:        
        task3()
        print('Task 3 Testing Complete')
    except Exception as e3:
        print('Unhandled exception in task3: {}'.format(e3))
    
    try:        
        task4()
        print('Task 4 Testing Complete')
    except Exception as e4:
        print('Unhandled exception in task4: {}'.format(e4))
    
    try:        
        task5()
        print('Task 5 Testing Complete')
    except Exception as e5:
        print('Unhandled exception in task5: {}'.format(e5))
    
    try:        
        task6()
        print('Task 6 Testing Complete')
    except Exception as e6:
        print('Unhandled exception in task6: {}'.format(e6))
    
    args = [[7,5,0],[8,3,5],[9,3,8],[10,3,11],[11,2,14]]
    #Tasks 7-11
    for arg in args:
        try:
            task(arg)
            print('Task {} Testing Complete'.format(arg[0]))
        except Exception as e:
            print('Unhandled exception in task{}: {}'.format(arg[0],e))
    
    try:        
        task12()
        print('Task 12 Testing Complete')
    except Exception as e12:
        print('Unhandled exception in task12: {}'.format(e12))
                        
    return

main()

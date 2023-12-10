#-------------------------
# Network Programming and Applications
# First Semester (2023-2024)
# Assignment 2
#-------------------------

#-------------------------
# Student Name: Yazan Matarweh
# Student ID  : 20180596
#-------------------------

# put your import statements between these two lines
#----------------------------------
from socket import socket,SHUT_RDWR,AF_INET,SOCK_STREAM,SO_ACCEPTCONN,SOL_SOCKET
#----------------------------------

BUFFER = 64                             #receive buffer for commands
ENCODING = 'utf-8'                      #encoding used by both ends
SERVER_ADDRESS = ('localhost',6330)     #server socket address
BACKLOG = 6                             #listen backlog
BLOCK_SIZE = 128                        #block size for upload/download
TEXT_EXTENSIONS = ['txt','rtf','html']  #valid text file extensions
PIC_EXTENSIONS = ['png','jpg','gif']    #valid picture file extensions

def write(file,msg):
    fh = open(file,'a')
    fh.write(str(msg))
    fh.close()
    return

'_______________________________________________________________'

def prepare_socket(filename,sock_type='client',address=None):
    """
    ----------------------------------------------------
    Parameters:   filename (str)
                  sock_type (str): 'client' or 'server'
                  address (?): None or IPv4 socket address
    Return:       sock (socket)
    Used by:      Client and Server
    Description:  Creates and returns a socket
                  if invalid sock_type:
                      return None
                  if sock_type is client:
                      create socket and return it
                  if sock_type is server:
                      create + bind + listen and return the socket
                  
                  if socket creation is successful:
                      write to file: 'stp(<type>): socket created'
                  otherwise:
                      write to file: 'stp(<type>): socket creation failed
                      return None
                  
                  if bind is successful:
                      write to file: 'stp(server): bound to <address>'
                  otherwise:
                      write to file: 'stp(server): bind fatal error'
                      return None
                  
                  if listen is successful:
                      write to file: 'stp(server): listening ...\n'
                  otherwise:
                      write to file: 'stp(server): listen fatal error'
                      return None                      
    ---------------------------------------------------
    """
    try:
        if sock_type == 'client':
                client_socket = socket()
                write(filename,f'stp({sock_type}): socket created')
                return client_socket

        elif sock_type == 'server':
            server_socket = socket()
            write(filename,f'stp({sock_type}): socket created')

            try:
                server_socket.bind(address)
                write(filename,f's  tp({sock_type}): bound to {address}')
                try:    
                    server_socket.listen(BACKLOG)
                    write(filename,f'stp({sock_type}): listening ...\n')
                
                except:
                    write(filename,f'stp({sock_type}): listen fatal error')
            except:
                write(filename,f'stp({sock_type}): bind fatal error')
                return None

            return server_socket  
          
        else:
            return None 
        
    except:
        write(filename,f'stp({sock_type}): socket creation failed')
        return None    


'_______________________________________________________________'

def stp_server(filename,server_address,client_count):
    """
    ----------------------------------------------------
    Parameters:   filename (str)
                  server_address (tuple): IPv4 socket address
                  client_count (int): number of clients to serve before closing
    Return:       -
    Used by:      Server
    Description:  Main server function.
                  Creates a server socket, 
                  accept clients and direct to handle_client
                      writes to outfile: 'stp(server): accepted client connection <#>'
                  Serves given number of clients then close
    Dependencies: prepare_socket, close_socket, handle_client
    ---------------------------------------------------
    """
    # your code here
    return

'_______________________________________________________________'

def handle_client(filename,connection):
    """
    ----------------------------------------------------
    Parameters:   filename (str)
                  connection (socket): client socket accepted by server
    Return:       -
    Used by:      Server
    Description:  Server function to handle clients
                  1- Receives commands from client
                  2- Process commands and send a response
                  3- if valid configuration, download file
                  4- close connection
    Exceptions:   Exception: 'stp(server): handle client error'
    Dependencies: receive_commands, download_file, close_socket
    ---------------------------------------------------
    """
    # your code here
    return

'_______________________________________________________________'

def receive_commands(filename : str,connection :socket) -> str | list:
    """
    ----------------------------------------------------
    Parameters:   filename (str)
                  connection (socket): client socket accepted by server
    Return:       response (str)
                  commands (list)
    Used by:      Server
    Description:  Receive and process client commands
                  1- Receives commands from client until '<configuration_complete>'
                      write to file: received commands
                  2- Check if given configuration/commands is valid
                      if valid: write to file: configuration
                  3-Send response to client
                      write to file: sent response
                  4- return copy of response and processed commands
    Dependencies: validate_configuration
    ---------------------------------------------------
    """
    
    
    return None

'_______________________________________________________________'

def validate_configuration(commands):
    """
    ----------------------------------------------------
    Parameters:   commands (list or str)
    Return:       response (str) one of the following messages:
                      '#10:ILLEGAL_COMMAND#'
                      '#20:COMMAND_MISSING#'
                      '#30:BAD_CONFIGURATION#'
                      '<configuration_approved>'
                  commands (list)
    Used by:      Server
    Description:  Check if given commands are valid
                  1- Check if they have proper format
                      if invalid: return '#10:ILLEGAL_COMMAND#' and empty commands list
                  2- Check if it has filename, filetype and filesize
                      if invalid: return '#20:COMMAND_MISSING#' and empty commands list
                  3- Check if filename, filetype and filesize has valid values
                      if invalid: return '#30:BAD_CONFIGURATION#' and empty commands list
                  4- if validated: return '<configuration_approved>' and commands list
    Dependencies: valid_commands_format, get_parameter_value, valid_filename
    ---------------------------------------------------
    """

    if not valid_commands_format(commands):
        return ('#10:ILLEGAL_COMMAND#',[])

    #commands = _to_standard_command_format(commands)
    file_size = get_parameter_value(commands,'size')
    file_type = get_parameter_value(commands,'type')
    file_name = get_parameter_value(commands,'name')

    if  not file_size or \
        not file_type or  \
        not file_name        :
            return (('#20:COMMAND_MISSING#',[]))
    
    if  not file_size.split(':')[1].isnumeric() or \
        not valid_filename(file_name) or \
        (not file_type in PIC_EXTENSIONS and file_type not in TEXT_EXTENSIONS):
        return ('#30:BAD_CONFIGURATION#',[])
    
    return ('<configuration_approved>', commands)


'_______________________________________________________________'

def download_file(out_filename,sock,commands):
    """
    ----------------------------------------------------
    Parameters:   out_filename (str)
                  sock (socket)
                  commands (list)
    Return:       True / False
    Used by:      Server
    Description:  downloads a file from the client using given configuration
                  The file contents are received as text or binary depending on file type
                  In both cases, the function receives BLOCK_SIZE bytes in each receive call
                  If download of "filename.ext" is successful:    
                      Store file as: filename_copy.ext
                      write to file: 'stp(server): download complete'
                      return True
                  If there was an error in download
                      write to file: 'stp(server): receive error: <Exception>'
                      return False   
                  Upon start of download write to file: 'stp(server): downloading ...'
                      write to file every received block
    ---------------------------------------------------
    """
    # your code here
    return None

'_______________________________________________________________'

def get_file_parameters(filename) -> list:
    """
    ----------------------------------------------------
    Parameters:   filename(str)
    Return:       parameters (list)
    Used by:      Client
    Description:  Analyzes a given file to get its type and size

                    if invalid filename: return empty list
    
                    inspect file extension to get its type as defined by
                    TEXT_EXTENSIONS and PIC_EXTENSIONS in utilities
                        if undefined: do not add type parameter
                    compute file size:
                        if file type is text: count number of characters
                        if file type is pic: count number of bytes
                        if file does not exit: do not add size     
    ---------------------------------------------------
    """
    param_list = []

    if not valid_filename(filename):
        return param_list
    
    param_list.append(f'$name:{filename}$')

    file_type = _get_file_type(filename)
    
    if file_type:
        param_list.append(f'$type:{file_type}')    

    #Implementation 2:
    
    # if file_extension in TEXT_EXTENSIONS:
    #     param_list.append('$type:text$')

    # elif file_extension in PIC_EXTENSIONS:
    #     param_list.append('$type:pic$') 


    
    try: 
        #if file_extension in TEXT_EXTENSIONS:        
        if file_type == 'text':
            with open(filename,'rt',encoding=ENCODING) as textfile:
                file_size = len(textfile.read())

        #elif file_extension in PIC_EXTENSIONS: 
        elif file_type == 'pic': 
            with open(filename,'rb',encoding=None) as image:
                file_size = len(bytearray(image.read()))
        
        else:
            return param_list        

        param_list.append(file_size)

    except FileNotFoundError:
        pass #TODO: Check if there's something to implement here

    return param_list

'_______________________________________________________________'

def close_socket(filename,sock : socket,sock_type='client'):
    """
    ----------------------------------------------------
    Parameters:   filename (str)
                  sock (socket object)
                  sock_type (str): 'client' or 'server'
    Return:       True or False
    Used by:      Client and Server
    Description:  if invalid type: take no action and return False
                  if socket is closed: take no action and return False
                  DONE

                  if listening server socket: close
                  DONE

                  if connected client socket: shutdown then close
                  DONE

                  if disconnected client socket: close
                  
                  when shutdown is successful write to file:
                      'stp(<type>): connection shutdown'
                  otherwise:
                      'stp(<type>): shutdown failed'

                  when close is successful write to outfile:
                      'stp(<type>): socket closed'
                  otherwise:
                      'stp(<type>): socket close failed'

                  if both shutdown/close are successful: return True
                      otherwise: return False
    ---------------------------------------------------
    """
    #TODO finish this
    if sock_type not in ('client','server') or sock.fileno() < 1:
        return False
    
    if sock.getsockopt(SOL_SOCKET,SO_ACCEPTCONN):
        sock.close()
        write(filename,f'stp({sock_type}): socket closed')
    
    elif "raddr" in str(sock):
        try:
            sock.getpeername() #TODO: probably better than trying to recv but figure out if there's a better way    
            sock.shutdown(SHUT_RDWR)
            write(filename,f'stp({sock_type}): connection shutdown')

        except BrokenPipeError:
            pass

        except:
            write(filename,f'stp({sock_type}): shutdown failed')
       
        finally:
            try:
                sock.close()
                write(filename,f'stp({sock_type}): socket closed')
                return True
            except:
                write(filename,f'stp({sock_type}): socket close failed')

    return False

'_______________________________________________________________'

def valid_commands_format(commands : str|list):
    """
    ----------------------------------------------------
    Parameters:   commands(str or list)
    Return:       True or False
    Used by:      Client and Server
    Description:  Inspects given commands and check if its format is valid
                  valid commands:
                      1- contain at least one command
                      2- every command is formatted as: $<command>$
    ---------------------------------------------------
    """

    if type(commands) not in (str,list):
        return False
    
    elif(len(commands) == 0):
        return False

    commands = _to_standard_command_format(commands)

    for command in commands: 
        if  not command[-1].isalnum() or            \
            not command[0].isalpha() or             \
            not command.count(':') == 1:
            return False

    return True

'_______________________________________________________________'

def get_parameter_value(commands : list|str ,parameter : str) -> str:
    """
    ----------------------------------------------------
    Parameters:   commands (str or list)
                  parameter (str)
    Return:       value (str)
    Used by:      Client and Server
    Description:  Returns the value of the given parameter in commands
                    
                    if commands are not in valid format: return None
                    if parameter undefined: return None
                    Otherwise, return value in string format

    Dependencies:  valid_commands_format
    ---------------------------------------------------
    """

    if not valid_commands_format(commands):
         return None
    
    #commands_dict = {}
    
    commands = _to_standard_command_format(commands)

    for command in commands:
        param_name , value = command.split(':')
        if param_name == parameter:
            return str(value) 
    return 

    #   commands_dict[param_name] = value

    # if parameter in commands_dict:
    #     return commands_dict[parameter]
    
    # else:
    #     return None

        
'_______________________________________________________________'

def stp_client(out_filename,server_address,filename=None,commands=None):
    """
    ----------------------------------------------------
    Parameters:   out_filename (str)
                  server_address (tuple): IPv4 socket address
                  filename (str or None): filename to be uploaded
                  commands (list or None): file transfer commands
    Return:       -
    Used by:      Client
    Description:  Main client function, performs the following
                  1- Creates a client socket
                  2- Connect to server
                  3- if commands is None extract file configuration
                  4- Send commands to server
                  5- Receive response from server
                  6- If configuration is approved by server: upload file
                  7- close the connection and socket
    Dependencies: prepare_socket, close_socket, connect_to_server, 
                    get_file_parameters, send_commands, get_config_response,
                    upload_file
    Errors:        The function returns in the following cases:
                        filename and commands are None
                        Creating the socket failed
                        Connecting to server failed
    Exception:    write to file: 'stp(client): Exception: <Exception>'
    ---------------------------------------------------
    """
    
    try:
        client_socket = prepare_socket(out_filename)
        client_socket.connect(server_address)
        pass

    except Exception as e:
        write(out_filename,f'stp(client): Exception: {e}')
        pass

    return None

'____________________________________________________'

def connect_to_server(filename,sock,server,):
    """
    ----------------------------------------------------
    Parameters:   filename (str)
                  sock (socket)
                  server (tuple): server address
    Return:       True / False
    Used by:      Client
    Description:  connects given socket to the given address
                  if successful: return True
                  if connect fails: 
                      close socket
                      write to file: stp(client): connect fatal error
                      return False
    Dependencies: close_socket
    ---------------------------------------------------
    """
    # your code here
    return None

'____________________________________________________'

def send_commands(filename : str, sock : socket, commands : list):
    """
    ----------------------------------------------------
    Parameters:   filename (str)
                  sock (socket)
                  commands (list)
    Return:       True / False
    Used by:      Client
    Description:  send given commands to server
                  each command is sent using a separate send operation
                  write to file each sent command
                  When done send: '<configuration_complete>' and return True
                  if sending fails: 
                      write to file: 'stp(client): send operation failed'
                      return False
    ---------------------------------------------------
    """

    try:
        for command in commands:
            sock.sendall(command)
            write(filename,f'stp(client): sent: {command}')
        
        sock.sendall('<configuration_complete>')
        return True

    except:
        write(filename,'stp(client): send operation failed')
        return False

'____________________________________________________'

def get_config_response(filename,sock):
    """
    ----------------------------------------------------
    Parameters:   filename (str)
                  sock (socket)
    Return:       response (str)
    Used by:      Client
    Description:  receives the server response to the sent commands
                  if successful: 
                      write to file: 'stp(client): received: <msg>'
                      return response message
                  if failed: write to outfile:
                      write to file: 'stp(client): configuration receive error: <Exception>'
                      return empty string
    ---------------------------------------------------
    """
    # your code here
    return None

'____________________________________________________'

def upload_file(out_filename,sock,commands):
    """
    ----------------------------------------------------
    Parameters:   out_filename (str)
                  sock (socket)
                  commands (list)
    Return:       True/False
    Used by:      Client
    Description:  uploads given file to the server
                  Send file as text or binary for pictures
                  file is sent in blocks of size BLOCK_SIZE
                  write to file: 'stp(client): uploading ...'
                  write to file blocks as: 'stp(client): sent: <block>'
                  write to file: 'stp(client): uploading complete'
    Errors:       if commands are not in valid format: return False
                  if opening file fails: write 'stp(client): uploading failed\n', return False
                  other errors: 'stp(client): uploading failed: <Exception>', return False
    ---------------------------------------------------
    """
    # your code here
    return None
'____________________________________________________'

def valid_filename(filename : str) -> bool:
    """
    ----------------------------------------------------
    Parameters:   filename (str)
    Return:       True/False
    Description:  Checks if given input is a valid filename 
                  a filename should have at least 3 characters
                  and contains a single dot that is not the first or last character
    ---------------------------------------------------
    """
    if  (type(filename) != str) or                          \
        (len(filename) < 3) or                               \
        (filename.count('.') != 1) or                         \
        (filename[0] == '.' or filename[-1] == '.') :
            return False

    return True     
'_______________________________________________________________'

def _to_standard_command_format(commands : str|list) -> list:
    if type(commands) == list:
        return [command.strip('$') for command in commands]
    else:
        if commands[0] != '$' or commands[-1] != '$':
            return list('!' + commands + '!')
        return list(filter(None,commands.split('$')))
'_______________________________________________________________'

def _get_file_type(filename : str) -> str:
    
    file_extension = filename.split('.')[1]

    # if (file_extension not in PIC_EXTENSIONS) and (file_extension not in TEXT_EXTENSIONS):
    #    return None
    
    # else:
    #     return file_extension
    
    if file_extension in PIC_EXTENSIONS:
        return 'pic'
    elif file_extension in TEXT_EXTENSIONS:
        return 'text'
    else:
        return None
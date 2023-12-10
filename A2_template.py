#-------------------------
# Network Programming and Applications
# First Semester (2023-2024)
# Assignment 2
#-------------------------

#-------------------------
# Student Name: 
# Student ID  : 
#-------------------------

# put your import statements between these two lines
#----------------------------------

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
    # your code here
    return 'None'

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

def receive_commands(filename,connection):
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
    # your code here
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
    # your code here
    return None    

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

def get_file_parameters(filename):
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
    # your code here
    return None

'_______________________________________________________________'

def close_socket(filename,sock,sock_type='client'):
    """
    ----------------------------------------------------
    Parameters:   filename (str)
                  sock (socket object)
                  sock_type (str): 'client' or 'server'
    Return:       True or False
    Used by:      Client and Server
    Description:  if invalid type: take no action and return False
                  if socket is closed: take no action and return False
                  if listening server socket: close
                  if connected client socket: shutdown then close
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
    # your code here
    return None

'_______________________________________________________________'

def valid_commands_format(commands):
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
    # your code here
    return None

'_______________________________________________________________'

def get_parameter_value(commands,parameter):
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
    # your code here
    return None

'_______________________________________________________________'

def stp_client(out_filename,server,filename=None,commands=None):
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
    # your code here
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

def send_commands(filename,sock,commands):
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
    # your code here
    return None

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


def valid_filename(filename):
    """
    ----------------------------------------------------
    Parameters:   filename (str)
    Return:       True/False
    Description:  Checks if given input is a valid filename 
                  a filename should have at least 3 characters
                  and contains a single dot that is not the first or last character
    ---------------------------------------------------
    """
    if type(filename) != str:
        return False
    if len(filename) < 3:
        return False
    if '.' not in filename:
        return False
    if filename[0] == '.' or filename[-1] == '.':
        return False
    if filename.count('.') != 1:
        return False
    return True
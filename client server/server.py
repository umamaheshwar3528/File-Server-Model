import os #import os for the python modules
from socketserver import ThreadingMixIn
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

from src.server import config

#https://docs.python.org/3/library/socketserver.html#socketserver.ThreadingMixIn
class MultiThreadedSimpleXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass

def UPLOAD(file_name: str, file_data) -> None: #performing upload operation
    filepath = os.path.join(config.server_data_directory, file_name) # path for uploading the file
    with open(filepath, 'wb') as file:
        file.write(file_data.data)  #writing the file in to the data folder of server
    return

def DOWNLOAD(file_name: str): # performing download operation
    filepath = os.path.join(config.server_data_directory, file_name) #path where to download the file
    with open(filepath, 'rb') as file:
        return xmlrpc.client.Binary(file.read()) #reading the file

def RENAME(curr_name: str, new_name: str) -> None: #performing the rename options
    curr_filepath = os.path.join(config.server_data_directory, curr_name) # curent path from where we need to select file for renaming
    new_filepath = os.path.join(config.server_data_directory, new_name)  #new path for the renamed file
    os.rename(curr_filepath, new_filepath) #renaming the file paths
    return

def DELETE(file_name: str) -> None: #performing the delete operation
    filepath = os.path.join(config.server_data_directory, file_name) # path for deleting the file
    os.remove(filepath) #calling the remove function to  delete the file
    print(f"successfully deleted the file {filepath}") #printing the succesfully deleted file
    return

def start_file_server(): # we are starting the file server using multithreading
    with MultiThreadedSimpleXMLRPCServer(('localhost', config.port), allow_none= True) as server:
        server.register_introspection_functions()
        
        server.register_function(UPLOAD) #registering the upload function 
        server.register_function(DOWNLOAD) #registering the download function 
        server.register_function(RENAME) #registering the rename function 
        server.register_function(DELETE)#registering the delete function 
        
         
        print(f"server is serving on port {config.port}") # printing whether server is serving the port (or) not.
        server.serve_forever() #server serving the port until it is connected
    return



    

import os #import os for the python modules
import time #import time
import xmlrpc.client #import client 
from src.client import config #import config from the client

proxy = xmlrpc.client.ServerProxy(config.server_uri)  # creating a proxy request to client and server for the communication

def file_present(filename): # checking whether the file is present in the client (or) not
    return os.path.isfile(os.path.join(config.data_directory_client, filename)) #returing the file path 

def upload_file(filename): # uploading the files function
    try:
        with open(os.path.join(config.data_directory_client, filename), 'rb') as file:#file path for getting the files
            proxy.UPLOAD(filename, xmlrpc.client.Binary(file.read()))#performing the upload function
            print(f"after uploading file {filename}") # printing uploaded function name
    except:
        print(f"uploading failed for {filename}") #printing if there is any exception is created (or) not
    return

def get_files(): # getting the files  from the directory
    files = [file for file in os.listdir(config.data_directory_client) if (file_present(file) and file != '__init__.py')]# getting all the files
    return files#returing the files

def time_file_change_update(files, mod_file_time):# getting the files after modifying
   
    for file in files: # loop for checking the files
        filepath = os.path.join(config.data_directory_client, file) #path for getting the files
        mod_file_time[file] = os.path.getmtime(filepath) # path after modifying the files
    return

def get_mod_file(files, mod_file_time, time_file_last):  #getting the modified files
    mod_files= []
    for file in files:#loop for checking the modified files
        if(mod_file_time[file] >= time_file_last): # last updated files
             mod_files.append(file)#appending the files
    return  mod_files # returing the modiied files

def get_del_file(files, mod_file_time):#deleting the files
    del_files = []
    for file in mod_file_time: # checking the for the modified files
        if file not in files:
            del_files.append(file)#getting the files after deleting the files
    return del_files# returning the deleting the files

def upload_file_mod(files): # uploading the modified files
    for file in files: # loop for checking the files
        upload_file(file) # uploading the files 
    return

def delete_server_files(files, mod_file_time): # deleting the files in the server also
    for file in files: #checking the all the files
       try:
        proxy.DELETE(file) #calling the delete function in client
        del mod_file_time[file]  #deleting the files
       except:
        print(f"deleting failed for {file}") #printing the if there any exception
    return

def files_checking(time_file_last, mod_file_time):  # checking the for the last updated and modified files

    files = get_files() # checking the files
    print(files)

    time_file_change_update(files, mod_file_time) #updating the file modified times
    

    mod_files = get_mod_file(files, mod_file_time, time_file_last) #modified files
    
    upload_file_mod(mod_files) #uploading the modified files

    del_files = get_del_file(files, mod_file_time) # getting the deleted files 
   
    delete_server_files(del_files, mod_file_time)  # deleting the files in server    
    return

def copy_files_from_client(): # copying the files from client to servers
    files = get_files() #getting all the files
    upload_file_mod(files) # uploading the modified files
    return

def client_start(): #starting the client_file_inspector when we are running the server to copy files from client to server.
    
    copy_files_from_client() #copying all the files to the server
    mod_file_time = {} # getting the file modified times
    time_file_last = time.time()  #checking the last checked timings
    while True: 
        print('started the file inspector') # stating the inspector
        check_start = time.time() #checking the start time
        print(time_file_last, check_start) #printing the last_checked and checked time
        files_checking(time_file_last, mod_file_time)  #checking if there any modifications in the last_checked and checked time
        time_file_last = check_start  # making the time_file_last as check_start time 
        print(time_file_last, check_start) #printing the time_file_last and start_time
        del check_start #deleting the  check_start time
        time.sleep(config.file_check_interval)
    return

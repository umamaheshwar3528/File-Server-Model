import os #import os
import src.server.data as data #import data

server_data_directory = os.path.abspath(data.__file__) #path for server
server_data_directory = os.path.dirname(server_data_directory) #server data directory path
port = 8023 #port for the server
print(f"server is storing the files in {server_data_directory}") #server storing files in the file directory
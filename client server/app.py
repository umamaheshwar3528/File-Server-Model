import threading #import threding for the threads
from src.server.server import start_file_server #starting the server file
from src.client.client import client_start #starting teh client file

if __name__ == "__main__":
    try:
        #server.serve_forever()
        thread_one = threading.Thread(target=start_file_server)#creating a first thread forsynchronous
        thread_one.start()#starting the first thraed
        print('server is running')#checking whether the server is running (or) not 
        thread_two = threading.Thread(target=client_start) #creating second thread for asynchronous
        thread_two.start()# starting second thread
        print('file inspector is running') #checking whether the connection is establised between client and server(or) not
    except:
        print('exiting') #exit 

    
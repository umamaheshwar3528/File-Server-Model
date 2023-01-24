import threading #import threading for the synchronous and asynchronous threads
from src.client import client #import client
from src.server.server import syn_comp_server, asyn_comp_server #import servers
from src.client import client #import client
import time #import time 
import sqlite3 #import sqlite3


if __name__ == "__main__":
    try:        
        #server.serve_forever()
        thread_one = threading.Thread(target=syn_comp_server)  #this thread to start the synchronus server
        thread_one.start()                                       #start thread 1
        print('synchronous server is running')                        #command to print the synchronous server running
        thread_two = threading.Thread(target=asyn_comp_server) #this thread to start the asynchrous server
        thread_two.start()                                       #start thread2
        print('asynchronous server is running')                       #command to print the asynchronous server running                   

       
        print('testing servers') #server testing is the next step 
        print(f"synchronous addition 1,8: {client.syn_add(1,8)}")  #sychronous addition for i and j
        print(f"synchronous sorting [10, 2, 6, 21, 13]: {client.syn_sort([10, 2, 6, 21, 13])}") #synchronous sorting 
        print(f"asynchronous addition 1,8: {client.asyn_add(1,8)}") #asynchronous addition for i and j
        db_con = sqlite3.connect('computation.db') #the database 
        cur_con = db_con.cursor()                      #connection for the db
       # cur.execute(f"INSERT INTO added_data VALUES ('{1}', '{8}', '{9}')")
        added_data=cur_con.execute("select * from added_data WHERE result=(SELECT max(result) FROM added_data)") 
        print("Async Sum:", added_data.fetchone()) 
        db_con.commit() #commit connection
        cur_con.close() #close cursor
        db_con.close() #close connection 


        print(f"asynchronous sorting [9, 7, 2, 6, 13]: {client.asyn_sort([9, 7, 2, 6, 13])}") #asynchronous sorting 
       


        #check if data got stored into table
        db_con = sqlite3.connect('computation.db') #the database 
        cur_con = db_con.cursor()                      #connection for the db
        data_added = cur_con.execute("SELECT * FROM data_added")  #selecting the data from the table
        print(data_added.fetchone())                          #fetching all the data
        sorted_data = cur_con.execute("SELECT * FROM sorted_data WHERE result=(SELECT max(result) FROM sorted_data)") #select fro  the sorted data 
        print(sorted_data.fetchone())                          #fetching all the sorted data
        db_con.commit() #commit connection
        cur_con.close() #close cursor
        db_con.close() #close connection
    except Exception as e: #if there is any error
        print('exiting')
        print(e)           #print error

    

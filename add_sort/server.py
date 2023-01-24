#import os
from socketserver import ThreadingMixIn
from xmlrpc.server import SimpleXMLRPCServer#, SimpleXMLRPCRequestHandler
import time #import time 
import threading #import threading for the threads
import sqlite3 #import sqlit3 database
import json #import json  for the files 

db_con = sqlite3.connect('computation.db') #connection to the db
cur_con = db_con.cursor() #connection to the cursor #create table for data_added with  i,j and  result text
cur_con.execute('''CREATE TABLE IF NOT EXISTS data_added 
               (i text, j text, result text)''')
cur_con.execute('''CREATE TABLE IF NOT EXISTS data_sorted
               (array text, result text)''')
db_con.commit() #create table for sorted_data with  i,j and  result text
cur_con.close()  #close the cursor
db_con.close()   #close the connection

from src.server import config #import config form the server

#https://docs.python.org/3/library/socketserver.html#socketserver.ThreadingMixIn
class MultiThreadedSimpleXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):  #remote procudure call for the server
    pass

def add(i, j): #addition of i,j 
    return i+j #returns the result of addition

def asyn_add_implementation(i, j): #asynchronous addition  of given i,j
    time.sleep(1) #time
    sum = i+j #addition of i and j from given values
    db_con = sqlite3.connect('computation.db')  #connection to the db
    cur_con = db_con.cursor() #connenction to the cursor
    cur_con.execute(f"INSERT INTO added_data VALUES ('{i}', '{j}', '{sum}')") #insert these values into the table
    db_con.commit() #commit connection
    cur_con.close()   #close the cursor
    db_con.close()   #close the connection
    return 

def sort(A):#sorting of the array from app.py
    A.sort() #returns the sorted array
    return A

def asyn_sort(A):#asynchronous sorting   of given array function
    first_thread  = threading.Thread(target=asyn_sort_implementation, args=(A,)) #asynchronous sorting
    first_thread.start() #to start the thread
    return

def asynchronous_adddition(i, j): #asynchronous addition  of given i,j function
    first_thread  = threading.Thread(target=asyn_add_implementation, args=(i,j)) #asynchrous addition with i and j
    first_thread.start() #start the thread
    return 

def asyn_sort_implementation(A):  #asynchronous sorting   of given array function
    original = json.loads(json.dumps(A)) #json for the array
    time.sleep(1) #await sleep
    A.sort() #sort the array function call 
    db_con = sqlite3.connect('computation.db') #connection to the db
    cur_con = db_con.cursor() #connection for the cursor
    cur_con.execute(f"INSERT INTO sorted_data VALUES ('{json.dumps(original)}', '{json.dumps(A)}')")
    db_con.commit()#commit connection
    cur_con.close()  #close the cursor
    db_con.close()#close the connection
    return

def syn_comp_server(): #synchronous server function 
    with MultiThreadedSimpleXMLRPCServer( 
        ('localhost', config.synchronous_port),
        #requestHandler = RequestHandler,
        allow_none= True
        ) as server:#xmlrpc server request handler 
        server.register_introspection_functions()  #server register functions
        server.register_function(add)#server register function for adding
        server.register_function(sort)  #server register function for sorting
        print(f"sync server is serving on port {config.synchronous_port}") #synchronnous server serving on the port 
        server.serve_forever()
    return

def asyn_comp_server():    #aysnchrnous server function 
    with MultiThreadedSimpleXMLRPCServer(
        ('localhost', config.asynchronous_port),
        #requestHandler = RequestHandler,
        allow_none= True
        ) as server:   #xmlrpc server request handler 
        server.register_introspection_functions()#server register functions
        server.register_function(asynchronous_adddition, 'add')#server register function for adding
        server.register_function(asyn_sort, 'sort') #server register function for sorting
        print(f"asynchronous server is serving on port {config.asynchronous_port}")#asynchronnous server serving on the port 
        server.serve_forever() #server function
    return

def start_deferred_server():
    return



    

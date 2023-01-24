import os #import os
import time #import time
import xmlrpc.client #import xmlrpc for client
from src.client import config #import config

syn_proxy = xmlrpc.client.ServerProxy(config.sync_server_uri)  #synchronous proxy between client client and server 
asyn_proxy = xmlrpc.client.ServerProxy(config.async_server_uri) #asynchronous proxy between client client and server 

def syn_sort(A):     #this is the synchronous sorting without aknowledgement
    return syn_proxy.sort(A) #sorting

def syn_add(i, j):      #this is synchrous addition without aknowledgement
    return syn_proxy.add(i,j) #addition of i,j from add function

def asyn_sort(A):  #this is the asynchronous sorting waits for the aknowledgement
    return asyn_proxy.sort(A) # #sorting
 
def asyn_add(i, j):   #this is asynchrous addition waits for the  aknowledgement   
    return asyn_proxy.add(i,j) #addition of i,j from add function


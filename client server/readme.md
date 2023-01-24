Operations such as Uploading, Deleting, Downloading and Renaming the files are
being done in client and server by using multithreading.
● Implemented communication between client and the server by connecting them using
multi-threaded connection.
● Separate data folders are present for both client and server folders
we have to make file transfer between client and server.Transparent and also should be automatically taken care of by the helper thread.Which is exactly what we have done.
In the client_server folder there is a helper thread which is making all the transfers of the files from client to server and also making sure that all the changes are being reflected on the server.
The changes mentioned before can be deleting,renaming or uploading a file to the client or from the client.

How to Run:
● Open the command prompt for client_server and run the command python app.py 
● Simultaneously in another command prompt run python test_server.py
● After the execution of first and second commands we will be able to see all the operations that are being performed.

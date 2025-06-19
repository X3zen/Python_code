import socket

print ("socket in esecuzione\n")

SRV_ADDR = input("inserire l'indirizzo IP del target: ")		#inserire ip bersaglio
SRV_PORT = 4444
									#AF_INET specifica l'utilizzo IPv4 // SOCK_STREAM specifica l'utilizzo di una connessione TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)			#s=socket.socket restituisce comevalore un nuovo socket che abbiamo chiamato 's'
s.bind((SRV_ADDR, SRV_PORT))						#s.bind è il binding, ovvero il collegamento all'IP e alla porta che abbiamo specificato 
s.listen(1)								#s.listen configura il socket sulla coppia IP:PORTA che abbiamo indicato; (1) indica in numero massimo di connessioni in coda
print("Server started! Waiting for connection...")
connection, address = s.accept()					#accept restituisce: 1. connection: l'identificativo che verra utilizzato per scambiare i dati; 2. address: l'IP del client che si collegherà
print('client connected with address', address)
while 1:								#ciclo while sempre vero (1). connection.recv riceve i dati per poi essere decodificati dopo nel formato utf-8
	data = connection.recv(1024)					#1024 è la grandezza del buffer in byte
	if not data: break
	#connection.sendall(b'-- Message Received --\n')		#è un comando per inviare a tutti i partecipanti un messaggio a schermo
	print(data.decode('utf-8'))
connection.close() 							#connection.close termina la connessione

import socket, platform, os

SRV_ADDR = input("Inserire l'indirizzo IP del target: ")			#inserire ip
SRV_PORT = int(input("Inserire la porta del target: "))				#la porta di riferimento

s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)				#AF_INET e SOCK_STREAM specificano che vogliamo utilizzare IPv4 e protocolli TCP
s.bind((SRV_ADDRESS, SRV_PORT))							#qui bindiamo IP:PORTA e socket
s.listen(1)									#ci mettiamo in ascolto ad attendere le connessioni in entrata
connection, address = s.accept()						#s.accept serve per accettare le connessioni in entrata e recuperare info sul client

print("client connected: ", address)

while 1:									#se il client invia '1', il server restituisce info circa OS sul quale è in esecuzione e versione
	try:
		data = connection.recv(1024)
		print (data)
	except:continue
	a= data.decode('utf-8')
	stringa= a.split(sep="\n")
	#print (stringa)
	if(stringa[0] == '1'):
		tosend = platform.platform() + "" + platform.machine()		#platform.platform/machine sono le funzioni che ci danno le info
		connection.sendall(tosend.encode())
	elif(stringa [0] == '2'):						#se il client restituisce '2', il server esegue il comando os.listdir che restituisce la lista dei file presenti in una determinata directory
		data = connection.recv(1024)
		try:
			filelist = os.listdir(data.decode('utf-8'))
			tosend = ""
			for x in filelist:
				tosend += "," + x
		except:
			tosend = "wrong path"
		connection.sendall(tosend.encode())
	elif(stringa [0] == '0'):						#se il client invia '0' il server chiude la connessione
		connection.close()
		connection, address = s.accept
	else:
		print ("Errore!")

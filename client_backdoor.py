import socket

SRV_ADDR = input("Inserire l'indirizzo IP del server: ")
SRV_PORT = int(input("inserire la porta del server: "))

def print_menu():
	print("""\n\n0) chiudere la connessione
1. Informazioni del sistema
2. lista del contenuto delle directory""")

my_sock = socket.socket(socket.AF_INET, socekt.SOCK_STREAM)
my_sock.connect((SRV_ADDR, SRV_PORT))

print ("connessione stabilita")
print_menu()

while 1:
	message = input("\n-seleziona un opzione: ")
	
	if(message == "0"):
		my_sock.sendall(message.encode())
		my_sock.close()
		break
		
	elif(message == "1"):
		my_sock.sendall(message.encode())
		data = my_sock.recv(1024)
		if not data:break
		print(data.decode('utf-8')
		
	elif(message == "2"):
		path = input("inserire il percorso: ")
		my_sock.sendall(message.encode())
		my_sock.sendall(path.encode())
		data = my_sock.recv(1024)
		data = data.decode('utf-8').split(",")
		print("*"*40)
		for x in data:
			print(x)
		print("*"*40)

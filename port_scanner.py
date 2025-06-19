import socket

target = input('enter the IP address to scan: ')				#inserire IP target
portrange = input('Enter the port range to scan (es 5-200): ')			#inserire range delle porte da scansionare

lowport = int(portrange.split('-')[0])						#stringhe con metodo split e il - come separatore
highport = int(portrange.split('-')[1])

print('scanning host ', target, 'from port',lowport, 'to port', highport)

for port in range (lowport, highport):						#tentato connessione in TCP a ogni porta e restituzione di un socket chiamato 's'
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	status = s.connect_ex((target, port))					#s.connect_ex tenta la connessione alla coppia IP:PORTA e ci restituisce 0 / diveso da 0
	if(status == 0):							#se 0 la connessione è andata a buon fine e quindi la porta è aperta
		print('*** port', port, '- OPEN ***')
	else:									#qualunque altro risultato a 0 vuol dire che la connessione non è andata a buon fine, dunque la porta è chiusa
		print('port', port, '- CLOSED')
	s.close()

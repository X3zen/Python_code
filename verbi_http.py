import http.client

host = input("inserire host/IP del sistema target: ")			#host/IP target
port = input("inserire la porta del sistema target (default:80): ")	#selezione porta, se vuota prende quella di default 80

if (port == ""):
	port = 80

try:
	connection = http.client.HTTPConnection(host, port)		#http.client.HTTPConnection prende in input i parametri host e portas inseriti e ci restituisce l'oggetto in connection
	connection.request('OPTIONS', '/')				#il request invia una richiesta http specificando verbo e path. in questo caso usiamo option (verbo) e / come path
	response = connection.getresponse()				#la risposta del server viene salvata nella variabile response
	print("I metodi abilitati sono:",response.status)		#tranite il metodo status si scriomo i verbi http abilitati in base alla risposta del server
	connection.close()
except ConnectionRefuseError:
	print("Connessione fallita")

import socket

HOST="127.0.0.1"
PORT=65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
  s.connect((HOST,PORT))
  print(f"Connesso a ('{HOST}', {PORT})")
  while True:
    messaggio=input("Inserisci i dati da inviare: ")
    s.sendall(messaggio.encode("UTF-8"))
    data=s.recv(1024)
    print("Ricevuto dal server: ")
    print(data.decode())
    print()
    if data.decode()=="KO":
      print("Sessione terminata")
      break
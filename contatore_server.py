# server.py
import socket
import json

HOST = '127.0.0.1'
PORT=65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
  s.bind((HOST,PORT))
  s.listen()
  print(f"Server in ascolto su ('{HOST}', {PORT})")
  clientsocket, address=s.accept()
  progressivo=1
  with clientsocket as cs:
    print("Connection received from ",address)
    while True:
      data=cs.recv(1024)
      # if len(data)==0:
      if not data:
        break
      data=data.decode()
      print(f"Ricevuto '{data}' dal client")
      if data=="KO":
        ris="KO"
      else:
        ris=f"Ciao, {address}. Ho ricevuto questo da te: '{progressivo}) {data}'"
      progressivo+=1
      cs.sendall(ris.encode("UTF-8"))
      if data=="KO":
        break
import socket
import os

from socket import *

HOST = '0.0.0.0'
PORT = 5020
FOLDER = "transferencias"

def connect():
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        print("escutando...")
        s.listen(5)
        return s
    except socket.error as error:
        print(error)

def receiveFile(conn):
    header = b""
    while not header.endswith(b"\n"):
        data = conn.recv(1024)
        if not data:
            return None
        header += data

    nome, tamanho = header.decode().strip().split("|")
    tamanho = int(tamanho)

    print(f"Arquivo: {nome}")
    print(f"Tamanho: {tamanho} bytes")

    return nome, tamanho

def writeFile(conn):
    result = receiveFile(conn)
    if result is None:
        return False

    nome, tamanho = result
    nome = os.path.basename(nome)

    os.makedirs(FOLDER, exist_ok=True)

    caminho = os.path.join(FOLDER, nome)
    recebidos = 0

    with open(caminho, 'wb') as file:
        while recebidos < tamanho:
            chunk = conn.recv(min(4096, tamanho - recebidos))
            if not chunk:
                return False

            file.write(chunk)
            recebidos += len(chunk)

    print(f"{nome} recebido!\n")

    conn.sendall(b"OK")
    return True

if __name__ == "__main__":
    server = connect()
    while True:
        conn, addr = server.accept()
        print("Conectado por:", addr[0])

        with conn:
            while True:
                if not writeFile(conn):
                    break
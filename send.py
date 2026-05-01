import socket
import os
from socket import *

HOST = 'localhost'
PORT = 5020

def parse_args():
    import argparse

    parser = argparse.ArgumentParser(description="Enviar arquivos")
    parser.add_argument("file", nargs="+", help="Arquivos para enviar")

    return parser.parse_args()

def connection():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))
    return s


def sendFile(sock, filepath):
    tamanho = os.path.getsize(filepath)
    nome = os.path.basename(filepath)

    header = f"{nome}|{tamanho}\n".encode()
    sock.sendall(header)
    medidor = tamanho / (1024 * 1024) #MB
    if medidor > 1000:
        nomeMedidor = f'{(medidor / 1024):.2f} GB'
    else:
        nomeMedidor = f'{medidor:.2f} MB'
    print(f"Enviando: {nome} ({nomeMedidor})")

    enviados = 0

    with open(filepath, 'rb') as file:
        while chunk := file.read(512):
            sock.sendall(chunk)
            enviados += len(chunk)
            percent = (enviados / tamanho) * 100
            print(f"\r{percent:.2f}% enviados!", end="")

    if sock.recv(2).decode() == "OK":
        print(" [ OK ]")
        print(f"{nome} foi entregue!")
    else:
        print(f"\n{nome} não foi entregue!")

if __name__ == '__main__':
    arg = parse_args()

    sock = connection()

    for arquivo in arg.file:
        if not os.path.exists(arquivo):
            print("=======================")
            print(f'{arquivo} não foi encontrado!')
            continue

        print("=======================")
        sendFile(sock, arquivo)
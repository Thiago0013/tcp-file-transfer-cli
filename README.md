# TCP File Transfer System (Custom Protocol)

## Description
Sistema de transferência de arquivos via TCP com protocolo próprio (header + size + ACK), desenvolvido em Python.

---

## Features
- Envio de múltiplos arquivos via terminal
- Progresso em tempo real do envio
- Confirmação de recebimento (ACK do servidor)
- Interface de linha de comando (CLI com argparse)

---

## Usage

### Enviar um arquivo:
```bash
python3 send.py arquivo.txt
Enviar múltiplos arquivos:
python3 send.py arquivo1.txt arquivo2.txt arquivo3.txt
Configuration
O endereço IP do servidor deve ser configurado no cliente (send.py)
O servidor (receive.py) deve ser executado na máquina que irá receber os arquivos
Ambos os dispositivos devem estar na mesma rede local (ou acessíveis via IP)
Architecture
Client → HEADER → DATA → Server → ACK (OK)
Protocol

Cada arquivo é enviado no seguinte formato:

nome_do_arquivo|tamanho_em_bytes\n
[dados binários]

O servidor responde:

OK

quando o arquivo é recebido com sucesso.


---

# 🔹 💡 O que eu corrigi 

### ✔️ 1. Erro de digitação
```text
istem a de transferência
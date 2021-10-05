import random
import socket
import string

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
sock.connect(server_address)

info_human = []
try:
    for i in range(5):
        bbbb = f'{random.randint(1000, 9999)}'
        nn = f'{random.choice(string.digits)}'
        hh = f'{random.randint(00, 3)}'
        mm = f'{random.randint(00, 60)}'
        ss = f'{random.randint(00,60)}'
        zz = f'{random.randint(1,9)}'
        gg = f'{random.randint(1, 20)}'
        message = f'{bbbb} {nn} {hh}:{mm}:{ss}.{zz} {gg}\n'
        sock.sendall(message.encode())
        print(message)

finally:
    sock.close()

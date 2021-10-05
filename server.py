import logging
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
sock.bind(server_address)
sock.listen(100)

response = ''
logging.basicConfig(filename="sample.log", level=logging.INFO)
logger = logging.getLogger("server")
logger.setLevel(logging.INFO)

strings_sports = []
while True:
    connection, client_address = sock.accept()
    try:
        while data := connection.recv(4096).decode('utf-8'):
            zap = f'{response}{data}'.split('\n')
            for i in zap:
                i = i.split(' ')
                print(f'Спортсмен {i[0]}, id {i[1]}, время {i[2]}, группа {i[3]}')
            logging.info()

    except Exception:
        connection.close()
        logging.info('ValueError. Connection close.')

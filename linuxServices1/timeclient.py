import socket

# Вводим IP адреса сервера от пользователя
server_ip = input("Enter the IP address of the server: ")

# Создаем сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаемся к серверу
client_socket.connect((server_ip, 1303))

# Получаем данные от сервера (до 1024 байтов)
data = client_socket.recv(1024)

# Выводим данные на экран
print("The server returned:", data.decode())

# Закрываем соединение с сервером
client_socket.close()
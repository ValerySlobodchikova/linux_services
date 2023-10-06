import socket
import datetime

# Создаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокет к адресу и порту
server_socket.bind(("0.0.0.0", 1303))

# Начинаем слушать сокет, максимальное количество соединений в очереди - 5
server_socket.listen(5)

print("The server is launched and listens to the port 1303...")

try:
    while True:
        # Принимаем подключение
        client_socket, client_address = server_socket.accept()
        print("Connecting from ", client_address)

        # Получаем текущую дату и время
        current_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")

        # Отправляем данные клиенту
        client_socket.send(current_time.encode())

        # Закрываем соединение с клиентом
        client_socket.close()
except KeyboardInterrupt:
    print("Server is stopped")
finally:
    server_socket.close()
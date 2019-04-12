import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

addr_to = ("127.0.0.1", 60000)

buffersize = 1024

# while True:
#     time.sleep(1)
#     client.sendto("hello".encode("utf8"), addr_to)
client.sendto("hello1".encode("utf8"), addr_to)

while True:
    info, addr = client.recvfrom(buffersize)
    print(info, addr)




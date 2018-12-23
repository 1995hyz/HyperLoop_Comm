import socket


def main():
    ip = '192.168.0.100'
    port = 12345
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    print(s.sendto('This is a test for HyperLoop Pod'.encode(encoding='utf-8'), (ip, port)))
    print(s.sendto('0x05504F3AD3D53401E50550'.encode(encoding='utf-8'), (ip, port)))
    print(s.sendto('Transmission End. Have a good day'.encode(encoding='utf-8'), (ip, port)))


if __name__ == '__main__':
    main()

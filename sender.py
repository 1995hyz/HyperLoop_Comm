import socket


def main():
    ip = '127.0.0.1'
    port = 12345
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    print(s.sendto(b'\x00\x01\x00\x00\x23\x11\x00\x00\x05\x21\x00\x00\x00\xaa\xff\x00\x11\x01\x00\x00\x00\x05\x00\x00\x00\x15\x00\x00\x00\x12', (ip, port)))
    print(s.sendto(b'\x00\x01\x00\x00\x23\x11\x00\x00\x05\x21\x00\x00\x00\xaa\xff\x00\x11\x01\x00\x00\x00\x05\x00\x00\x00\x15\x00\x00\x00\x12', (ip, port)))
    print(s.sendto(b'\x00\x02\x00\x00\x23\x11\x00\x00\x05\x21\x00\x00\x00\xaa\xff\x00\x11\x01\x00\x00\x00\x05\x00\x00\x00\x15\x00\x00\x00\x12', (ip, port)))
    # print(s.sendto('This is a test for HyperLoop Pod'.encode(encoding='utf-8'), (ip, port)))
    # print(s.sendto('0x05504F3AD3D53401E50550'.encode(encoding='utf-8'), (ip, port)))
    # print(s.sendto('Transmission End. Have a good day'.encode(encoding='utf-8'), (ip, port)))


if __name__ == '__main__':
    main()

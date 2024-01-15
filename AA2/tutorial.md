Debug the Code
======================
In this activity, you will debug the code to perform the DDoS attack.




<img src= "https://s3-whjr-curriculum-uploads.whjr.online/f50b92bd-501c-43cb-9398-fc0407a391e7.gif" width = "100%" height = "50%">




Follow the given steps to complete this activity.




1. Debug the code.
* Open the file main.py.
* Debug the below code to fix the bug.
```
if worker is not None and worker.is_alive():
    worker.join(1.0)
    print(f"Woker Number - {worker.name} Joined!")
else:
    workers.remove(worker)
```
* Run the except block only when keyboard  interruption and system exit occurs.


```
def isEncrypted(filePath, key):
  with open(filePath, 'rb') as file:
    firstLine = file.readline()
    try:
      Fernet(key).decrypt(firstLine)
      return True
    except Exception as e:
      return False
```


* Save and run the code to check the output.

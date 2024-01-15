Download, Install, and Setup the Virtual Machine
======================
In this activity, you will install the Kali Linux, download, and set up the virtual machine on our computers.




<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10944475/pasted-from-clipboard.png" width = "auto" height = "auto">




Follow the given steps to complete this activity.




1. Download, install and setup the Kali Linux
* Download the Kali Linux 2023.3 Changelog version using using the link: `https://www.kali.org/get-kali/#kali-installer-images`.
<img src= "https://s3-whjr-curriculum-uploads.whjr.online/b6acc35a-6bd2-4e2c-9cdd-3d17ba99febc.png" width = "auto" height = "auto">
* Run the downloaded version.
<img src= "https://s3-whjr-curriculum-uploads.whjr.online/6efc11f0-0000-4699-a64f-83eb88cd7ba9.png" width = "auto" height = "auto">
* Click on the `Open` button.
<img src= "https://s3-whjr-curriculum-uploads.whjr.online/392ae467-003f-429c-8cb2-973ae6502739.png" width = "auto" height = "auto">
* Click on the `README` file.
<img src= "https://s3-whjr-curriculum-uploads.whjr.online/c252e8d7-bb5a-4a8e-9826-2319af84c02e.png" width = "auto" height = "auto">
* Double click on the `vmlinuz` file.
<img src= "https://s3-whjr-curriculum-uploads.whjr.online/5356a6c1-1b05-47c9-ac99-ac39698671f3.png" width = "auto" height = "auto">
* Download the toy website folder and extract it on the Kali Linux window using Mozilla Firefox.


2. Download, install and setup the Virtual Machine
* Download the virtual amchine using using the link: `https://www.vmware.com/in/products/fusion/fusion-evaluation.html`.




3. Setup the Virtual Machine using the Kali Linux
* Open the command prompt window on the Kali Linux.
* Install requirements.txt file or requirements using the following commands.
```
// Install Python
sudo apt install python3.11-venv 
//Add password for linux which won't be visible while typing
//Press Y
python -m venv myenv
source myenv /bin/activate
clear
//Install flask and its libraries
pip install flask
//run the code
pip install flask_migrate
pip install 'reportlab'
pip install flask_session
```
* Save and run the code to check the output.

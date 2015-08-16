# Fetch and forward Raspberry Pi's public IP via email. 
The purpose of this tool is developing a daemon for fetching Raspberry Pi's (or any other Linux distro's) public IP and sending it to a desired email address at a desired time step. After you finish setting up this script, you will be informed at a defined timestep, or at every system boot if the IP address of your machine has changed.

This script is useful for creating a webserver, using VNC outside a local network or being able to SSH to a dynamic IP host. Knowing the public IP of a dynamic IP host has numerous other useful uses.

### Install

To install the tool, download the [public_ip_hander.py](public_ip_handler.py) file and place it in a suitable folder, e.g. */home/user/*. Then edit the fields: *to*, *gmail_user* and *gmail_password*, to match the email of the recipient and email and password of the sender. 

After you have successfully edited the script, in order to execute it write in terminal (replace */home/user/* with your path to file):
```bash
python /home/user/public_ip_handler.py
```

### Setup
#### Send IP at a defined timestep
Now, to setup the script to be executed at a desired timestep, we shall use the built-in **cron** tool.

To open cron editor, write:
```bash
crontab -e
```
If you want to execute the script each day at 12:00, append the fallowing command to the editor:
```
0 12 * * * python /home/user/public_ip_handler.py
```

For more **crontab** options, you can consult the [official manual](http://crontab.org/) or this [quick reference](http://www.adminschoice.com/crontab-quick-reference).

#### Send IP at system boot
To send your Pi's IP at each system boot, you have to edit the hidden *~/.bashrc* file. The command to that is:
```bash
echo 'python /home/user/public_ip_handler.py' >> ~/.bashrc
```

### Attribution
The [public_ip_hander.py](public_ip_handler.py) is a modification of the [startup_mailer.py](http://elinux.org/RPi_Email_IP_On_Boot_Debian) script under the "Creative Commons Attribution-ShareAlike 3.0 Unported License".

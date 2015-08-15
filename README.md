# Fetch and forward via email Raspberry Pi's public IP. 
The purpose of this tool is developing a daemon for fetching Raspberry Pi's (or any other linux distro) public IP and sending it to a desired email address. After you finish setting up this script, you will informed at a defined timestep if the IP address of your machine has changed.

This script is useful for creating a webserver, VNC or being able to SSH to a dynamic IP host. Knowing the public IP of a dynamic IP host has other useful uses.

### Install

To install the tool, download the [public_ip_hander.py](public_ip_handler.py) file and place it in suitable folder, e.g. */home/user/*. Then edit the fields *to*, *gmail_user* and *gmail_password*.

After that do:
```bash
sudo chmod +x /home/user/public_ip_hander.py
```
The configuration is thus finished.

To execute the script write:
```bash
python /home/user/public_ip_handler.py
```

Now, to setup the script to be executed at a desired timestep, we shall use the built-in cron tool.

To open cron editor, write:
```bash
crontab -e
```
If you want to execute the script each day at 12:00, append the fallowing command to the editor:
```
0 12 * * * python /home/user/public_ip_handler.py
```

# rpi-public-ip
The purpose of this tool is developing a daemon for fetching Raspberry Pi's (or any other linux distro) public IP and sending it to a desired email address. After you finish setting up this script, you will informed at a defined timestep if the IP address of your machine has changed.

This script is useful for creating a webserver, VNC or being able to SSH to a dynamic IP host. Knowing the public IP of a dynamic IP host has other useful uses.


To install the tool, download the "public_ip_hander.py" file and place it in suitable folder, e.g. "/home/user/". Then edit the fields to, gmail_user and gmail_password.

After that do:
sudo chmod +x /home/user/public_ip_hander.py

To execute the script write:
python /home/user/public_ip_handler.py

Now, to setup the script being initialized at a desired timestep, we shall use the builtin cron tool.

To open cron editor, write:
crontab -e
If you want to execute the script each day at 12:00, append to the opened editor:
0 12 * * * python /home/user/public_ip_handler.py

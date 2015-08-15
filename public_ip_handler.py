__author__ = 'Hamza Merzic'
__license__ = 'Creative Commons Attribution-ShareAlike 3.0 Unported License'
__version__ = '1.0'
__maintainer__ = 'Hamza Merzic'

import subprocess
import smtplib
from email.mime.text import MIMEText
import datetime

# Your own account information.
to = 'your.email@gmail.com' # Email to send to.
gmail_user = 'senders.email@gmail.com' # Email to send from. (MUST BE GMAIL)
gmail_password = 'senderspassword' # Gmail password.
smtpserver = smtplib.SMTP('smtp.gmail.com', 587) # Server to use.

smtpserver.ehlo()  # Says 'hello' to the server
smtpserver.starttls()  # Start TLS encryption
smtpserver.ehlo()
smtpserver.login(gmail_user, gmail_password)  # Log in to server
today = datetime.date.today()  # Get current time/date

arg='touch ~/stored_ip; cat ~/stored_ip'
# Runs 'arg' in a 'hidden terminal'.
p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
data = p.communicate()  # Get data from 'p terminal'.

# Store previous ip.
previous_ip = str(data[0])

arg="curl -s checkip.dyndns.org|sed -e 's/.*Current IP Address: //' -e 's/<.*$//\'"  # Linux command to retrieve public ip address.
p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
data = p.communicate() 

# Store current ip.
current_ip = str(data[0])

if previous_ip == current_ip:
	smtpserver.quit()
	exit()

# Creates the text, subject, 'from', and 'to' of the message.
msg = MIMEText("Your public ip is " + current_ip[:-1] + ".")
msg['Subject'] = "RaspberryPi's public IP on %s" % today.strftime('%b %d %Y')
msg['From'] = gmail_user
msg['To'] = to
# Sends the message.
smtpserver.sendmail(gmail_user, [to], msg.as_string())
# Closes the smtp server.
smtpserver.quit()

# Stores the new password.
arg="echo " + current_ip[:-1] + " > ~/stored_ip"
p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)

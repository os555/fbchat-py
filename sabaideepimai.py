# -*- coding: utf-8 -*-
import sys
from fbchat import Client
from fbchat.models import *
user= "FACEBOOK_USER_OR_EMAIL"
pas= "PASSWORD"
client = Client(user,pas)
users = client.fetchAllUsers()
listuser=[user.uid for user in users if user.uid!="0"] # Loop UID
on=""
if on=="exit": # Type exit to exit
    client.logout() # Run Exit command
    sys.exit() #Exit application
for id in listuser: # Loop for all Friends from your facebook
    client.send(Message(text='ສະບາຍດີປີໃຫມ່ເດີ້ ຂໍໃຫ້ແຂງແຮງ ລໍ້າລວຍ ມີຄວາມສຸກ ມີເງິນໃຊ້'), thread_id=id, thread_type=ThreadType.USER) # Send MSG
print("happy new year :D")
client.logout() # Exit

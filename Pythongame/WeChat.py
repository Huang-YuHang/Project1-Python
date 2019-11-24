import itchat
import time
import random
itchat.auto_login()
time.sleep(10)
friends = itchat.get_friends(update=True)

selected_friends = random.sample(friends[1:],10)
for friend in selected_friends:
    username = friend['UserName']
    itchat.send_msg('...',username)
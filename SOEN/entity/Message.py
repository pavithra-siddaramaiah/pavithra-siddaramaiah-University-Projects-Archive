import datetime
from entity.data import *

def broadcastNotification(sender,message):
    for user in users:
        sendPrivateNotification(sender=sender,reciever=user["username"],message=message)

def sendPrivateNotification(sender,reciever,message):
    newNotification = {"sender":sender,"message":message,"timeStamp":datetime.datetime.now()}
    if reciever in notifications.keys():
        notifications[reciever].append({"sender":sender,"message":message,"timeStamp":datetime.datetime.now()})
    else:
        notifications[reciever] = [newNotification]
def showAllNotifications(username):
    for notification in notifications[username]:
        print(notification["message"])
        
def sendComplaint(sender,message):
    for user in users:
        if user["userType"] == ADMIN:
            sendPrivateNotification(sender=sender,reciever=user["username"],message="COMPLAINT:" + message)

from boilerplate.inputs import getIntegerInRange
from entity.User import *
from entity.Message import *
def ownerMainMenu():
    admin = Admin.getAdmin()
    while True:
        choice = getIntegerInRange("1.Add Slot\n2.Show Slots\n3.Send Notitication\n4.Show All Notifications\n5.Exit",1,5)
        if choice == 1:
            addSlotMenu(admin.username)
        elif choice == 2:
            Slot.showAllSlotsByOwner(admin.username)
        elif choice == 3:
            # TODO LEAST PRIORITY
            sendNotification(sender = admin.username)
        elif choice == 4:
            showAllNotifications(admin.username)
        else:
            break

def addSlotMenu(owner):
    while True:
        choice = getIntegerInRange("Choose a service:\n1.Cinema\n2.Restaurant\n3.Hotel\n4.Conference Room\n5.Airplane Slot\n6.Exit",1,6)
        if choice == 1:
            Slot.addSlotBySlotType(owner,CINEMA)
        elif choice == 2:
            Slot.addSlotBySlotType(owner,RESTAURANT)
        elif choice == 3:
            Slot.addSlotBySlotType(owner,HOTEL)
        elif choice == 4:
            Slot.addSlotBySlotType(owner,CONFIERENCE)
        elif choice == 5:
            Slot.addSlotBySlotType(owner,AIRPLANE)
        else:
            break

def sendNotification(sender):
    while True:
        choice = getIntegerInRange("Select one option:\n1.Broadcast Message\n2.Send a priavte message\n3.Exit",1,3)
        if choice == 1:
            message = getString("Please provide the message you want to send")
            broadcastNotification(sender,message=message)
        elif choice == 2:
            reciever = getString("Please provide the message you want to send")
            message = getString("Please provide the message you want to send")
            sendPrivateNotification(sender,reciever,message)
        else:
            break


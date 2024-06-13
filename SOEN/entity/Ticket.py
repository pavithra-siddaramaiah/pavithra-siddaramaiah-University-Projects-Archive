import datetime
from entity.data import *

class Ticket:
    padding = 70
    sectionPadding = padding / 2 - 1

    def __init__(self,customerID, category, slotID, seatID, price) -> None:
        self.customerID = customerID
        self.category = category
        self.slotID = slotID
        self.seatID = seatID
        self.price = price
        self.timeStamp = datetime.datetime.now()

    def show(self):
        print("-"*Ticket.padding)
        print("|{label:<34}|{value:>34}|".format(
            label="Type", value=self.category))
        print("|{label:<34}|{value:>34}|".format(
            label="Room ID", value=self.slotID))
        print("|{label:<34}|{value:>34}|".format(
            label="Seat ID", value=self.seatID))
        print("|{label:<34}|{value:>34}|".format(
            label="Price", value="$ " +str(self.price)))
        print("|{label:<34}|{value:>34}|".format(
            label="TimeStamp", value=self.timeStamp.strftime('%c')))
        print("-"*Ticket.padding)
    

class DiscountTicket:
    def __init__(self, ticket, discount) -> None:
        self.ticket = ticket
        self.discount = discount
    
    def purchaseTicket(self,username):
        category = self.ticket.category 
        slotID = self.ticket.slotID 
        seatID = self.ticket.seatID 
        price = self.ticket.price - self.ticket.price  * self.discount
        slot = categories[category][slotID]
        if slot.getTicketByCustomerID(username) == None:
            slot.cancelTicket(self.ticket.customerID)
            slot.bookTicket(username,seatID,price)
        else:
            print("Customer have already booked a ticket!!!")
    
    def show(self):
        self.ticket.show()


class ExchangeTicket:
    def __init__(self,userA,ticketA,userB,ticketB) -> None:
        self.userA = userA
        self.ticketA = ticketA
        self.userB = userB
        self.ticketB = ticketB
        self.exchangedOperatonPerformed = False
    
    def confirmExchange(self):
        slotType = self.ticketA.category
        slotID = self.ticketA.slotID
        print(slotType)
        print(slotID)
        print(categories[slotType])
        slot = categories[slotType][slotID]
        userNameA = self.ticketA.customerID
        self.ticketA.customerID = self.ticketB.customerID
        self.ticketB.customerID = userNameA
        slot.bookedTickets[self.ticketA.customerID] = self.ticketA
        slot.bookedTickets[self.ticketB.customerID] = self.ticketB
        self.exchangedOperatonPerformed = True

    def showTicketByUser(self,username):
        if username == self.userA:
            self.ticketA.show()
        elif username == self.userB:
            self.ticketB.show()


    def show(self):
        print("Your Ticket")
        self.ticketB.show()
        print("In exchange you will get the following ticket")
        self.ticketA.show()
    
    



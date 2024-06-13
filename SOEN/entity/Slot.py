from entity.Slot import *
from boilerplate.contants import *
from boilerplate.inputs import *
from entity.data import *
from entity.Ticket import *


def getSlotInputFromUser(owner):
    name = getString("Provide slotID")
    n = getInteger("Provide the size of the squared room :")
    price = getInteger("Ptovide the normal price")
    return {"owner": owner, "name": name, "n": n, "price": price}

def showSlotsBySlotType(slotType):
    print("List of available rooms:")
    for slotID in categories[slotType].keys():
        slot = categories[slotType][slotID]
        print(slot.name)

class Slot:
    def __init__(self, name, n, price, owner, slotType) -> None:
        self.owner = owner
        self.name = name
        self.slotType = slotType
        self.firstRow = 0
        self.lastRow = n-1
        self.n = n
        self.seats = [
            ["#" for j in range(n)] for i in range(n)
        ]
        self.bookedTickets = {}
        self.price = price
        self.middleColumn1 = (n // 2) - 1
        self.middleColumn2 = self.middleColumn1 + 1

    def bookTicket(self, userID, seatID,price):
        if userID in self.bookedTickets.keys():
            print("User have already booked one ticket for this slot.")
        else:
            row = (seatID - 1) // self.n
            column = (seatID - 1) - (row * self.n)
            self.seats[row][column] = "-"
            if price == None:
                self.bookedTickets[userID] = Ticket(
                userID, self.slotType, self.name, seatID, self.getSeatSymbol(row, column))
            else:
                self.bookedTickets[userID] = Ticket(
                userID, self.slotType, self.name, seatID, price=price)
            self.bookedTickets[userID].show()

    def getSeatSymbol(self, x, y):
        if x == self.firstRow:
            return 2 * self.price
        elif x == self.lastRow:
            return self.price - self.price * 0.25
        elif y == self.middleColumn1 or y == self.middleColumn2:
            return self.price + self.price * 0.25
        else:
            return self.price

    def show(self):
        print(self.slotType+"::"+self.name, end="\n\n")
        for i in range(self.n):
            for j in range(self.n):
                print("{:>8}${:>5}".format(self.getSeatSymbol(
                    i, j), f"({(i*self.n + j) + 1})" if self.seats[i][j] == "#" else "(Sold)"), end=" ")
            print("\n")

    def addSlotBySlotType(owner,slotType):
        slotInputs = getSlotInputFromUser(owner=owner)
        conference = Slot(name=slotInputs["name"], n=slotInputs["n"],
                          price=slotInputs["price"], owner=slotInputs["owner"], slotType=slotType)
        categories[slotType][slotInputs["name"]] = conference
        showMessage("Slot Added")

    def getSlotByType(slotType, slotID):
        if slotType in categories.keys():
            if slotID in categories[slotType].keys():
                return categories[slotType][slotID]
            else:
                return None
        else:
            return None

    def showAllSlotsByOwner(owner):
        for cat in categories.keys():
            for slotID in categories[cat].keys():
                categories[cat][slotID].show()

    def showTicketByCustomerID(self,customerID):
        if customerID in self.bookedTickets.keys():
            self.bookedTickets[customerID].show()

    def getTicketByCustomerID(self,customerID):
        if customerID in self.bookedTickets.keys():
            return self.bookedTickets[customerID]
        else:
            return None
    def getTicketByTicketID(self,seatID):
        for customerID in self.bookedTickets.keys():
            if self.bookedTickets[customerID].seatID == seatID:
                return self.bookedTickets[customerID]
    
    def cancelTicket(self, customerID):
        oldTicket = self.bookedTickets[customerID]
        row = (oldTicket.seatID - 1) // self.n
        column = (oldTicket.seatID - 1) - (row * self.n)
        self.seats[row][column] = "#"
        del self.bookedTickets[customerID]
        
    def sellTicket(self,ticket,discount):
        category = ticket.category
        slotID = ticket.slotID
        if slotID in sellList[category].keys():
            sellList[category][slotID].append(DiscountTicket(ticket,discount))
        else:
            sellList[category][slotID] = [DiscountTicket(ticket,discount)]
        print("Ticket put into the Sell Ticket List")
    
    def changeTickets(self,oldTicket,newSeatID):
        newRow = (newSeatID - 1) // self.n
        newColumn = (newSeatID - 1) - (newRow * self.n)
        oldRow = (oldTicket.seatID - 1) // self.n
        oldColumn = (oldTicket.seatID - 1) - (oldRow * self.n)
        if self.seats[newRow][newColumn] == "#":
            self.seats[newRow][newColumn] = "$"
            self.seats[oldRow][oldColumn] = "#"
            oldTicket.seatID = newSeatID
            oldTicket.price = self.getSeatSymbol(newRow,newColumn)
            oldTicket.timeStamp = datetime.datetime.now()
            print("Tickets exchanged successfully!!")
            return True
        else:
            print("Provided new seat ID is already sold.")
            return False

    def getCustomerIDByTicketID(self,seatID):
        for userID in self.bookedTickets.keys():
            if self.bookedTickets[userID].seatID == seatID:
                return userID

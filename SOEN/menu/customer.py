from boilerplate.inputs import getIntegerInRange
from entity.User import *
from entity.Message import *


def customerMainMenu():
    customer = User.getUser()
    while True:
        choice = getIntegerInRange(
            "1.Book Slot Ticket\n2.Show Tickets\n3.Send Notitication\n4.Show All Notifications\n5.Register a complaint\n6.Sell Ticket\n7.Change Ticket\n8.Cancel Ticket\n9.Show Sell Ticket List\n10.Exchange Tickets\n11.Show and Confirm Exchange Tickets\n12..Exit", 1, 12)
        if choice == 1:
            bookSlotMenu(customer)
        elif choice == 2:
            showTicketsByCustomerID(customer.username)
        elif choice == 3:
            sendNotification(sender=customer.username)
        elif choice == 4:
            showAllNotifications(customer.username)
        elif choice == 5:
            compalint = getString("Enter the complaint")
            sendComplaint(customer.username, compalint)
        elif choice == 6:
            sellTicketsByCustomer(customer.username)
        elif choice == 7:
            changeTicketByCustomer(customerID=customer.username)
        elif choice == 8:
            cancelTicketsByCustomer(customerID=customer.username)
        elif choice == 9:
            showSellTicketsByCustomer()
        elif choice == 10:
            exchangeTicketByCustomer(customer.username)
        elif choice == 11:
            showAndConfirmExchangeTicket(customer.username)
        else:
            break


def sendNotification(sender):
    while True:
        choice = getIntegerInRange(
            "Select one option:\n1.Broadcast Message\n2.Send a priavte message\n3.Exit", 1, 3)
        if choice == 1:
            message = getString("Please provide the message you want to send")
            broadcastNotification(sender, message=message)
        elif choice == 2:
            reciever = getString("Please provide the message you want to send")
            message = getString("Please provide the message you want to send")
            sendPrivateNotification(sender, reciever, message)
        else:
            break


def bookSlotMenu(customer):
    while True:
        choice = getIntegerInRange(
            "Choose a service:\n1.Cinema\n2.Restaurant\n3.Hotel\n4.Conference Room\n5.Airplane Slot\n6.Exit", 1, 6)
        if choice == 1:
            customer.bookCinemaTickets()
        elif choice == 2:
            customer.bookRestaurantTickets()
        elif choice == 3:
            customer.bookHotelTickets()
        elif choice == 4:
            customer.bookConferenceTickets()
        elif choice == 5:
            customer.bookAirplaneTickets()
        else:
            break

# def cancelBooking(customer):


def showTicketsByCustomerID(customerID):
    for ticketType in categories.keys():
        for slotID in categories[ticketType].keys():
            slot = categories[ticketType][slotID]
            slot.showTicketByCustomerID(customerID)


def sellTicketsByCustomer(customerID):
    tickets = []
    slots = []
    ticketIndex = 0
    for ticketType in categories.keys():
        for slotID in categories[ticketType].keys():
            slot = categories[ticketType][slotID]
            ticket = slot.getTicketByCustomerID(customerID)
            if ticket != None:
                tickets.append(ticket)
                slots.append(slot)
                print("Ticket #" + str(ticketIndex + 1))
                ticket.show()
    choice = getIntegerInRange("Choose a ticket", 1, len(tickets)) - 1
    discount = getInteger("Provide Discount Rate(Integer)")
    selectedTicket = tickets[choice]
    selectedSlot = slots[choice]
    selectedSlot.sellTicket(selectedTicket, discount)


def cancelTicketsByCustomer(customerID):
    tickets = []
    slots = []
    ticketIndex = 0
    for ticketType in categories.keys():
        for slotID in categories[ticketType].keys():
            slot = categories[ticketType][slotID]
            ticket = slot.getTicketByCustomerID(customerID)
            if ticket != None:
                tickets.append(ticket)
                slots.append(slot)
                print("Ticket #" + str(ticketIndex + 1))
                ticket.show()
    choice = getIntegerInRange("Choose a ticket", 1, len(tickets)) - 1
    selectedSlot = slots[choice]
    selectedSlot.cancelTicket(customerID)


def changeTicketByCustomer(customerID):
    tickets = []
    slots = []
    ticketIndex = 0
    for ticketType in categories.keys():
        for slotID in categories[ticketType].keys():
            slot = categories[ticketType][slotID]
            ticket = slot.getTicketByCustomerID(customerID)
            if ticket != None:
                tickets.append(ticket)
                slots.append(slot)
                print("Ticket #" + str(ticketIndex + 1))
                ticket.show()
    choice = getIntegerInRange("Choose a ticket", 1, len(tickets)) - 1
    selectedSlot = slots[choice]
    selectedTicket = tickets[choice]
    # take input for a new seatID
    selectedSlot.show()
    newSeatNumber = getInteger("Provide new seat number:")
    selectedSlot.changeTickets(selectedTicket, newSeatNumber)


def showSellTicketsByCustomer():
    for slotType in sellList.keys():
        for slotID in sellList[slotType].keys():
            for dicountTicket in sellList[slotType][slotID]:
                dicountTicket.show()


def exchangeTicketByCustomer(customer):
    tickets = []
    slots = []
    ticketIndex = 0
    for ticketType in categories.keys():
        for slotID in categories[ticketType].keys():
            slot = categories[ticketType][slotID]
            ticket = slot.getTicketByCustomerID(customer)
            if ticket != None:
                tickets.append(ticket)
                slots.append(slot)
                print("Ticket #" + str(ticketIndex + 1))
                ticket.show()
    if len(tickets) == 0:
        print("You do not have the booked tickets to be exchanged.")
        return
    else:
        choice = getIntegerInRange("Choose a ticket", 1, len(tickets)) - 1
        selectedSlot = slots[choice]
        selectedTicket = tickets[choice]
        selectedSlot.show()
        newSeatNumber = getInteger("Provide new seat number:")

        if selectedSlot.changeTickets(selectedTicket, newSeatNumber) == True:
            print("Tickets has been exchanged successfully!!")
        else:
            exchangeTicket = selectedSlot.getTicketByTicketID(newSeatNumber)
            if exchangeTicket.customerID == customer:
                print("This ticket is already yours!!!")
            else:
                print(
                    "Sending noticition to the ticket holder about exchanging ticket request!!")
                # PUT TICKET INTO EXCHANGE LIST
                if slotID in exchangeTicketList[selectedSlot.slotType].keys():
                    exchangeTicketList[selectedSlot.slotType][slotID].append(ExchangeTicket(
                        customer, selectedTicket, exchangeTicket.customerID, exchangeTicket))
                else:
                    exchangeTicketList[selectedSlot.slotType][slotID] = [ExchangeTicket(
                        customer, selectedTicket, exchangeTicket.customerID, exchangeTicket)]

                # SEND NOTIFIACTION TO TICKET HOLDER
                ticketHolder = selectedSlot.getCustomerIDByTicketID(
                    newSeatNumber)
                sendPrivateNotification(
                    customer, ticketHolder, "You have a ticket to be exchanged!!")


def showAndConfirmExchangeTicket(customer):
    customerExchangeList = []
    index = 0
    for slotType in exchangeTicketList.keys():
        for slotID in exchangeTicketList[slotType]:
            exchangeList = exchangeTicketList[slotType][slotID]
            for exchangeTicket in exchangeList:
                if exchangeTicket.userB == customer and not exchangeTicket.exchangedOperatonPerformed:
                    print(
                        f"--------------------------------------${index + 1}--------------------------------------")
                    customerExchangeList.append(exchangeTicket)
                    exchangeTicket.show()
    if len(customerExchangeList) == 0:
        print("No exchnage tickets are available for now!!!")
    else:
        choice = getIntegerInRange(
            "Select the exchange ticket", 1, len(customerExchangeList)) - 1
        exchangeTicket = customerExchangeList[choice]
        action = getIntegerInRange("1.Exchange\n2.Refuse\n3.Exit", 1, 3)
        if action == 1:
            exchangeTicket.confirmExchange()
        elif action == 2:
            exchangeTicket.exchangedOperatonPerformed = True
        else:
            return

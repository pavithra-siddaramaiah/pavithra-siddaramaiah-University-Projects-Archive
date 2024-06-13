from entity.data import *
from entity.Slot import *
from boilerplate.contants import *
from boilerplate.inputs import *


def getUserByUsername(username):
    for user in users:
        if user["username"] == username:
            return user
    return {}


def validateUser(username, password):
    for user in users:
        if user["username"] == username and user["password"] == password:
            return user
    return {}


class Admin:
    def __init__(self, username) -> None:
        self.userDetails = getUserByUsername(username)
        self.username = username
        print(self.userDetails)

    def getAdmin():
        while (True):
            username = getString("Please provide the username")
            password = getString("Please provide the password")
            user = validateUser(username=username, password=password)
            if user and user["userType"] == OWNER:
                return Admin(username=username)
            else:
                print("Please provide valid credentials!!")

    def showCinemaSlots(self):
        cinema = categories[CINEMA][self.username]
        cinema.show()


class User:
    def __init__(self, username) -> None:
        self.userDetails = getUserByUsername(username)
        self.username = username

    def getUser():
        while (True):
            username = getString("Please provide the username")
            password = getString("Please provide the password")
            user = validateUser(username=username, password=password)
            if user and user["userType"] == CUSTOMER:
                return User(username=username)
            else:
                print("Please provide valid credentials!!")

    def bookCinemaTickets(self):
        showSlotsBySlotType(CINEMA)
        name = getString("Provide SlotID:")
        if name in categories[CINEMA].keys():
            cinema = categories[CINEMA][name]
            cinema.show()
            seatID = getIntegerInRange(
                "Provide a seat Number", 1, cinema.n*cinema.n)
            cinema.bookTicket(self.username, seatID,None)
        else:
            print("No Slot avialable for given input")

    def bookRestaurantTickets(self):
        showSlotsBySlotType(RESTAURANT)
        name = getString("Provide SlotID:")
        if name in categories[RESTAURANT].keys():
            restaurant = categories[RESTAURANT][name]
            restaurant.show()
            seatID = getIntegerInRange(
                "Provide a seat Number", 1, restaurant.n*restaurant.n)
            restaurant.bookTicket(self.username, seatID,None)
        else:
            print("No Slot avialable for given input")
    
    def bookHotelTickets(self):
        showSlotsBySlotType(HOTEL)
        name = getString("Provide SlotID:")
        if name in categories[HOTEL].keys():
            hotel = categories[HOTEL][name]
            hotel.show()
            seatID = getIntegerInRange(
                "Provide a seat Number", 1, hotel.n*hotel.n)
            hotel.bookTicket(self.username, seatID,None)
        else:
            print("No Slot avialable for given input")

    def bookAirplaneTickets(self):
        showSlotsBySlotType(AIRPLANE)
        name = getString("Provide SlotID:")
        if name in categories[AIRPLANE].keys():
            airplane = categories[AIRPLANE][name]
            airplane.show()
            seatID = getIntegerInRange(
                "Provide a seat Number", 1, airplane.n*airplane.n)
            airplane.bookTicket(self.username, seatID,None)
        else:
            print("No Slot avialable for given input")

    def bookConferenceTickets(self):
        showSlotsBySlotType(CONFIERENCE)
        name = getString("Provide SlotID:")
        if name in categories[CONFIERENCE].keys():
            conference = categories[CONFIERENCE][name]
            conference.show()
            seatID = getIntegerInRange(
                "Provide a seat Number", 1, conference.n*conference.n)
            conference.bookTicket(self.username, seatID,None)
        else:
            print("No Slot avialable for given input")

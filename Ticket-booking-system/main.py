
class Cinema():
    def __init__(self, rows, cols, base_cost):
        self.rows = rows
        self.cols = cols
        self.base_cost = base_cost
        self.seats = [[0 for j in range(cols)] for i in range(rows)]
        self.sell_list = {}
        self.booking_list = [] 
        self.time_slots = {
        '1': '9:00 am',
        '2': '3:00 pm'
        }
        self.bookings = {} 
        self.booked_seats = [] 
        self.available_seats = [] 
        self.users = {}
        self.count = 1
        self.Total_income = 0

    def display_menu(self):
        print()
        print("Welcome to PVR CINEMAS")
        print("------------------------")
        print("Please select an option:")
        print("1. View available seats")
        print("2. Book a seat")
        print("3. Cancel a booking")
        print("4. Change a booking")
        print("5. View sell list")
        print("6. Add a seat to the sell list")
        print("7. Access Internal messaging System")
        print("8. Exit")
        choice = input("Enter option number: ")
        if choice == "1":
            self.display_seats()
            self.display_menu()
        elif choice == "2":
            self.reserve_seat()
            self.display_menu()
        elif choice == "3":
            seat_id = input("Enter seat ID: ")
            self.cancel_booking(seat_id)
            self.display_menu()
        elif choice == "4":
            seat_id = input("Enter seat ID: ")
            self.change_booking(seat_id)
            self.display_menu()
        elif choice == "5":
            self.display_sell_list()
            self.display_menu()
        elif choice == "6":
            self.add_to_sell_list()
            self.display_menu()
        elif choice == "7":
            self.messaging_service()
            self.display_menu()
        elif choice == "8":
            self.exit()
        else:
            print("Invalid option. Please try again.")
            self.display_menu() 

    def calculate_seat_cost(self, row, col, base_cost): 

        first_row_cost = self.base_cost * 2  # 100% more expensive
        last_row_cost = self.base_cost * 0.75  # 25% less expensive
        middle_cols_cost = self.base_cost * 1.25  # 25% more expensive
        
        if row == 1:
            return first_row_cost
        elif row == self.rows:
            return last_row_cost
        elif col in [1, self.cols]:
            return self.base_cost
        else:
            return middle_cols_cost

        

    def display_seats(self):
        # display the available seats
        for i in range(self.rows):
            for j in range(self.cols):
                if self.seats[i][j] == 0:
                    print("0", end=" ")
                else:
                    print("X", end=" ")
            print()

    def reserve_seat(self):
        while True:
            # Prompt user to select a time slot
            print("Select a time slot:")
            for slot_id, slot_time in self.time_slots.items():
                print(f"{slot_id}: {slot_time}")
            slot_choice = input("Enter time slot number: ")
            if slot_choice in self.time_slots:
                selected_time = self.time_slots[slot_choice]
                break
            else:
                print("Invalid input. Please try again.")

        while True:
            # Prompt user to select a seat
            row = int(input("Enter row number: "))
            col = int(input("Enter column number: "))
            if not (1 <= row <= self.rows and 1 <= col <= self.cols):
                print("Invalid row or column number. Please try again.")
                continue

            if self.seats[row-1][col-1] == 1:
                print("This seat is already reserved. Please select another seat.")
                continue

            cost = self.calculate_seat_cost(row, col, base_cost)

            # Display cost of seat and prompt user to confirm reservation
            print("The cost of this seat is:", cost)
            confirm = input("Do you want to reserve this seat? (y/n): ")
            if confirm == "y":
                self.seats[row-1][col-1] = 1
                selected_seat = f"{chr(ord('A') + col - 1)}{row}"
                self.bookings[selected_seat] = {"time": selected_time, "cost": cost}
                self.Total_income = self.Total_income + self.calculate_seat_cost(row, col, base_cost)
                self.booked_seats.append(selected_seat)
                self.update_booked_seats()
                print("Seat reserved!")
                print(f"Reserved seat details: {selected_seat}, time slot {selected_time}, cost {cost}")
                self.display_seats()
                break
            else:
                print("Seat not reserved.") 
    
    def update_booked_seats(self):
        self.booked_seats.clear()
        for i in range(self.rows):
            for j in range(self.cols):
                if self.seats[i][j] == 1:
                    self.booked_seats.append(f"{chr(ord('A') + j)}{i+1}")

    def cancel_booking(self, seat_id):
   
        if seat_id in self.booked_seats:
            confirmation = input("Are you sure you want to cancel the booking for seat {} because no amout will be refunded if you cancel? (y/n)".format(seat_id))
            if confirmation == "y":
                self.booked_seats.remove(seat_id)
                self.available_seats.append(seat_id)
            
                i = seat_id[0] 
                i = ord(i) - 64
                j = seat_id[1] 
                j = int(j)
                self.seats[i-1][j-1] = 0
                print("Booking for seat {} has been cancelled and added back to the available seats list.".format(seat_id))
            else:
                print("Booking cancellation for seat {} has been cancelled.".format(seat_id))
        else:
            print("Seat {} is not currently booked.".format(seat_id))

    def change_booking(self, seat_id):
        # change a booking
        
        # Check if seat is already booked
        if seat_id not in self.bookings:
            print("This seat is not booked.")
            return

        # Get row and column numbers from seat ID
        col = ord(seat_id[0]) - ord('A')
        row = int(seat_id[1:])

        # Display current booking details
        cost = self.calculate_seat_cost(row, col, base_cost)
        print(f"Current booking details: row {row}, column {chr(col + ord('A'))}, time slot {self.bookings[seat_id]['time']}, cost {cost}")

        # Prompt user to select a new seat
        while True:
            # Prompt user to select a seat
            new_row = int(input("Enter new row number: "))
            new_col = input("Enter new column letter: ").upper()
            if not (1 <= new_row <= self.rows and 'A' <= new_col <= chr(ord('A') + self.cols - 1)):
                print("Invalid row or column letter. Please try again.")
                continue

            # Check if new seat is already reserved
            new_col_num = ord(new_col) - ord('A')
            if self.seats[new_row-1][new_col_num] == 1:
                print("This seat is already reserved. Please select another seat.")
                continue

            # Calculate cost of seat based on its zone
            new_cost = self.calculate_seat_cost(new_row, new_col_num, base_cost)

            # Display cost of seat and prompt user to confirm reservation
            print("The cost of this seat is:", new_cost)
            confirm = input("Do you want to change to this seat? (y/n): ")
            if confirm == "y":
                # Update seat reservation
                self.seats[row-1][col] = 0
                self.seats[new_row-1][new_col_num] = 1
                new_seat_id = f"{new_col}{new_row}"
                self.bookings[new_seat_id] = {"time": self.bookings[seat_id]["time"], "cost": new_cost}
                del self.bookings[seat_id]
                self.booked_seats.remove(seat_id)
                self.booked_seats.append(new_seat_id)
                self.update_booked_seats()
                print("Seat reservation updated!")
                print(f"New seat details: {new_seat_id}, time slot {self.bookings[new_seat_id]['time']}, cost {new_cost}")
                self.display_seats()
                break
            else:
                print("Seat change cancelled.")


    def display_sell_list(self):
        # display the sell list
        
        if len(self.sell_list) == 0:
            print("No seats are currently available for sale.")
        else:
            print("The following seats are available for sale:")
            
            for i in self.sell_list: 
                print(self.sell_list[i])

    def add_to_sell_list(self):
        # add a seat to the sell list
        
    # Prompt the user for the details of the seat they want to sell
        business_type = input("Enter the business type of the seat: ")
        seat_number = input("Enter the seat number: ")
        cost = float(input("Enter the cost of the seat: "))
        discount_ratio = float(input("Enter the discount ratio (in decimal form) for the seat: "))
        
        # Create a dictionary with the seat details and add it to the sell_list
        seat_details = {
            "business_type": business_type,
            "seat_number": seat_number,
            "cost": cost,
            "discount_ratio": discount_ratio
        }
        self.sell_list[self.count] = seat_details 
        self.count += 1
        self.display_sell_list()
        

    def messaging_service(self):
        messages = {}
        while True:
            print("Sell List: ", self.sell_list)
            print("Messages: ", messages)
            print("1. Send message")
            print("2. View messages")
            print("3. Make offer")
            print("4. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                recipient = input("Enter recipient username: ")
                message = input("Enter message: ")
                if recipient not in messages:
                    messages[recipient] = []
                messages[recipient].append({"from": recipient, "message": message})
            elif choice == 2:
                
                print("Your messages: ")
                for message in messages[recipient]:
                    print(message["from"], ": ", message["message"])
                
            elif choice == 3:
                offer = float(input("Enter your offer: "))
                discount = float(input("Enter your discount: "))
                if offer < self.sell_list[1]['cost']*(1 - self.sell_list[1]['discount_ratio']):
                    print("Your offer is too low.")
                else:
                    self.sell_list[1]['cost'] = offer
                    self.sell_list[1]['discount_ratio'] = discount
                    print("Your offer has been accepted.")
            elif choice == 4:
                break
            else:
                print("Invalid choice. Try again.")

    def exit(self):
        # exit the program
        pass




class Owner:
    def __init__(self):
        self.username = None
        self.password = None

    def OwnerLogin(self):
        self.Owner_username = input("Enter the user name: ")
        self.Owner_password = input("Enter the password ")

    def CalculateIncome(self):
        income = Cinema(rows, cols, base_cost)
        value = income.calculate_seat_cost(rows, cols, base_cost)
        print("Total income is ", value)

    def ViewSeats(self):
        seats = Cinema(rows, cols, base_cost)
        seats.display_seats()

class SystemAdmin():
    def __init__(self) -> None:
        pass

    def ViewSeats(self):
        seats = Cinema(rows, cols, base_cost)
        seats.display_seats()
    
    def CheckLoginIssues(self):
        login = Cinema(rows, cols, base_cost)
        login.display_menu()

class User():

    def __init__(self):
        self.username = None
        self.password = None

    def LoginToTicketBooking(self):
        self.username = input("Enter the username: ")
        self.password = input("Enter the password: ")

    def TicketBookingTerminal(self):
        Cinema_user = Cinema(rows, cols, base_cost)
        Cinema_user.display_menu()


        
print("------------------------------------")
print("Welcome to seat reservation system")
print("------------------------------------")
Role = 5
Total_seat = 0
while Role != 0:
    Role = int(input('\n ****   Select ****\n1. ADMIN\n2. USER\n3. OWNER\n4. SYSTEM ADMIN\n'))
    if Role == 1:
        username = input("Enter the user name: ")
        password = input("Enter the password: ")
        print()
        rows = int(input('Enter the size of a room\nNumber of seats in a row:  '))
        cols = int(input("Number of seats in a column: "))
        Total_seat = rows*cols
        print("\nAs a room size is square, Total seats available is ", Total_seat)
        base_cost = int(input("\nEnter the base price of a ticket in CAD: "))
        print("\nThanks for the update\n")
        ask = input("Do you want to login to PVR CINEMAS as view the option? (yes/no): ")
        if ask == "yes" :
            Cinema1 = Cinema(rows, cols, base_cost)
            Cinema1.display_menu()
        
   
    elif Role == 2:
        User1 = User()
        User1.LoginToTicketBooking()
        User1.TicketBookingTerminal()


    elif Role == 3:
        Owner1 = Owner()
        Owner1.OwnerLogin()
        Owner1.CalculateIncome()
        Owner1.ViewSeats()

    elif Role == 4:
        sysadmin = SystemAdmin()
        sysadmin.ViewSeats()
        sysadmin.CheckLoginIssues()

    
    else:
        print ("\nPlease select valid input")

# Create a new Cinema object
Cinema = Cinema(rows, cols, base_cost)

# Display the menu
Cinema.display_menu()
import os
import platform
from getpass import getpass
import time



# clear() is a function that will clear the command line interface
#   of any text, leaving the user with a blank slate
#   It is useful for when you want to update the display
#   of information to the user without having to rewrite
#   all of the information that was previously displayed
#   It is also useful for creating a more interactive
#   interface by allowing the user to see only the
#   most relevant information at any given timeh
def clear():
    # The following will clear the command line interface
    #   on Windows systems
    Windows_clear = lambda: os.system("cls")
    # The following will clear the command line interface
    #   on Linux systems
    Linux_clear = lambda: os.system("clear")
    # The following will clear the command line interface
    #   on MacOS systems
    Mac_clear = lambda: os.system("clear")
    # The following will clear the command line interface
    #   on either Windows or Linux systems
    if platform.system() == "Windows":
        Windows_clear()
    elif platform.system() == "Linux":
        Linux_clear()
    elif platform.system() == "Darwin":
        Mac_clear()

def auth():
    while True:
        # Create login authentication from console
        clear()
        print("1. Login")
        print("2. Signup")
        choice = input("Enter your choice: ")
        if choice == "1":
            username = input("Enter your username: ")
            password = getpass("Enter your password: ")
            if username in logins:
                if logins[username][0] == hash(password):
                    print("Login successful")
                    return logins[username][1]
                else:
                    print("Incorrect password")
            else:
                print("User not found")
        elif choice == "2":
            username = input("Enter your username: ")
            password = getpass("Enter your password: ")
            name = input("Enter your name: ")
            age = input("Enter your age: ")
            passport_number = input("Enter your passport number: ")
            if username in logins:
                print("User already exists")
            else:
                logins[username] = [hash(password), Passenger(name, age, passport_number)]
                print("Signup successful")
                
                return Passenger(name, age, passport_number)
        else:
            continue
        input("Press anything to go back")

class Flight:
    reservations = {}
    seats = {}
    def __init__(self, flight_number, destination, departure_time, total_seats: int, booked_seats = 0):
        self.flight_number = flight_number
        self.destination = destination
        self.departure_time = departure_time
        if total_seats < 0:
            raise ValueError("Total seats must be a positive number")
        self.total_seats = int(total_seats)
        self.seats = {i : Seat(i, "Economy", True) for i in range(1, total_seats + 1)} # TODO: add varied layouts seats for first, business and economy class
        self.booked_seats = int(booked_seats)

    def get_flight_number(self):
        return self.flight_number

    def get_destination(self):
        return self.destination

    def get_departure_time(self):
        return self.departure_time

    def get_total_seats(self):
        return self.total_seats

    def get_booked_seats(self):
        return self.booked_seats

    def book(self, reservation, token):
        seat_number = reservation.get_seat_number()
        if seat_number not in self.seats.keys():
            raise KeyError("Invalid seat_number")
        if self.seats[seat_number].is_available == True:
            self.booked_seats += 1
            if token in self.reservations:
                self.reservations[token].append(reservation)
            else:
                self.reservations[token] = [reservation]
            self.seats[seat_number].is_available = False
        else:
            raise ValueError("Unable to book the flight: Seats not available")

    def cancel(self, reservation, token):
        if token not in self.reservations.keys():
            raise KeyError("Unable to cancel the flight: Customer not found")
        Notvalid = True
        for _ in self.reservations[token]:
            if reservation.get_seat_number() == _.get_seat_number():
                Notvalid = False
                break
        if Notvalid:
            raise ValueError("Unable to cancel the flight: Reservation not found")
        self.booked_seats -= 1
        self.seats[reservation.get_seat_number()].is_available = True
        for _ in range(len(self.reservations[token])):
            if reservation.get_seat_number() == self.reservations[token][_].get_seat_number():
                self.reservations[token].pop(_)
                break
                
        if len(self.reservations[token]) == 0:
            del self.reservations[token]

    def view_flight_details(self):
        available_seats = []
        for i in self.seats:
            if (self.seats[i].is_available == True):
                available_seats.append(str(i))

        
        return (
                f"Flight No: {self.flight_number}\n"
                f"Destination: {self.destination}\n"
                f"Departure Time: {self.departure_time}\n"
                f"Total Seats: {self.total_seats}\n"
                f"Booked Seats: {self.booked_seats}\n"
                f"Available Seats: {", ".join(available_seats)}"
                )

class Seat:
    def __init__(self, seat_number, seat_type: str, is_available: bool):    # TODO: add grid layout seats
        self.seat_number = int(seat_number)
        self.seat_type = seat_type
        if not isinstance(is_available, bool):
            raise TypeError("is_available must be a boolean")       
        self.is_available = is_available

class Passenger:
    def __init__(self, name = "John Doe", age = 18, passport_number = "316588"):
        self.__name = name
        self.__age = int(age)
        if age < 0:
            raise ValueError("Age must be a positive number")
        self.__passport_number = passport_number

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_passport_number(self):
        return self.__passport_number

    def get_passenger(self):
        return  f"Name: {self.__name}\n"\
                f"Age: {self.__age}\n"\
                f"Passport Number: {self.__passport_number}"
    def __str__(self):
        return self.get_passenger()

class Reservation(Passenger):
    def __init__(self, flight_number, seat_number, passenger):
        self.__flight = flight_number
        self.__seat_number = int(seat_number)
        if not isinstance(passenger, Passenger):
            raise TypeError("Passenger must be a Passenger object")
        self.passenger = passenger
        super().__init__()

    def get_flight(self):
        return self.__flight
    
    def get_seat_number(self):
        return self.__seat_number
    
    def get_passenger(self):
        return self.passenger
    
class AirlineSystem:
    
    def __init__(self, flights):
        if not isinstance(flights, dict):
            raise TypeError("Flights must be a dictionary")
        for _ in flights.values():
            if not isinstance(_, Flight):
                raise TypeError("Flights must be a dictionary of Flight objects")
        self._flights = flights

    def add_flight(self, flight: Flight):
        if flight.get_flight_number() in self._flights.keys():
            print("Flight already exists")
        else:
            self._flights[flight.get_flight_number()] = flight
            print("Flight successfully added")

        return self

    def book_flight(self, flight_number, seat_number, passenger):
        if flight_number in self._flights:
            flight = self._flights[flight_number]
            try:
                flight.book(Reservation(flight_number, seat_number, passenger), token = passenger.get_passport_number())
                print("Flight booked successfully") 
            except ValueError:
                print("Seat is already booked")
            except SyntaxError:
                print("A reservation already exists")
            except KeyError:
                print("Invalid seat number")
        else:
            print("Flight doesn't exist")

        return self

    def cancel_reservation(self, flight_number, seat_number, passenger):
        if flight_number in self._flights:
            flight = self._flights[flight_number]
            try:
                flight.cancel(Reservation(flight_number, seat_number, passenger), token = passenger.get_passport_number())
                print("Reservation cancelled successfully")
            except ValueError:
                print("No reservation found")
            except KeyError:
                print("No customer's reservations found")
        else:
            print("Flight doesn't exist")

        return self

    def view_flight_details(self, flight_number):
        if flight_number in self._flights:
            flight = self._flights[flight_number]
            return flight.view_flight_details()
        else:
            return "Flight doesn't exist"
        
logins = {"John Doe": [hash("root"), Passenger()]}

if __name__ == "__main__":
    flights = {"1": Flight("1","Seoul/Incheon", "22:40", 2)}
    system = AirlineSystem(flights)
    
    while True:
        passenger = auth()  # TODO: Anti-bruteforce
        time.sleep(2)

        clear()
        title = r"""

  /$$$$$$  /$$           /$$ /$$                            /$$$$$$                        /$$            /$$$$$$                        /$$                            
 /$$__  $$|__/          | $$|__/                           /$$__  $$                      | $$           /$$__  $$                      | $$                            
| $$  \ $$ /$$  /$$$$$$ | $$ /$$ /$$$$$$$   /$$$$$$       | $$  \__/  /$$$$$$   /$$$$$$  /$$$$$$        | $$  \__/ /$$   /$$  /$$$$$$$ /$$$$$$    /$$$$$$  /$$$$$$/$$$$ 
| $$$$$$$$| $$ /$$__  $$| $$| $$| $$__  $$ /$$__  $$      |  $$$$$$  /$$__  $$ |____  $$|_  $$_/        |  $$$$$$ | $$  | $$ /$$_____/|_  $$_/   /$$__  $$| $$_  $$_  $$
| $$__  $$| $$| $$  \__/| $$| $$| $$  \ $$| $$$$$$$$       \____  $$| $$$$$$$$  /$$$$$$$  | $$           \____  $$| $$  | $$|  $$$$$$   | $$    | $$$$$$$$| $$ \ $$ \ $$
| $$  | $$| $$| $$      | $$| $$| $$  | $$| $$_____/       /$$  \ $$| $$_____/ /$$__  $$  | $$ /$$       /$$  \ $$| $$  | $$ \____  $$  | $$ /$$| $$_____/| $$ | $$ | $$
| $$  | $$| $$| $$      | $$| $$| $$  | $$|  $$$$$$$      |  $$$$$$/|  $$$$$$$|  $$$$$$$  |  $$$$/      |  $$$$$$/|  $$$$$$$ /$$$$$$$/  |  $$$$/|  $$$$$$$| $$ | $$ | $$
|__/  |__/|__/|__/      |__/|__/|__/  |__/ \_______/       \______/  \_______/ \_______/   \___/         \______/  \____  $$|_______/    \___/   \_______/|__/ |__/ |__/
                                                                                                                   /$$  | $$                                            
                                                                                                                  |  $$$$$$/                                            
                                                                                                                   \______/                                             

__________________________________________________________________________________________________________________________________________________________________________
    _    ____ ____
   / \  / ___/ ___|
  / _ \ \___ \___ \
 / ___ \ ___) |__) |
/_/   \_\____/____/
"""
    
        while True:
            print(title)
            print("1. Add a flight")
            print("2. Book a flight")
            print("3. Cancel a reservation")
            print("4. View flight details")
            print("5. View passengers details")
            print("6. Exit the program")
            print("7. Log out")
            choice = input("Enter your choice: ")
            clear()
            if choice == "1":
                flight_number = input("Enter the flight number: ")
                destination = input("Enter the destination: ")
                departure_time = input("Enter the departure time: ")
                total_seats = int(input("Enter the total number of seats: "))
                flight = Flight(flight_number, destination, departure_time, total_seats)
                system.add_flight(flight)
            elif choice == "2":
                flight_number = input("Enter the flight number: ")
                seat_number = int(input("Enter the seat number: "))
                system.book_flight(flight_number, seat_number, passenger)
            elif choice == "3":
                flight_number = input("Enter the flight number: ")
                seat_number = int(input("Enter the seat number: "))
                system.cancel_reservation(flight_number, seat_number, passenger)
            elif choice == "4":
                flight_number = input("Enter the flight number: ")
                print(system.view_flight_details(flight_number))
            elif choice == "5":
                print(passenger.get_passenger())
            elif choice == "6":
                exit()
            elif choice == "7":
                break
            else:
                continue
            time.sleep(1.2)
            getpass("Press anything to go back")
            clear()


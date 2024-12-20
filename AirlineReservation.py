import os
import platform

# clear() is a function that will clear the command line interface
#   of any text, leaving the user with a blank slate
#   It is useful for when you want to update the display
#   of information to the user without having to rewrite
#   all of the information that was previously displayed
#   It is also useful for creating a more interactive
#   interface by allowing the user to see only the
#   most relevant information at any given time
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
        dict({token: None}, self.reservations)  # Check duplicate tokens
        seat_number = reservation.get_seat_number()
        if self.seats[seat_number].is_available == True:
            self.booked_seats += 1
            self.reservations[token] = reservation
            self.seats[seat_number].is_available = False
        raise ValueError("Unable to book the flight: Seats not available")

    def cancel(self, token):
        if token not in self.reservations.keys():
            raise ValueError("Unable to cancel the flight: Customer not found")
        self.booked_seats -= 1
        del self.reservations[token]

    def view_flight_details(self):
        available_seats = []
        for i in self.seats:
            if (self.seats[i].is_available == True):
                available_seats.add(i)

        
        return (
                f"Flight No: {self.__flight_number}\n"
                f"Destination: {self.__destination}\n"
                f"Departure Time: {self.__departure_time}\n"
                f"Total Seats: {self.__total_seats}\n"
                f"Booked Seats: {self.__booked_seats}\n"
                f"Available Seats: {", ".join(*available_seats)}"
                )

class Seat:
    def __init__(self, seat_number, seat_type: str, is_available: bool):    # TODO: add grid layout seats
        self.seat_number = seat_number
        self.seat_type = seat_type
        if not isinstance(is_available, bool):
            raise TypeError("is_available must be a boolean")       
        self.is_available = is_available

class Passenger:
    def __init__(self, name, age: int, passport_number):
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


class Reservation(Passenger):
    def __init__(self, flight_number, seat_number, name, age, passport_number):
        self.__flight = str(flight_number)
        self.__seat_number = seat_number
        super().__init__(name, age, passport_number)

    def get_flight(self):
        return self.__flight
    
    def get_seat_number(self):
        return self.__seat_number
    
    def get_passenger(self):
        return Passenger(self.get_name(), self.get_age(), self.get_passport_number)
    
class AirlineSystem:
    def __init__(self):
        self.__flights = {}

    def add_flight(self, flight: Flight):
        self.__flights[flight.get_flight_number()] = flight

    def book_flight(self, flight_number, seat_number, name, age: int, passport_number):
        if flight_number in self.__flights:
            flight = self.__flights[flight_number]
            try:
                flight.book(Reservation(flight_number, seat_number, name, age, passport_number), token = passport_number)
                print("Flight booked successfully") 
            except ValueError:
                print("Seat is already booked")
            except SyntaxError:
                print("A reservation already exists")
        print("Flight doesn't exist")

    def cancel_reservation(self, flight_number, passport_number):
        if flight_number in self.__flights:
            flight = self.__flights[flight_number]
            try:
                flight.cancel(token = passport_number)
                print("Reservation cancelled successfully")
            except ValueError:
                print("No reservation found")
        print("Flight doesn't exist")

    def view_flight_details(self, flight_number):
        if flight_number in self.__flights:
            flight = self.__flights[flight_number]
            return flight.view_flight_details()
        print("Flight doesn't exist")

    def view_passenger_details(self, flight_number):
        if flight_number in self.__flights:
            flight = self.__flights[flight_number]
            passengers = []
            for reservation in flight:
                passengers.append(reservation.get_passenger())
            return passengers
        print("Flight doesn't exist")


if __name__ == "__main__":
    clear()
    system = AirlineSystem()
    while True:
        print("1. Add a flight")
        print("2. Book a flight")
        print("3. Cancel a reservation")
        print("4. View flight details")
        print("5. View passenger details")
        print("6. Exit")
        choice = input("Enter your choice: ")
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
            name = input("Enter the name: ")
            age = int(input("Enter the age: "))
            passport_number = input("Enter the passport number: ")
            system.book_flight(flight_number, seat_number, name, age, passport_number)
        elif choice == "3":
            flight_number = input("Enter the flight number: ")
            passport_number = input("Enter the passport number: ")
            system.cancel_reservation(flight_number, passport_number)
        elif choice == "4":
            flight_number = input("Enter the flight number: ")
            print(system.view_flight_details(flight_number))
        elif choice == "5":
            flight_number = input("Enter the flight number: ")
            print(system.view_passenger_details(flight_number))
        elif choice == "6":
            exit()
        input("Press anything to go back")
        clear()


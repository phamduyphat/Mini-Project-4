class Flight:
    reservations = {}
    def __init__(self, flight_number, destination, departure_time, total_seats: int, booked_seats = 0):
        self.flight_number = flight_number
        self.destination = destination
        self.departure_time = departure_time
        if total_seats < 0:
            raise ValueError("Total seats must be a positive number")
        self.total_seats = int(total_seats)
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

        if self.booked_seats < self.total_seats:
            self.booked_seats += 1
            self.reservations[token] = reservation
        raise ValueError("Unable to book the flight: No available seats")

    def cancel(self, token):
        if token not in self.reservations.keys():
            raise ValueError("Unable to cancel the flight: Customer not found")
        self.booked_seats -= 1
        del self.reservations[token]

    def view_flight_details(self):
        return (
                f"Flight No: {self.__flight_number}\n"
                f"Destination: {self.__destination}\n"
                f"Departure Time: {self.__departure_time}\n"
                f"Total Seats: {self.__total_seats}\n"
                f"Booked Seats: {self.__booked_seats}\n"
                f"Available Seats: {self.__total_seats - self.__booked_seats}\n"
                )

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
    def __init__(self, flight_number, name, age, passport_number):
        self.__flight = str(flight_number)
        super().__init__(name, age, passport_number)

    def get_flight(self):
        return self.__flight
    
    def get_passenger(self):
        return Passenger(self.get_name(), self.get_age(), self.get_passport_number)
    
class AirlineSystem:
    def __init__(self):
        self.__flights = {}

    def add_flight(self, flight: Flight):
        self.__flights[flight.get_flight_number()] = flight

    def book_flight(self, flight_number, name, age: int, passport_number):
        if flight_number in self.__flights:
            flight = self.__flights[flight_number]
            try:
                flight.book(Reservation(flight_number, name, age, passport_number), token = passport_number)
                print("Flight booked successfully") 
            except ValueError:
                print("Flight is fully booked")
            except SyntaxError:
                print("Reservation already exists")
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
    pass
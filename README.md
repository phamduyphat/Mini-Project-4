# [Airline Reservation System](https://github.com/phamduyphat/Mini-Project-4)

## Table of Contents
- [Introduction](#introduction)
- [Program Structure](#program-structure)
- [Key Components](#key-components)
- [OOP Concepts Utilized](#oop-concepts-utilized)
- [Challenges Faced](#challenges-faced)
- [Installation and Usage](#installation-and-usage)

## Introduction

This project implements an airline reservation system using Python. It allows users to manage flights, book reservations, cancel bookings, and view flight details. The system is designed to demonstrate Object-Oriented Programming (OOP) concepts and provide a practical application of these principles.

## Program Structure

The system is built around several interconnected classes:

1. `Flight`: Represents individual flights with attributes like flight number, destination, departure time, total seats, and booked seats.
2. `Seat`: Manages individual seats within a flight, including availability status.
3. `Passenger`: Stores passenger information such as name, age, and passport number.
4. `Reservation`: Links passengers to specific flights and seats.
5. `AirlineSystem`: Manages the overall system, including adding flights, booking/canceling reservations, and viewing flight details.

The main program flow is controlled by the `auth()` function, which handles user login and signup. The `if __name__ == "__main__"` block provides the main menu-driven interface.

## Key Components

- `Flight` class:
  - Attributes: flight_number, destination, departure_time, total_seats, booked_seats
  - Methods: book(), cancel(), view_details()

- `Seat` class:
  - Attributes: seat_number, seat_type, is_available
  - Method: is_available()

- `Passenger` class:
  - Attributes: name, age, passport_number
  - Method: get_passenger_info()

- `Reservation` class:
  - Attributes: flight_number, seat_number, passenger
  - Methods: get_flight(), get_seat_number(), get_passenger()

- `AirlineSystem` class:
  - Methods: add_flight(), book_flight(), cancel_reservation(), view_flight_details()

## OOP Concepts Utilized

* Classes and Objects
* Encapsulation (use of private attributes and getter/setter methods)
* Inheritance
* Polymorphism (method overriding or overloading)

## Challenges Faced

### 1. Collaborative Coding and Task Distribution

Working in a group of four presented unique challenges. Achieving consistency across the entire project was difficult since all members had different coding styles. The need to develop the system incrementally, with completion of one section before moving to the next, forced simultaneous collaboration and consolidation phases. This is different from previous projects that are handled piece by piece, requiring careful planning and coordination.

### 2. Balancing OOP Principles with Practicality

Although the assignment made a big point of encapsulation, inheritance, and polymorphism, the team had to weigh these principles against the dangers of over-complication. They needed to be critical in assessing where such concepts really improved the system and where simpler ways would work.

### 3. Comprehensive Error Handling

Developing a flight reservation system required great attention to error handling and input validation. The conditional statements used here are quite extensive in managing a variety of scenarios so that the system remains stable and user-friendly even when receiving unexpected inputs or edge cases.

### 4. Clarifying Assignment Requirements

The project prompt had some ambiguities that needed interpretation. Group members worked together to clarify these points, such as the separation of employee and customer functionalities, the limitation of purchasing tickets by one customer, and other logical divisions of the system.

These challenges not only tested the team's coding skills but also their ability to collaborate effectively, interpret complex requirements, and balance theoretical concepts with practical implementation needs.

## Installation and Usage

To run this program:
1. Ensure Python is installed on your system.
2. Clone or download the repository.
3. Run the script using a Python interpreter.

## Credits

This project was made possible by the following students from VinUniversity COMP1010 - Fall 2024 Group 9:

- Le Thao Vy
- Nguyen Anh Duc
- Nguyen Dat Thanh
- [Pham Duy Phat](https://phamduyphat.pp.ua)
- Pham Tien Huy

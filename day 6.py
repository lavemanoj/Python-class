from abc import ABC, abstractmethod

# encapsulation
# 1.wrap code and data
# 2.data hiding


# class bankaccount:
#     def __init__(self,name,balance):
#         self.name = name
#         self.balance = balance

#     def deposit(self,amount):
#         self.balance += amount
#         print("Deposited",amount)
#     def withdraw(self,amount):
#         if amount<= self.balance:
#             self.balance -= amount
#             print("Withdraw successful",self.balance)
#         else:
#             print("Insufficient balance")
# def show_balance(self):
#     print(self._balance)

# pin=1234
# name=input("Enter your name: ")
# balance=int(input("Enter initial balance: "))
# pin=int(input("Enter your pin: "))

# s=bankaccount(name,balance)
# if pin==1234:
#     print("Login successful")
# elif pin!=1234:
#     print("Invalid pin")
#     exit()
# while True:
#     print("\n1.deposit\n2.withdraw\n3.show balance\n4.exit")
#     choice=int(input("Enter your choice: "))
#     if choice==1:
#         amount=int(input("Enter amount to deposit: "))
#         s.deposit(amount)
#     elif choice==2:
#         amount=int(input("Enter amount to withdraw: "))
#         s.withdraw(amount)
#     elif choice==3:
#         s.show_balance()
#     elif choice==4:
#         break





# polymorphism
# #build in polymorphism
# #len
# print(len("hello"))
# print(len([1,2,3,4,5]))
# #operator polymorphism
# print(5+3)
# print("5"+"3")

# def add(a,b):
#     return a+b
# print(add(2,3))

# print(add("hello","world"))

# class animal:
#     def sound(self):
#         print("Animal makes a sound")

# class dog(animal):
#     def sound(self):
#         print("Dog barks")

# class cat(animal):
#     def sound(self):
#         print("Cat meows")

# d=dog()
# c=cat()

# d.sound()
# c.sound()


# inheritance,polmorphism,abstraction,encapsulation
# class bankaccount:
#     def __init__(self,name,balance):
#         self.name = name
#         self.balance = balance

#     def deposit(self,amount):
#         self.balance += amount
#         print("Deposited",amount)
    
#     def withdraw(self,amount):
#        pass

# def show_balance(self):
#     print(self._balance)

# class savingsaccount:
#     def withdraw(self,amount):
#         if amount<= self.balance:
#             self.balance -= amount
#             print("Withdraw from savings")
#         else:
#             print("Insufficient balance in savings account")

# class currentaccount:
#     def withdraw(self,amount):
#         if amount<= self.balance:
#             self.balance -= amount
#             print("Withdraw od withdraw")
#         else:
#             print("Insufficient balance ")

# pin=1234
# name=input("Enter your name: ")
# balance=int(input("Enter initial balance: "))
# pin=int(input("Enter your pin: "))

# s=bankaccount(name,balance)
# if pin==1234:
#     print("Login successful")
# elif pin!=1234:
#     print("Invalid pin")
#     exit()
# while True:
#     print("\n1.deposit\n2.withdraw\n3.show balance\n4.exit")
#     choice=int(input("Enter your choice: "))
#     if choice==1:
#         amount=int(input("Enter amount to deposit: "))
#         s.deposit(amount)
#     elif choice==2:
#         amount=int(input("Enter amount to withdraw: "))
#         s.withdraw(amount)
#     elif choice==3:
#         s.show_balance()
#     elif choice==4:
#                 break
        
        

# class Vehicle(ABC):
#     def __init__(self, number, total_seats):
#         self.number = number
#         self.total_seats = total_seats

#     def calculate_fare(self):
#         pass

#     def show_details(self):
#         print(f"Bus Number: {self.number}")
#         print(f"Total Seats: {self.total_seats}")


# class LuxuryBus(Vehicle):
#     def calculate_fare(self):
#         return 500


# class OrdinaryBus(Vehicle):
#     def calculate_fare(self):
#         return 200


# class SeatManager:
#     def __init__(self, total_seats):
#         self.__total_seats = total_seats
#         self.__booked = []

#     def book_seat(self):
#         if len(self.__booked) < self.__total_seats:
#             seat_no = len(self.__booked) + 1
#             self.__booked.append(seat_no)
#             return seat_no
#         return None

#     def cancel_seat(self, seat_no):
#         if seat_no in self.__booked:
#             self.__booked.remove(seat_no)
#             return True
#         return False

#     def available_seats(self):
#         return self.__total_seats - len(self.__booked)


# class Passenger:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")


# class Ticket:
#     def __init__(self, passenger, bus, seat, fare):
#         self.passenger = passenger
#         self.bus = bus
#         self.seat = seat
#         self.fare = fare

#     def show_ticket(self):
#         print("\n--- TICKET ---")
#         self.passenger.show()
#         self.bus.show_details()
#         print(f"Seat Number: {self.seat}")
#         print(f"Fare: ₹{self.fare}")
#         print("-" * 30)
# print("\n1. Luxury Bus (₹500)")
# print("2. Ordinary Bus (₹200)")
# bus_choice = int(input("Choose bus type: "))

# if bus_choice == 1:
#     bus = LuxuryBus("LB101", 5)
# elif bus_choice == 2:
#     bus = OrdinaryBus("OB201", 5)
# else:
#     print("Invalid choice")
# seat_manager = SeatManager(bus.total_seats)
# tickets = []

# while True:
#     print("\n1. Available Seats")
#     print("2. Book Seat")
#     print("3. Cancel Seat")
#     print("4. Show Tickets")
#     print("5. Exit")

#     choice = int(input("Enter choice: "))

#     if choice == 1:
#         print(f"Available Seats: {seat_manager.available_seats()}")

#     elif choice == 2:
#         name = input("Enter passenger name: ")
#         age = int(input("Enter passenger age: "))

#         seat = seat_manager.book_seat()
#         if seat is None:
#             print("Bus is full!")
#         else:
#             passenger = Passenger(name, age)
#             fare = bus.calculate_fare()
#             ticket = Ticket(passenger, bus, seat, fare)
#             tickets.append(ticket)
#             ticket.show_ticket()

#     elif choice == 3:
#         seat_no = int(input("Enter seat number to cancel: "))

#         if seat_manager.cancel_seat(seat_no):
#             tickets = [t for t in tickets if t.seat != seat_no]
#             print(f"Seat {seat_no} cancelled successfully")
#         else:
#             print("Invalid seat number")

#     elif choice == 4:
#         if tickets:
#             for ticket in tickets:
#                 ticket.show_ticket()
#         else:
#             print("No tickets booked yet")

#     elif choice == 5:
#         print("Thank you for using Bus Ticket Booking System!")
#         break

#     else:
#         print("Invalid choice")

# Pre-defined API
# def guess(num: int) -> int:

# def guessNumber(n: int) -> int:
#     left = 1
#     right = n

#     while left <= right:
#         mid = (left + right) // 2
#         result = guess(mid)

#         if result == 0:
#             return mid
#         elif result == -1:
#             right = mid - 1
#         else:  
#             left = mid + 1
word = input("Enter a word: ")
def detectCapitalUse(word):
    return (
            word.isupper() or
            word.islower() or
            word.istitle()
        )
print("Correct Capital Usage:", detectCapitalUse(word))     
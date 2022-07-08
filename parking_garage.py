import os

# Define parking spots

#   If spots available
# Take ticket decrese parking spots
#   If full
#Goodbye

#  **track ticket time**

#  pay ticket 

# parking spost + 1


class Tracking():
    garage = {'spots': 10, 'tickets_take': 0, 'profit': 0}

    def __init__(self):
        self.time = 0.0

    def spots_available(self):
        pass
    def take_ticket(self, time):
        pass                        #remove 1 spot add ticket takes
    def pay_ticket(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        price = self.time * 5.25
        paying = True
        while paying:
            print(f"\nTicket price is: ${price}")                         #add 1 spot add proft + payment 
            p = input("\nHow will you be paying: Cash or Card ").lower()
            if p.lower() == 'cash':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Sorry we don't take cash")
            elif p.lower() == 'card':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Have a wonderful day')
                self.garage['spots']+= 1
                paying = False
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Please select a valid payment method.....idiot")

dylan = Tracking()
dylan.pay_ticket()


# class ParkingGarage():    
#     tracking = Tracking()

#     def enter_garage(cls):
#         if cls.spots_available():
#             time = int(input("How many hours will you be parked? "))
#             cls.take_ticket(time)
#         else:
#             print("Sorry all full. Come back later.")

#     def leave_garage(cls):
#         cls.payticket()



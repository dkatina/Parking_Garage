from http.client import PAYMENT_REQUIRED
import os



#---------------------------Ticket-Tracking-----------------------

class Tracking():
    garage = {'spots': 3, 'tickets_taken': 0, 'profit': 0}
    current_tickets = {}    #Store ticket number and time

    def spots_available(self):
        if self.garage['spots'] > 0:
            return  True
        else:
            return False

    def take_ticket(self, time):
        if self.current_tickets:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.garage['tickets_taken'] += 1
            self.ticket = self.garage['tickets_taken']
            self.current_tickets[self.ticket] = time
            print(f'Your ticket number is: {self.ticket}')
            self.acknowledge(self.ticket)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Your ticket number is: 1')
            self.current_tickets[1] = time
            self.garage['tickets_taken'] = 1
            self.acknowledge(1)
        self.garage['spots'] -= 1


    def acknowledge(self, ticket):
        understand = input("\nIf you lose this ticket you will be fined, do you understand? yes/no ")
        if understand == 'yes':
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print(""" 
            YOUR TICKET HAS BEEN INVALIDATED AND THE IQ POLICE HAVE BEEN CALLED
                  YOU ARE CLEARLY TOO DUMB TO NOT BE IN AN INSTATUTION!""")
            del self.current_tickets[ticket]
            self.garage['spots'] += 1
            

    def pay_ticket(self, ticket_number):                                                       #Gives you a ticket number based on how number of tickets sold                                                                               #Appends ticket number to current_ticketlist
        os.system('cls' if os.name == 'nt' else 'clear')
        time = self.current_tickets[ticket_number]
        price = time * 5.00
        paying = True
        while paying:
            print(f"\nTicket price is: ${price}")                         
            p = input("\nHow will you be paying: Cash or Card ").lower()
            if p.lower() == 'cash':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Sorry we don't take cash")
            elif p.lower() == 'card':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Have a wonderful day')
                self.garage['spots']+= 1
                self.garage['profit'] += price
                del self.current_tickets[ticket_number]
                paying = False
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Please select a valid payment method.....idiot")
    
    def pay_max(self):
        print("Because you have lost your ticket, you're required to pay the max amount.")
        print()
        paying = True
        while paying:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Price: $1000.00")
            print()
            p = input("\nHow will you be paying: Cash or Card ").lower()
            if p.lower() == 'cash':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Sorry we don't take cash")
            elif p.lower() == 'card':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Have a wonderful day!')
                self.garage['spots']+= 1
                paying = False
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Please select a valid payment method.....idiot")

    def get_total_tickets(cls):
        return cls.garage['tickets_taken']

    def get_active_tickets(cls):
        print("Active tickets include: \n")
        for ticket in cls.current_tickets:
            print(f"Ticket Number {ticket}")
    
    def get_profit(cls):
        return cls.garage['profit']

    def get_spots(cls):
        return cls.garage['spots']

#---------------------Portal----------------------------    

class Portal():

    tracking = Tracking()

    def manager_portal(cls):
        managing = True
        while managing:
            os.system('cls' if os.name == 'nt' else 'clear')
            check = input("""Would you like to check:
            
Total Tickets Issued
Active Tickets
Profits
            
Close Up

            """).lower()
            if check == 'close up':
                cls.active = False
                managing = False
                print("Have a nice day!")
            elif check == 'total tickets issued':
                os.system('cls' if os.name == 'nt' else 'clear')
                tickets = cls.tracking.get_total_tickets()
                print(f"{tickets} ticket(s) have been issued")
            elif check == 'active tickets':
                os.system('cls' if os.name == 'nt' else 'clear')
                cls.tracking.get_active_tickets()
            elif check == 'profits':
                os.system('cls' if os.name == 'nt' else 'clear')
                profit = cls.tracking.get_profit()
                print(f"${profit} made today") 
            else:
                print("Invalid Selection")
            if managing:
                another = input("\nWould you like to check something else: Yes/No ").lower()
                if another == 'no':
                    managing = False
                    print("Have a nice day!")


#-------------------------------Main UI--------------------------------

class ParkingGarage():    
    tracking = Tracking()
    portal = Portal()
    active = True
    @classmethod
    def main(cls):
        os.system('cls' if os.name == 'nt' else 'clear')
        while cls.active:
            option = input("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Welcome to D&G Tiny Parking 

Are You Entering - Leaving - Management 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                :""").lower()
            if option == 'entering':
                cls.enter_garage()
            elif option == 'leaving':
                cls.leave_garage()
            elif option == 'management':
                pw = int(input("What is your manager code?: "))
                if pw == 1234:
                    cls.portal.manager_portal()
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("\nInvalid code!")
                    print("\nBeat it Pal!")
            else:
                print('Invalid option please try again.')
    @classmethod
    def enter_garage(cls):
        os.system('cls' if os.name == 'nt' else 'clear')
        if cls.tracking.spots_available():
            spots = cls.tracking.get_spots()
            print(f"\nWonderful, we have {spots} spot{'s' if spots > 1 else ''} available.")
            time = int(input("\n\nHow many hours will you be parked? "))
            cls.tracking.take_ticket(time)
        else:
            print("Sorry all full. Come back later.")
    @classmethod
    def leave_garage(cls):
        os.system('cls' if os.name == 'nt' else 'clear')
        ticket_number = int(input("What is your ticket number? "))
        if ticket_number in Tracking.current_tickets:
            cls.tracking.pay_ticket(ticket_number)
        else:
            print("Invalid ticket number!")
            lost = input("Did you lose your ticket?: Yes/No ").lower()
            if lost == 'yes':
                cls.tracking.pay_max()
            else:
                cls.leave_garage()


if __name__ == '__main__':

    ParkingGarage.main()





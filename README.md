# Parking_Garage
Built the UI and Ticket Tracking functionality of a parking-lot kiosk

### Run through of the kiosk experience

#### Entering

When entering the kiosk will check to see if there are any available spots.
-if not it prints "Sorry all full" and doesnt issue a ticket

If there are spots available it ask how long you plan to park,   
when answered it will store that data and issue you a ticket whose number is 1 increment higher than the last ticket.

It will then ask you to acknowledge that if you lose the ticket you will be fined.
-If yes screen clears and goes back to home screen
-If no It invalidates your ticket and calls the cops on you.

#### Leaving

When you go to leave the kiosk will ask for your ticket number.

If you enter a ticket number that is not in the active tickets registry it will ask you if you've lost your ticket.
- if yes you will be fined and then allowed to leave
- if no it will prompt you to re-insert your ticket number

Once the correct ticket number has been entered, based on the time you said you would be parked there, it will charge you $5.15 per hour said.

Once paid you are free to leave

#### Management

The manager of the kiosk has a terminal that they can access with their password.

Once inside the manager UI they can check:

Total tickets Issued
Which ticket numbers are active
Total profits

or they can shut the kiosk down, wiping the data from the day


## Work Division





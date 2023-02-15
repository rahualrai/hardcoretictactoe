import serial.tools.list_ports, serial, sys, time

"""
This code is used to control a LED connected to a Arduino board.
It first lists all the available ports and then allows the user to select the desired port to connect to.
After a successful connection, the user is then prompted to enter either a '1' or '0' to turn the LED on or off respectively.
The code then sends the appropriate signal to the board and the LED is turned on or off accordingly.
"""

ports = serial.tools.list_ports.comports()
portsList = []

for i in ports: # make a list of ports
   i = str(i)
   portsList.append(i)
   print(i)

if not portsList: # if no ports are available
   sys.exit("No ports")

val = str(input("\nSelect PORT: COM "))

for x in range(0,len(portsList)):
   if portsList[x].startswith("COM"+val):
      portVar = "COM" + val
      print("connecting to " + portVar)

ttt = serial.Serial(portVar, 9600)

time.sleep(1) # give a little time to establish connection

message = ttt.readline()
print("Connected")
print("\nEnter 1 to get LED ON & 0 to get LED OFF")

LED = False

while True:

   var = input() #get input from user

   if var == "1":
      if LED:
         print("LED is already ON")
      else:
         ttt.write(var.encode())
         LED = True
         print ("LED turned ON")
      time.sleep(0.5)

   elif var == "0":
      if not LED:
         print("LED is already OFF")
      else:
         ttt.write(var.encode())
         LED = False
         print ("LED turned OFF")
      time.sleep(0.5)

   else:
      print("Not a Valid Input")
      print("Enter 1 to get LED ON & 0 to get LED OFF")

   print()
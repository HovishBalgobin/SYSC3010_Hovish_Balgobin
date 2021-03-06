from sense_hat import SenseHat
from time import sleep

"""

  Sense HAT SYSC 3010 lab 2 exercise 1 part (i) 
  
  By Hovish Balgobin
  9/27/2020
  
  Consists of codes to toggle between H and B (my initials) whenever a key is registered \
  form the joystick.

"""


sense = SenseHat()
## creating a variable to make use of the SenseHat in-built functions
sense.clear()
## clearing the display

purple = (148,0,211)
##creating purple using the RGB values

def show_H():
  sense.show_letter("H",back_colour= purple)
  #time.sleep(.5)
  
##function to display H whenever it is called with a purple background.
  
def show_B():
  sense.show_letter("B", back_colour = purple)
  #time.sleep(.5)
  
##function to display B whenever it is called with a purple background.

def repeat(flag):
    if (flag==True):
        show_H()
        
       
    elif(flag==False):
        show_B()
        #flag = True
        
    flag=not(flag)
    return flag

## function used to display the letters and toggle the flag.

    
selection = False    #initialising selection and Flag    
Flag= True;
while True: 
  
  events = sense.stick.get_events()
  for event in events:
    # Skip releases
    if event.action != "released":        
         Flag = repeat(Flag)         
         selection = True
sense.clear()

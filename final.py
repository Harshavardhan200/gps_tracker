from locations import *
import time
list1 = [(15.7981369807174, 78.07836403585469), (15.79729668063069, 78.07760405129781), (15.797241787632668, 78.0775743578153), (15.796960621390312, 78.07747336628034), (15.796924341846738, 78.07767400279646), (15.797135540526392, 78.07700409222842), (15.79687575315547, 78.07691858603702), (15.796631513856962, 78.0768579911135)]
lcd_ = LCD()
lcd_.clear_the_screen()
last_location = "System Rebooted"

Sound.audio(last_location)
lcd_.display(last_location)
time.sleep(2)
lcd_.display("Welcome", pos=(0, 4))
Sound.audio("Welcome")
lcd.home()
while True:
   coordinates = Tracking.track_location()
   location = Locations(coordinates).compare()
   if coordinates == (0.0, 0.0):
        lcd_.display("Connecting...")
        if location != last_location:
            last_location=location
            Sound.audio("Connecting..")
            break
   if location != last_location:
        Sound.audio(location)
        lcd_.display(location)
        last_location=location
    

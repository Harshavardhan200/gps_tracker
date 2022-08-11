from locations import *
import time

list1 = [ (15.797135540526392, 78.07700409222842), (15.79687575315547, 78.07691858603702), (15.796631513856962, 78.0768579911135)]
# while True:
#     coordinates = Tracking.track_location()
#     location = Locations(coordinates).compare()'
print(len(list1))
for i in list1:
    location = Locations(i)
    print(location.compare())
    

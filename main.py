from ride import Ride, Ride_Request, Ride_Matching, Ride_Sharing
from users import Rider, Driver
from vehicle import Car, Bike

ure_jao = Ride_Sharing("Ure Jao")
rahim = Rider("Rahim Uddin", "rahim@gmail.com", 4234234, "Mohakhali", 1200)
ure_jao.add_rider(rahim)
mofizuddin = Driver("Mofiz Uddin", "mofiz@gmail.com", 342343, "Gulshan")
ure_jao.add_driver(mofizuddin)
print(ure_jao)
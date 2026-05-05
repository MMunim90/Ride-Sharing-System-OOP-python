from datetime import datetime
from time import sleep

class Ride_Sharing:
    def __init__(self, company_name):
        self.company_name = company_name
        self.riders = [] # rider database
        self.drivers = [] # drivers database
        self.rides = [] # rides database

    def add_rider(self, rider):
        self.riders.append(rider)

    def add_driver(self, driver):
        self.drivers.append(driver)

    def __str__(self):
        return f"Company Name: {self.company_name} with Riders: {len(self.riders)} and Drivers: {len(self.drivers)}"

class Ride:
    def __init__(self, start_location, end_location):
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None

    def set_driver(self, driver):
        self.driver = driver

    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare

    def __repr__(self):
        return f"Ride details: Strarted From: {self.start_location} To: {self.end_location}. Start At: {self.start_time}, End At: {self.end_time}. Total Paid: {self.estimated_fare}"
    

class Ride_Request:
    def __init__(self, rider, end_location):
        self.rider = rider
        self.end_location = end_location

class Ride_Matching:
    def __init__(self, drivers):
        self.available_drivers = drivers

    def find_driver(self, ride_request):
        if len(self.available_drivers) > 0:
            print("Looking for drivers.....")
            sleep(5)
            driver = self.available_drivers[0]
            ride = Ride(ride_request.rider.current_location, ride_request.end_location)
            driver.accept_ride(ride)
            return ride
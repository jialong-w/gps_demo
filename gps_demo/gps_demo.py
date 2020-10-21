"""Main module."""
import sys
import gps_api

# global variables
name = ""
port = ""
GPS = None
destination = ()

def welcome():
    global name, port
    #put code here to call welcome and menu methods
    print ("__________________________________________________")
    print ("Welcome to the Speeed GPS Demonstrator Application")
    print ("__________________________________________________")
    name = input ("Please enter your name:\n")
    port = input ("Please enter the port you will be using:\n")

def menu():
    print ("1  - View current location")
    print ("2  - Set destination")
    print ("3  - View estimated distance to destination")
    print ("4  - See your estimated time of arrival at your destination")
    print ("5  - View current speed")
    print ("6  - Request your altitude")
    print ("7  - Request your latitude")
    print ("8  - Request your longitude")
    print ("9  - Request date and UTC time")
    print ("0 - Exit the GPS demonstrator application")

def operation():
    option = input ("Please select an option:\n")

    if option == "1":
        location =  GPS.get_current_location()
        print ("Your current location is {}, {}".format(location[0], location[1]))

    elif option == "2":
        set_destination()
        print ("Your destination has been set to {}, {}".format(destination[0], destination[1]))

    elif option == "3":
        if not destination:
            set_destination()
        km = GPS.get_distance(destination[0], destination[1])
        print ("{} km to your destination".format(km))

    elif option == "4":
        if not destination:
            set_destination()
        result = GPS. get_time_of_arrival(destination[0], destination[1])
        if isinstance(result, str):
            print(result)
        else:
            print ("Your estimated time of arrival to {} is {}".format(destination, result))

    elif option == "5":
        speed = GPS.get_speed()
        print ("Your current speed is {} km/h".format(speed))

    elif option == "6":
        altitude = GPS.get_altitude()
        print ("Your altitude is {} metres above sea level".format(altitude))

    elif option == "7":
        lat = GPS.get_latitude()
        print ("Your latitude is {} N".format(lat))

    elif option == "8":
        lon = GPS.get_longitude()
        print ("Your longitude is {} E".format(lon))

    elif option == "9":
        date = GPS.get_date()
        time = GPS.get_UTC_time()
        print ("Date: {}; Time at {} UTC".format(date, time))

    elif option == "0":
        print ("Come back soon {} :)".format(name))
        sys.exit()

    else:
        print("Invalid option.")

def set_destination():
    global dest_latitude, dest_longitude, destination
    dest_latitude = float(input("Please enter in your destination latitude (-90 to 90):\n"))
    dest_longitude = float(input ("Please enter in your destination longitude (-180 to 180):\n"))
    destination = (dest_latitude, dest_longitude)

if __name__ == "__main__":
    try:
        welcome()
        GPS = gps_api.GPS(port)
        while True:
            #create gps here ans pass it into main
            menu()
            operation()
            pass
    except Exception as e:
        print("Error: {}".format(e))

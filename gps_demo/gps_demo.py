"""Main module."""
import sys 
import gps_api

class gps_demo:
     
   
    

    #def getDistanceTravelled(GPS):
        


    
    
    def menu(name,GPS):
        print ("Please select an option:")
        print ("1  - View current location")
        print ("2  - Set destination")
        print ("3  - View distance to destination")
        print ("4  - See your estimated time of arrival at your destination")
        #print ("5  - See how many km you have travelled during this trip")
        print ("6  - View current speed")
        print ("7  - Request your altitude")
        print ("8  - Request your latitude")
        print ("9  - Request your longitude")
        print ("10 - Exit the GPS demonstrator application")
        option = input("Select an option:   \n")

        if option == "1":
            location =  GPS.get_current_location()
            print ("Your current location is " +location)
        elif option == "2":
            latitude = input("Please enter in your destination latitude")
            longitude = input ("Please enter in your destination longitude")
            GPS.set_distination(latitude, longitude)
        elif option == "3":
            if latitude==null or longitude==null:
                latitude = input("Please enter in your destination latitude")
                longitude = input ("Please enter in your destination longitude")
            km = GPS.get_distance(latitude, longitude)
            print (km + " km to your destination")
        elif option == "4":
            if latitude==null or longitude==null:
                latitude = input("Please enter in your destination latitude")
                longitude = input ("Please enter in your destination longitude")
                time = GPS. get_time_of_arrival(latitude, longitude)
            else:
                d = GPS.get_distance()
                time = GPS. get_time_of_arrival()
            print ("Your estimated time of arrival is " + time)
       
        elif option == "6":
            speed = GPS.get_speed()
            print ("Your current speed is: " + speed)
        elif option == "7":
            altitude = GPS.get_altitude()
            print ("Your altitude is: " + altitude)
        elif option == "8":
            lat = GPS.get_latitude()
            print ("Your latitude is: " + lat)
        elif option == "9":
            lon = GPS.get_longitude()
            print ("Your longitude is: " + lon)
        elif option == "10":
            print ("Come back soon "+name+":)")
            sys.exit()
         #elif option == "5":
            #get distance between points 5 seconds away and append to km
            #this must run constantly
           # km += #value between two points every 5 seconds
            #print ("km travelled so far: " + km)


    #put code here to call welcome and menu methods   
    print ("")
    print ("Welcome to the Speeed GPS Demonstartor Application")
    print ("__________________________________________________")
    name = input("Please enter your name: ")
    port = input ("Please enter the port you will be using: ")
    print ("")
    
    try:        
        while True:
            #create gps here ans pass it into main
            GPS = gps_api.GPS(port)
            menu(name, GPS)
            pass
    except Exception as e:
        print(e)
    


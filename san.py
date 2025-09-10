#Author: A.S.M. Damunugalla
#Date: 4.12.2024
#Student ID: w2121298

import csv
from datetime import datetime , timedelta

# Task A: Input Validation
def validate_date_input():
#Date input Validation
    while True:
        try:
            date = int(input("Please enter the date in the foramt dd: "))
            if (date < 1 or date > 31):
                print("Out of range - values must be in the range 1 and 31.")
                continue
            else:
                break
        except ValueError:
            print("Integer required")

#Month input Validation 
    while True:
        try:
            month = int(input("Please enter the month in the format MM: "))
            if (month < 1 or month > 12):
                print("Out of range - values must be in the range 1-12.")
                continue
            else:
                break
        except ValueError:
            print("Integer required")
             
#Year input validation
    while True:
        try:
            year = int(input("Enter the year: "))
            if (year < 2000 or year > 2024):
                print("Out of range  - values must be in the range 2000-2024.")
                continue
            
            else:
                break
        except ValueError:
            print("Integer required")

    valid = str(date)+ "/" + str(month) + "/" + str(year)
    print("The valid date is " , valid)
    return valid


def validate_continue_input():
    continue_input = input("Do you want to select another data file for a different date? Y/N ").lower()
    while True:
        if continue_input == "y":
            return True 

        if continue_input == "n": 
            return False
        else:
            validate_continue_input()


# Task B: Processed Outcomes
def process_data():
    try:
    
        valid = validate_date_input()
        if not valid:
            return
        # Store the three csv files in to variables
        date01 = "traffic_data15062024.csv"
        date02 = "traffic_data16062024.csv"
        date03 = "traffic_data21062024.csv"

        # Select the database
        database = ""
        if valid == "15/6/2024":
            database = date01

        elif valid == "16/6/2024":
            database = date02

        elif valid == "21/6/2024":
            database = date03

        else:
            print("")
      
# Reading the file
        with open("C:\\Users\\Sandes Damunugalla\\Documents\\IIT\\Coursework 1\\" + database, mode='r') as file:
            read = csv.DictReader(file)
            
# The total number of vehicles passing through all junctions for the selected date

            file.seek(0)
            total_number_vehicles = 0
            for row in read:
                total_number_vehicles += 1
            

# The total number of trucks passing through all junctions for the selected date. 

            file.seek(0)
            total_number_trucks = 0
            for row in read:
                if row["VehicleType"] == "Truck":
                    total_number_trucks += 1
            

# The total number of electric vehicles passing through all junctions for the selected date. 

            file.seek(0)
            total_number_electricHybrids = 0
            for row in read:
                if row["elctricHybrid"] == "True":
                    total_number_electricHybrids += 1
           
# The number of “two wheeled” vehicles through all junctions for the date (bikes, motorbike, scooters). 

            file.seek(0)
            total_two_wheels = 0
            for row in read:
                if row["VehicleType"] in ["Bicycle" , "Motorcycle" , "Scooter"]:
                    total_two_wheels += 1
            
# The total number of busses leaving Elm Avenue/Rabbit Road junction heading north

            file.seek(0)
            total_busses_leaving_elmJunction = 0
            for row in read:
                if (row["VehicleType"] == "Buss" and row["JunctionName"] == "Elm Avenue/Rabbit Road" and row["travel_Direction_out"] == "N"):
                    total_busses_leaving_elmJunction += 1
            
# The total number of vehicles passing through both junctions without turning left or right

            file.seek(0)
            total_vehicles_going_straight = 0
            for row in read:
                if  row["travel_Direction_in"] == row["travel_Direction_out"]:
                    total_vehicles_going_straight += 1
            
# The percentage of all vehicles recorded that are Trucks for the selected date 

            file.seek(0)
            percentage_trucks = int(round((total_number_trucks / total_number_vehicles) * 100))
            

# The average number Bicycles per hour for the selected date (rounded to an integer). 

            file.seek(0)
            total_number_bicycles = 0
            for row in read:
                if row["VehicleType"] == "Bicycle":
                    total_number_bicycles += 1
            average_number_bicycles = int(round((total_number_bicycles)/24))
            

#The total number of vehicles recorded as over the speed limit for the selected date.

            file.seek(0)
            vehicles_overTheSpeed = 0
            try:
                for row in read:
                    try:
                        junction_Speed =  int(row["JunctionSpeedLimit"])
                        vehicle_speed = int(row["VehicleSpeed"])
                        if vehicle_speed > junction_Speed:
                            vehicles_overTheSpeed += 1
                    except ValueError:
                        continue
            except Exception as e:
                print("An error occured while processing the file",e)

            except error as e:
             print(e)

# The total number of vehicles recorded through only Elm Avenue/Rabbit Road junction for the selected date.

            file.seek(0)
            total_vehicles_through_Elm = 0
            for row in read:
                if row ["JunctionName"]in["Elm Avenue/Rabbit Road"]:
                    total_vehicles_through_Elm += 1
            

# The total number of vehicles recorded through only Hanley Highway/Westway junction for the selected date.

            file.seek(0)
            total_vehicles_through_hanley = 0
            for row in read:
                if row ["JunctionName"] in ["Hanley Highway/Westway"]:
                    total_vehicles_through_hanley += 1
            

# The percentage of vehicles through Elm Avenue/Rabbit Road that are Scooters

            file.seek(0)
            total_number_scooters = 0
            for row in read:
                if row ["VehicleType"] == "Scooter" and row ["JunctionName"] == "Elm Avenue/Rabbit Road":
                    total_number_scooters += 1
            percentage_scooters_Elm = int((total_number_scooters/total_vehicles_through_Elm)*100)

# The busiest hour in Hanley Avenue
            peak_hours=[]
            maximum_vehicle_count=0
            for current_hour in range(24):
                vehicles_per_hour=0
                file.seek(0)  

                for row in read:
                    if row['JunctionName'] == "Hanley Highway/Westway":
                        row_hour = int((row['timeOfDay']).split(":")[0])
                        if row_hour == current_hour:
                            vehicles_per_hour += 1

                if vehicles_per_hour > maximum_vehicle_count:
                    maximum_vehicle_count = vehicles_per_hour
                    peak_hours = [current_hour]  
                elif vehicles_per_hour == maximum_vehicle_count:
                    peak_hours.append(current_hour)

#the number of hours of rain for this day
            rain_hours_count=0
            for current_hour in range(24):
                file.seek(0)  

                for row in read:
                    if row['Weather_Conditions']== "Heavy Rain" or row['Weather_Conditions']== "Light Rain" :
                        row_hour = int((row['timeOfDay']).split(":")[0])
                        if row_hour == current_hour:
                            rain_hours_count += 1
                            break
                                                    
                                                                       


#Store the outcomes
            output=[database, total_number_vehicles, total_number_trucks, total_number_electricHybrids, total_two_wheels, total_busses_leaving_elmJunction,
                                total_vehicles_going_straight, percentage_trucks, average_number_bicycles, vehicles_overTheSpeed, total_vehicles_through_Elm,
                                        total_vehicles_through_hanley, percentage_scooters_Elm,maximum_vehicle_count,peak_hours,rain_hours_count]
            return output
        
    except FileNotFoundError:
        print(f"Error: The file  does not exist.")


# displaying the outcomes
def display_outcomes(output):

    print("************************************************")
    
    print("The selected data file is " +(output[0]))

    print("************************************************")

    print("The total number of vehicles recorded for this date is " + str(output[1]))

    print("The total number of trucks recorded for this date is " + str(output[2]))
    
    print("The total number of electric vehicles for this date is " + str(output[3]))

    print("The total number of two-wheeled vehicles for this date is " + str(output[4]))
    
    print("The total number of Busses leaving Elm Avenue/Rabbit Road heading North is " + str(output[5]))

    print("The total number of vehicles passing through both junctions without turning left or right is " + str(output[6]))

    print("The percentage of total vehicles recorded that are trucks for this date is %" + str(output[7]))

    print("The average number of Bicycles per hour for this date is"+ str(output[8]))

    print("The total number of vehicles recorded as over the speed limit for this date is " + str(output[9]))

    print("The total number of vehicles recorded through ELm Avenue/Rabbit Road junction is " + str(output[10]))

    print("The total number of vehicles recorded through Hanley Highway/Westway junction is " + str(output[11]))

    print(str(output[12]) + "% of vehicles recorded through Elm Avenue/Rabbit Road are scooters.")
    
    print("The highest number of vehicles in an hour on Hanley Highway/Westway is "+str(output[13]))
    for hour in (output[14]):
        print(f"The most vehicles through Hanley Highway/Westway were recorded between {hour:02}:00 and {hour + 1:02}:00")

    print("The number of hours of rain for this date is "+str(output[15]))


# Task C: Save Results to Text File
def save_results_to_file(output, file_name="results.txt"):
    with open("C:\\Users\\Sandes Damunugalla\\Documents\\IIT\\Coursework 1\\Results.txt", mode = "a") as file:
        file.write("************************************************" + "\n" + "\n")
        file.write("The selected data file is " +(output[0])+ "\n")
        file.write("************************************************" + "\n" + "\n")
        file.write("The total number of vehicles recorded for this date is " + str(output[1])+ "\n")
        file.write("The total number of trucks recorded for this date is " + str(output[2])+ "\n")
        file.write("The total number of electric vehicles for this date is " + str(output[3])+ "\n")
        file.write("The total number of two-wheeled vehicles for this date is " + str(output[4])+ "\n")
        file.write("The total number of Busses leaving Elm Avenue/Rabbit Road heading North is " + str(output[5])+ "\n")
        file.write("The total number of vehicles passing through both junctions without turning left or right is " + str(output[6])+ "\n")
        file.write("The percentage of total vehicles recorded that are trucks for this date is" + str(output[7])+ str("%") + "\n")
        file.write("The average number of Bicycles per hour for this date is"+ str(output[8])+ "\n")
        file.write("The total number of vehicles recorded as over the speed limit for this date is " + str(output[9])+ "\n")
        file.write("The total number of vehicles recorded through ELm Avenue/Rabbit Road junction is " + str(output[10])+ "\n")
        file.write("The total number of vehicles recorded through Hanley Highway/Westway junction is " + str(output[11])+ "\n")
        file.write(str(output[12])+ "% of vehicles recorded through Elm Avenue/Rabbit Road are scooters." + "\n")
        file.write("The highest number of vehicles in an hour on Hanley Highway/Westway is "+str(output[13])+ "\n")
        file.write("The number of hours of rain for this date is "+str(output[15])+"\n")

while True:
    try:
        output = process_data()

        display_outcomes(output)

        save_results_to_file(output, file_name="Results.txt")

        if not(validate_continue_input()):
            break
    except TypeError:
        print("file not found")
        if not(validate_continue_input()):
            break
        

# reference
# https://www.w3schools.com/python/python_string_formatting.asp
# https://www.w3schools.com/python/python_lists.asp


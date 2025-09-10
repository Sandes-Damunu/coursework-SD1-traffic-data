#Author: A.S.M. Damunugalla
#Date: 27.11.2024
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
    print(valid)
    return valid



pass  # Validation logic goes here

def validate_continue_input():
    continue_input = input("Do you want to select another data file for a different date? Y/N ").lower()
    while True:
        if continue_input == "y" or continue_input == "n":
            return continue_input
        else:
            print("Please enter 'Y' or 'N'")


    pass  # Validation logic goes here


# Task B: Processed Outcomes
def process_data():
    
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
      
# 
        with open("C:\\Users\\CHAMA COMPUTERS\\Documents\\Coursework 1\\" + database, mode='r') as file:
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
            

#
'''
            file.seek(0)
            vehicle_count =  {}
            for row in read:
                timeOfDay = datetime.strptime(row["timeOfDay"],"%H:%M:%S")
# Group by hour

                hour = timeOfDay.strftime("%H:00")
                
# increment the count for the respective hour

                if hour not in vehicle_count:
                    vehicle_count[hour] = 0
                vehicle_count[hour] += 1
        
                busiest_hour = max(vehicle_count,key = vehicle_count.get)
                busiest_count = vehicle_count[busiest_hour]
            
'''




# Store the all outcomes in a tuple
                    outputs = [database, total_count, truck_count, electric_vehicles, two_wheeled, heading_north_out_buses,
                       without_turn_left_or_right, avg_percentage_truck, av_bycycle, over_speed, total_Elm_Avenue,
                       total_Hanley_Highway, percentage_Scooters, maximum, start, end,rain_hours]
                      



outcomes= process_data()

    
   
def display_outcomes(outcomes):
    """
    Displays the calculated outcomes in a clear and formatted way.
    """
    pass  # Printing outcomes to the console

    print("The total number of vehicles recorded for this date is" , total_number_vehicles)

    print("The total number of trucks recorded for this date is", total_number_trucks)
    
    print("The total number of electric vehicles for this date is", total_number_electricHybrids)

    print("The total number of two-wheeled vehicles for this date is", total_two_wheels)
    
    print("The total number of Busses leaving Elm Avenue/Rabbit Road heading North is", total_busses_leaving_elmJunction)

    print("The total number of vehicles passing through both junctions without turning left or right is", total_vehicles_going_straight)

    print("The percentage of total vehicles recorded that are trucks for this date is {}%".format (percentage_trucks))

    print("The average number of Bicycles per hour for this date is", average_number_bicycles)

    print("The total number of vehicles recorded as over the speed limit for this date is", vehicles_overTheSpeed)

    print("The total number of vehicles recorded through ELm Avenue/Rabbit Road junction is" , total_vehicles_through_Elm)

    print("The total number of vehicles recorded through Hanley Highway/Westway junction is" , total_vehicles_through_hanley)

    print( "{}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters.".format(percentage_scooters_Elm))

    
# Task C: Save Results to Text File
def save_results_to_file(outcomes, file_name="results.txt"):
    
    """
    Saves the processed outcomes to a text file and appends if the program loops.
    """
    pass  # File writing logic goes here

# if you have been contracted to do this assignment please do not remove this line

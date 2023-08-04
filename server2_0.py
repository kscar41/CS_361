import os

def print_car_log_data(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            car_log_data = file.read()
        new_file_name = "carDatabase.txt"

        with open(new_file_name, "w") as new_file:
            new_file.write("Car Log Data:\n")
            new_file.write(car_log_data)

        print("Car log data has been written to:", new_file_name)
    else:
        print("Car Log does not exist.")

def find_car_log():
    while True:
        car_type = input("Enter the Year, Make, and Model of the car: ")

        if car_type.lower() == "exit":
            print("Exiting...")
            break

        if not car_type:
            print("Invalid input.")
            continue

        car_log = car_type.replace(" ", ".")
        file_name = car_log + ".txt"
        print_car_log_data(file_name)

if __name__ == "__main__":
    find_car_log()

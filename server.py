import os

def print_car_log_data(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            car_log_data = file.read()
            print("Car Log Data:")
            print(car_log_data)
    else:
        print("Car Log does not exist.")

def find_car_log():
    car_type = input("Enter the Year, Make, and Model of the car: ")

    if not car_type:
        print("Invalid input.")
        return

    car_log = car_type.replace(" ", ".")
    file_name = car_log + ".txt"

    print_car_log_data(file_name)

if __name__ == "__main__":
    find_car_log()

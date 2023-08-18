import os
import threading
import time

def find_car_log():
    check_search = open('begin_search.txt', 'r')
    with check_search:
        check = check_search.read().lower()
        check_search.close()
        if check == 'prepare for search':
            file = open('begin_search.txt', 'w')
            file.close()
            car = open('data_file.txt', 'r')
            with car:
                car_info = car.read().lower()
                database_needed = str(car_info).replace(' ', '.')
                info = open(database_needed + '.txt')
                car_log = info.read()
                return_file = open('data_file.txt', 'w')
                return_file.write(str(car_log))

def interval_function():
    while True:
        find_car_log()
        time.sleep(3)
interval_thread = threading.Thread(target=interval_function)
interval_thread.start()

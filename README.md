The microservive implemented for my partners project will allow users to search for a particular car through the make, model and year. once the car the user has requested is found the user will be returned with the particular maintenance done on the vehicle along with when the maintenance was added as well as the mileage at time of service.
How to programmatically REQUEST data: the user will be prompted upon running server and client files to enter the car they are enquiring about. 
  Example: Enter the Year, Make, and Model of the car: will be prompted on the server CL for the user to enter
How to programmatically RECEIVE data: the microservice will search the database in the client file and if or when a match is found all information pertaining to the vehical in question will present its self to the user.
  Example:  Enter the Year, Make, and Model of the car: 2022 Toyota Tacoma
            Car Log Data:
            2022 Toyota Tacoma car log created! Date Created: 2023-07-28
            Completed on: 2023-07-31
            Maintenance Type: oil change
            Mileage Performed at: 150000

UML sequence diagram:

client(main) program -> user adds carr entry -> car is added to database.txt
               -> user adds maintenance work -> work is added to car_log + .txt

microservice program -> user enters car data -> request from car_log.txt -> entry is compared to database.txt -> match -> reads car_log.txt -> returns current data to user                                                                                                          -> no match -> returns "no car found" to user

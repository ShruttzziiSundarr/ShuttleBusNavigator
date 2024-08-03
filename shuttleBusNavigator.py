import mysql.connector
import sys


connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="123456",
    database="bus_management"
)


if connection.is_connected():
    print("Connection Successful\n")
else:
    print("Connection is not successful.")
    sys.exit()


cursor = connection.cursor()


def bus_details_add():
    bus_number = input("Enter the bus number: ")
    driver_name = input("Enter the driver's name: ")
    route = input("Enter the bus route: ")
    timings = input("Enter the bus timings: ")
    query = "INSERT INTO bus_details (bus_number, driver_name, route, timings) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (bus_number, driver_name, route, timings))
    connection.commit()
    print("Bus details added successfully.")


def bus_details_update():
    bus_number = input("Enter the bus number to update: ")
    query = "SELECT * FROM bus_details WHERE bus_number = %s"
    cursor.execute(query, (bus_number,))
    bus = cursor.fetchone()
    if not bus:
        print("Bus not found.")
        return


    new_driver_name = input("Enter the new driver's name (or press Enter to leave it unchanged): ")
    new_route = input("Enter the new bus route (or press Enter to leave it unchanged): ")
    new_timings = input("Enter the new bus timings (or press Enter to leave it unchanged): ")


    new_driver_name = new_driver_name if new_driver_name else bus[1]
    new_route = new_route if new_route else bus[2]
    new_timings = new_timings if new_timings else bus[3]


    update_query = "UPDATE bus_details SET driver_name = %s, route = %s, timings = %s WHERE bus_number = %s"
    cursor.execute(update_query, (new_driver_name, new_route, new_timings, bus_number))
    connection.commit()
    print("Bus details updated successfully.")


def bus_details_delete():
    bus_number = input("Enter the bus number to delete: ")
    query = "SELECT * FROM bus_details WHERE bus_number = %s"
    cursor.execute(query, (bus_number,))
    bus = cursor.fetchone()
    if not bus:
        print("Bus not found.")
        return


    delete_query = "DELETE FROM bus_details WHERE bus_number = %s"
    cursor.execute(delete_query, (bus_number,))
    connection.commit()
    print("Bus deleted successfully.")


def create_student_account():
    username = input("Enter the student username: ")
    password = input("Enter the student password: ")
    query = "INSERT INTO student (username, password) VALUES (%s, %s)"
    cursor.execute(query, (username, password))
    connection.commit()
    print("Student account created successfully.")


def update_student_account():
    username = input("Enter the student username to update: ")
    query = "SELECT * FROM student WHERE username = %s"
    cursor.execute(query, (username,))
    student = cursor.fetchone()
    if not student:
        print("Student not found.")
        return


    new_password = input("Enter the new password (or press Enter to leave it unchanged): ")


    new_password = new_password if new_password else student[1]


    update_query = "UPDATE student SET password = %s WHERE username = %s"
    cursor.execute(update_query, (new_password, username))
    connection.commit()
    print("Student account updated successfully.")


def delete_student_account():
    username = input("Enter the student username to delete: ")
    query = "SELECT * FROM student WHERE username = %s"
    cursor.execute(query, (username,))
    student = cursor.fetchone()
    if not student:
        print("Student not found.")
        return


    delete_query = "DELETE FROM student WHERE username = %s"
    cursor.execute(delete_query, (username,))
    connection.commit()
    print("Student account deleted successfully.")


def add_driver_details():
    driver_name = input("Enter the driver's name: ")
    driver_id = input("Enter the driver ID: ")
    driver_mobile = input("Enter the driver's mobile number: ")
    query = "INSERT INTO drivers (driver_name, driver_id, driver_mobile) VALUES (%s, %s, %s)"
    cursor.execute(query, (driver_name, driver_id, driver_mobile))
    connection.commit()
    print("Driver details added successfully.")


def update_driver_details():
    driver_id = input("Enter the driver ID to update: ")
    query = "SELECT * FROM drivers WHERE driver_id = %s"
    cursor.execute(query, (driver_id,))
    driver = cursor.fetchone()
    if not driver:
        print("Driver not found.")
        return


    new_driver_name = input("Enter the new driver's name (or press Enter to leave it unchanged): ")
    new_driver_mobile = input("Enter the new driver's mobile number (or press Enter to leave it unchanged): ")


    new_driver_name = new_driver_name if new_driver_name else driver[1]
    new_driver_mobile = new_driver_mobile if new_driver_mobile else driver[3]


    update_query = "UPDATE drivers SET driver_name = %s, driver_mobile = %s WHERE driver_id = %s"
    cursor.execute(update_query, (new_driver_name, new_driver_mobile, driver_id))
    connection.commit()
    print("Driver details updated successfully.")


def delete_driver_details():
    driver_id = input("Enter the driver ID to delete: ")
    query = "SELECT * FROM drivers WHERE driver_id = %s"
    cursor.execute(query, (driver_id,))
    driver = cursor.fetchone()
    if not driver:
        print("Driver not found.")
        return


    delete_query = "DELETE FROM drivers WHERE driver_id = %s"
    cursor.execute(delete_query, (driver_id,))
    connection.commit()
    print("Driver details deleted successfully.")


def admin_login():
    username = input("Enter your admin username: ")
    password = input("Enter your admin password: ")
    query = "SELECT username FROM admin WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    if result:
        print("\nAdmin Login successful. Welcome, admin!\n")
        while True:
            print("1- Add Bus Details")
            print("2- Update Bus Details")
            print("3- Delete Bus Details")
            print("4- Add Driver Details")
            print("5- Update Driver Details")
            print("6- Delete Driver Details")
            print("7- Create Student Account")
            print("8- Update Student Account")
            print("9- Delete Student Account")
            print("10- Logout")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                bus_details_add()
            elif choice == 2:
                bus_details_update()
            elif choice == 3:
                bus_details_delete()
            elif choice == 4:
                add_driver_details()
            elif choice == 5:
                update_driver_details()
            elif choice == 6:
                delete_driver_details()
            elif choice == 7:
                create_student_account()
            elif choice == 8:
                update_student_account()
            elif choice == 9:
                delete_student_account()
            elif choice == 10:
                sys.exit("Logged out")
            else:
                print("Invalid choice.")
            print("\n")
    else:
        print("Login failed. Please check your username and password.")


def student_login():
    username = input("Enter your student username: ")
    password = input("Enter your student password: ")
    query = "SELECT username FROM student WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    if result:
        print("\nStudent Login successful. Welcome, student!\n")
        student_specific_actions()
    else:
        print("Login failed. Please check your username and password.")


def student_specific_actions():
    while True:
        print("1- View Bus Schedule")
        print("2- Logout")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            view_bus_schedule()
        elif choice == 2:
            sys.exit("Logged out")
        else:
            print("Invalid choice.")


def view_bus_schedule():
    print("+--------------------------------------------------+")
    print("|                 Bus Schedule                     |")
    print("+--------------------------------------------------+\n")
    query = "SELECT bus_number, driver_name, route, timings FROM bus_details"
    cursor.execute(query)
    schedules = cursor.fetchall()
    if not schedules:
        print("No bus schedule available.")
    else:
        for schedule in schedules:
            bus_number, driver_name, route, timings = schedule
            print(f"Bus Number: {bus_number}")
            print(f"Driver: {driver_name}")
            print(f"Route: {route}")
            print(f"Timings: {timings}")
            print("-" * 20)


def driver_login():
    driver_id = input("Enter your driver ID: ")
    query = "SELECT driver_name FROM drivers WHERE driver_id = %s"
    cursor.execute(query, (driver_id,))
    result = cursor.fetchone()
    if result:
        print(f"\nDriver Login successful. Welcome, {result[0]}!\n")
        driver_specific_actions(driver_id)
    else:
        print("Login failed. Please check your driver ID.")


def driver_specific_actions(driver_id):
    while True:
        print("1- View Assigned Bus")
        print("2- Logout")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            view_assigned_bus(driver_id)
        elif choice == 2:
            sys.exit("Logged out")
        else:
            print("Invalid choice.")


def view_assigned_bus(driver_id):
    query = "SELECT bus_number, route FROM bus_details WHERE driver_name = (SELECT driver_name FROM drivers WHERE driver_id = %s)"
    cursor.execute(query, (driver_id,))
    assigned_buses = cursor.fetchall()
    if not assigned_buses:
        print("You are not currently assigned to any buses.")
    else:
        print("Assigned Buses:")
        for assigned_bus in assigned_buses:
            bus_number, route = assigned_bus
            print(f"Bus Number: {bus_number}")
            print(f"Route: {route}")
            print("-" * 20)


print("+--------------------------------------------------+")
print("|            Bus Management System                 |")
print("+--------------------------------------------------+\n")
print("1- ADMIN LOGIN")
print("2- STUDENT LOGIN")
print("3- DRIVER LOGIN")
print("4- Exit")
print("Emergency number: 123456789")


choice = int(input("Enter your choice: "))
print("\n")


if choice == 1:
    admin_login()
elif choice == 2:
    student_login()
elif choice == 3:
    driver_login()
elif choice == 4:
    sys.exit("Exiting")
cursor.close()
connection.close()

# ShuttleBusNavigator
The Bus management system that connects to a MySQL database for managing various aspects of a bus service. It offers separate functionalities for administrators, students, and drivers. Users can log in with their respective roles and access role-specific features.



# Shuttle Bus Navigator System

## Overview

The Shuttle Bus Navigator System is a comprehensive management tool designed to streamline operations related to buses, drivers, students, and administrators. This system provides functionalities for adding, updating, and deleting bus details and driver information, as well as managing student accounts. It includes user authentication for admins, students, and drivers, each with tailored functionalities.

The system uses a MySQL database to store essential information such as bus schedules, user credentials, and driver details. The project aims to enhance the organization and efficiency of managing shuttle bus operations through a user-friendly interface.

## Objectives

1. **Database Management:**
   - Create and manage tables in a MySQL database to store information about buses, drivers, students, and administrators.

2. **User Authentication:**
   - Implement authentication mechanisms for administrators, students, and drivers to access the system.

3. **Administrator Actions:**
   - Add, update, and delete bus details.
   - Add, update, and delete driver information.
   - Create, update, and delete student accounts.

4. **Student Actions:**
   - Log in to view bus schedules.

5. **Driver Actions:**
   - Log in to view assigned buses.

6. **User-Friendly Menu:**
   - Provide a menu-driven interface for easy navigation.

7. **Security:**
   - Ensure secure login for users.

8. **Logging Out:**
   - Allow users to log out and protect their sessions.

9. **Emergency Number:**
   - Display an emergency contact number.

10. **Exiting the System:**
    - Provide a way to exit the system gracefully.

11. **Displaying Information:**
    - Show relevant information such as bus schedules and assigned buses.

12. **Structured Database:**
    - Maintain a well-structured MySQL database.

## Database Schema

### Tables

1. **Bus Details**

    ```sql
    CREATE TABLE bus_details (
        bus_number VARCHAR(10) PRIMARY KEY,
        driver_name VARCHAR(30),
        route VARCHAR(255),
        timings VARCHAR(255)
    );
    ```

2. **Admin**

    ```sql
    CREATE TABLE admin (
        username VARCHAR(20) PRIMARY KEY,
        password VARCHAR(20)
    );
    ```

3. **Student**

    ```sql
    CREATE TABLE student (
        username VARCHAR(20) PRIMARY KEY,
        password VARCHAR(20)
    );
    ```

4. **Drivers**

    ```sql
    CREATE TABLE drivers (
        driver_id VARCHAR(10) PRIMARY KEY,
        driver_name VARCHAR(30),
        driver_mobile VARCHAR(15)
    );
    ```



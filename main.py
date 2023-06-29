import sqlite3

import sqlite3

class ReservationManagementSubsystem:
    database_path = "path/to/database.db"

    @classmethod
    def create_reservation(cls):
        # Retrieve user input for reservation details
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        from_date = input("Enter the check-in date (YYYY-MM-DD): ")
        to_date = input("Enter the check-out date (YYYY-MM-DD): ")

        # Prompt user to select single or double room
        room_type = input("Select room type (1 for Single, 2 for Double): ")
        if room_type == "1":
            room_type = "Single"
        elif room_type == "2":
            room_type = "Double"
        else:
            print("Invalid room type selection.")
            return

        # Prompt user to select room subtype based on the selected room type
        if room_type == "Single":
            room_subtype = input("Select room subtype (1 for King, 2 for Queen): ")
            if room_subtype == "1":
                room_subtype = "King"
            elif room_subtype == "2":
                room_subtype = "Queen"
            else:
                print("Invalid room subtype selection.")
                return
        else:
            room_subtype = None

        # Connect to the SQLite database
        connection = sqlite3.connect(cls.database_path)
        cursor = connection.cursor()

        # Check room availability based on the selected room type and dates
        availability_query = """
            SELECT COUNT(*) FROM reservations 
            WHERE room_type = ? AND date >= ? AND date <= ? AND available = 1
        """
        cursor.execute(availability_query, (room_type, from_date, to_date))
        available_rooms_count = cursor.fetchone()[0]

        if available_rooms_count > 0:
            # Insert reservation details into the database
            insert_query = """
                INSERT INTO reservations (first_name, last_name, room_type, room_subtype, date, available) 
                VALUES (?, ?, ?, ?, ?, 0)
            """
            cursor.execute(insert_query, (first_name, last_name, room_type, room_subtype, from_date))
            reservation_id = cursor.lastrowid

            # Commit the changes
            connection.commit()

            # Display confirmation number and reservation summary
            print("Reservation confirmed successfully.")
            print("Confirmation number:", reservation_id)
            print("Reservation summary:",first_name, last_name,room_type)
            if room_subtype:
                print("Room Subtype:", room_subtype)
            print("Check-in Date:", from_date)
            print("Check-out Date:", to_date)
        else:
            # No available rooms for the selected dates and room type
            print("No available rooms for the selected dates and room type.")

        # Close the connection
        connection.close()


    @classmethod
    def modify_reservation(cls):
        # Retrieve user input for reservation ID and modified details

        # Connect to the SQLite database
        connection = sqlite3.connect(cls.database_path)
        cursor = connection.cursor()

        # Update the reservation details in the database
        # Execute appropriate SQL statements

        # Commit the changes and close the connection
        connection.commit()
        connection.close()

        print("Reservation modified successfully.")

    @classmethod
    def cancel_reservation(cls):
        # Retrieve user input for reservation ID

        # Connect to the SQLite database
        connection = sqlite3.connect(cls.database_path)
        cursor = connection.cursor()

        # Delete the reservation from the database
        # Execute appropriate SQL statements

        # Commit the changes and close the connection
        connection.commit()
        connection.close()

        print("Reservation canceled successfully.")

    @classmethod
    def view_reservation(cls):
        # Retrieve user input for reservation ID

        # Connect to the SQLite database
        connection = sqlite3.connect(cls.database_path)
        cursor = connection.cursor()

        # Retrieve the reservation details from the database based on the ID
        # Execute appropriate SQL statements

        # Display the reservation details

        # Close the connection
        connection.close()

    # Rest of the class

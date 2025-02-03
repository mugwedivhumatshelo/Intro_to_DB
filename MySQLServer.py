import mysql.connector

def create_database():
    try:
        # Establish a connection to the MySQL server
        db = mysql.connector.connect(
            host="localhost",
            use="root",
            password="Futureeits@2021"
        )

        # Create a cursor object to execute SQL queries
        cursor = db.cursor()

        # Create the database if it does not exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        # Print a success message
        print("Database 'alx_book_store' created successfully!")

        # Close the cursor and connection
        cursor.close()
        db.close()

    except mysql.connector.Error as err:
        # Print an error message if the connection fails
        print(f"Error connecting to the MySQL server: {err}")

if __name__ == "__main__":
    create_database()

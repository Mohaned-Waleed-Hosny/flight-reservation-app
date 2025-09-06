import sqlite3
import os

def create_connection():
    """Create a database connection to the SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect('flights.db')
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table():
    """Create reservations table if it doesn't exist"""
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS reservations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    flight_number TEXT NOT NULL,
                    departure TEXT NOT NULL,
                    destination TEXT NOT NULL,
                    date TEXT NOT NULL,
                    seat_number TEXT NOT NULL
                )
            ''')
            conn.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()

def add_reservation(name, flight_number, departure, destination, date, seat_number):
    """Add a new reservation to the database"""
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (name, flight_number, departure, destination, date, seat_number))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()
    return None

def get_all_reservations():
    """Get all reservations from the database"""
    conn = create_connection()
    reservations = []
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM reservations ORDER BY date DESC')
            reservations = cursor.fetchall()
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()
    return reservations

def get_reservation_by_id(reservation_id):
    """Get a specific reservation by ID"""
    conn = create_connection()
    reservation = None
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM reservations WHERE id = ?', (reservation_id,))
            reservation = cursor.fetchone()
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()
    return reservation

def update_reservation(reservation_id, name, flight_number, departure, destination, date, seat_number):
    """Update an existing reservation"""
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE reservations 
                SET name = ?, flight_number = ?, departure = ?, destination = ?, date = ?, seat_number = ?
                WHERE id = ?
            ''', (name, flight_number, departure, destination, date, seat_number, reservation_id))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()
    return False

def delete_reservation(reservation_id):
    """Delete a reservation from the database"""
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM reservations WHERE id = ?', (reservation_id,))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()
    return False

# Initialize the database when this module is imported
create_table()
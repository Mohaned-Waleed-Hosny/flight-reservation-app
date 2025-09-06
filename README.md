# Flight Reservation System

A desktop application for managing flight reservations built with Python, Tkinter, and SQLite.

## Features

- ✈️ Book new flights with complete details
- 📋 View all existing reservations in a table format
- ✏️ Edit existing reservation information
- 🗑️ Delete/cancel reservations
- 🔍 Search through reservations
- 💾 Local SQLite database storage

## Files Included

- `main.py` - Main application file
- `database.py` - SQLite database operations
- `home.py` - Home page UI
- `booking.py` - Flight booking form
- `reservations.py` - Reservations list view
- `edit_reservation.py` - Edit reservation functionality
- `requirements.txt` - Python dependencies
- `flights.db` - SQLite database file
- `main.exe` - Windows executable
- `README.md` - This documentation file
- `user_guide.pdf` - Complete user guide

## Installation

### Option 1: Run from Source Code

1. Ensure Python 3.6+ is installed
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```

### Option 2: Use the Executable (Windows)

1. Double-click `main.exe` to launch the application
2. No installation or dependencies required

## How to Use

1. **Launch the application** (run `main.py` or double-click `main.exe`)
2. **Book a Flight**: Click "Book Flight" and fill in the form
3. **View Reservations**: Click "View Reservations" to see all bookings
4. **Manage Bookings**: Use edit/delete buttons for each reservation
5. **Search**: Use the search box to filter reservations

## Database Information

- Uses SQLite database (`flights.db`)
- Automatically creates necessary tables
- Stores all reservation data locally
- No internet connection required

## Building the Executable

To create your own executable:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

The executable will be created in the `dist` folder.

## Notes

- All files are in the same directory for simplicity
- The application creates and uses `flights.db` automatically
- No external dependencies besides Python standard libraries

## Created By

Mohaned Waleed

## License

Educational use only.

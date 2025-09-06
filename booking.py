import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from database import add_reservation

class BookingPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#f0f8ff")
        
        # Create main container with scrollbar
        main_container = tk.Frame(self, bg="#f0f8ff")
        main_container.pack(fill="both", expand=True)
        
        # Canvas and scrollbar for responsiveness
        canvas = tk.Canvas(main_container, bg="#f0f8ff", highlightthickness=0)
        scrollbar = ttk.Scrollbar(main_container, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#f0f8ff")
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Title
        title_label = tk.Label(
            scrollable_frame,
            text="Book a Flight",
            font=("Arial", 24, "bold"),
            fg="#2c3e50",
            bg="#f0f8ff"
        )
        title_label.pack(pady=(20, 30))
        
        # Form container
        form_frame = tk.Frame(scrollable_frame, bg="#f0f8ff", padx=40, pady=20)
        form_frame.pack()
        
        # Full Name field
        name_frame = tk.Frame(form_frame, bg="#f0f8ff")
        name_frame.pack(fill="x", pady=10)
        
        name_label = tk.Label(
            name_frame,
            text="Full Name",
            font=("Arial", 12, "bold"),
            fg="#2c3e50",
            bg="#f0f8ff"
        )
        name_label.pack(anchor="w", pady=(0, 5))
        
        self.name_entry = ttk.Entry(
            name_frame,
            font=("Arial", 12),
            width=40
        )
        self.name_entry.pack(fill="x", pady=(0, 5))
        
        name_hint = tk.Label(
            name_frame,
            text="Enter your full name",
            font=("Arial", 10),
            fg="#7f8c8d",
            bg="#f0f8ff"
        )
        name_hint.pack(anchor="w")
        
        # Flight Number field
        flight_frame = tk.Frame(form_frame, bg="#f0f8ff")
        flight_frame.pack(fill="x", pady=10)
        
        flight_label = tk.Label(
            flight_frame,
            text="Flight Number",
            font=("Arial", 12, "bold"),
            fg="#2c3e50",
            bg="#f0f8ff"
        )
        flight_label.pack(anchor="w", pady=(0, 5))
        
        self.flight_entry = ttk.Entry(
            flight_frame,
            font=("Arial", 12),
            width=40
        )
        self.flight_entry.pack(fill="x", pady=(0, 5))
        
        flight_hint = tk.Label(
            flight_frame,
            text="e.g. 55123",
            font=("Arial", 10),
            fg="#7f8c8d",
            bg="#f0f8ff"
        )
        flight_hint.pack(anchor="w")
        
        # Departure field
        departure_frame = tk.Frame(form_frame, bg="#f0f8ff")
        departure_frame.pack(fill="x", pady=10)
        
        departure_label = tk.Label(
            departure_frame,
            text="Departure",
            font=("Arial", 12, "bold"),
            fg="#2c3e50",
            bg="#f0f8ff"
        )
        departure_label.pack(anchor="w", pady=(0, 5))
        
        self.departure_entry = ttk.Entry(
            departure_frame,
            font=("Arial", 12),
            width=40
        )
        self.departure_entry.pack(fill="x", pady=(0, 5))
        
        departure_hint = tk.Label(
            departure_frame,
            text="e.g. New York",
            font=("Arial", 10),
            fg="#7f8c8d",
            bg="#f0f8ff"
        )
        departure_hint.pack(anchor="w")
        
        # Destination field
        destination_frame = tk.Frame(form_frame, bg="#f0f8ff")
        destination_frame.pack(fill="x", pady=10)
        
        destination_label = tk.Label(
            destination_frame,
            text="Destination",
            font=("Arial", 12, "bold"),
            fg="#2c3e50",
            bg="#f0f8ff"
        )
        destination_label.pack(anchor="w", pady=(0, 5))
        
        self.destination_entry = ttk.Entry(
            destination_frame,
            font=("Arial", 12),
            width=40
        )
        self.destination_entry.pack(fill="x", pady=(0, 5))
        
        destination_hint = tk.Label(
            destination_frame,
            text="e.g. London",
            font=("Arial", 10),
            fg="#7f8c8d",
            bg="#f0f8ff"
        )
        destination_hint.pack(anchor="w")
        
        # Date field
        date_frame = tk.Frame(form_frame, bg="#f0f8ff")
        date_frame.pack(fill="x", pady=10)
        
        date_label = tk.Label(
            date_frame,
            text="Date",
            font=("Arial", 12, "bold"),
            fg="#2c3e50",
            bg="#f0f8ff"
        )
        date_label.pack(anchor="w", pady=(0, 5))
        
        self.date_entry = ttk.Entry(
            date_frame,
            font=("Arial", 12),
            width=40
        )
        self.date_entry.pack(fill="x", pady=(0, 5))
        
        date_hint = tk.Label(
            date_frame,
            text="Pick a date (YYYY-MM-DD)",
            font=("Arial", 10),
            fg="#7f8c8d",
            bg="#f0f8ff"
        )
        date_hint.pack(anchor="w")
        
        # Seat Number field
        seat_frame = tk.Frame(form_frame, bg="#f0f8ff")
        seat_frame.pack(fill="x", pady=10)
        
        seat_label = tk.Label(
            seat_frame,
            text="Seat Number",
            font=("Arial", 12, "bold"),
            fg="#2c3e50",
            bg="#f0f8ff"
        )
        seat_label.pack(anchor="w", pady=(0, 5))
        
        self.seat_entry = ttk.Entry(
            seat_frame,
            font=("Arial", 12),
            width=40
        )
        self.seat_entry.pack(fill="x", pady=(0, 5))
        
        seat_hint = tk.Label(
            seat_frame,
            text="e.g. 12A",
            font=("Arial", 10),
            fg="#7f8c8d",
            bg="#f0f8ff"
        )
        seat_hint.pack(anchor="w")
        
        # Button frame
        button_frame = tk.Frame(form_frame, bg="#f0f8ff", pady=30)
        button_frame.pack(fill="x")
        
        # Style for buttons
        style = ttk.Style()
        style.configure("Book.TButton", font=("Arial", 12), padding=10)
        
        cancel_btn = ttk.Button(
            button_frame,
            text="Cancel",
            style="Book.TButton",
            command=self.cancel_booking
        )
        cancel_btn.pack(side="left", padx=10)
        
        book_btn = ttk.Button(
            button_frame,
            text="Book Flight",
            style="Book.TButton",
            command=self.submit_booking
        )
        book_btn.pack(side="right", padx=10)
        
        # Bind mouse wheel to canvas for scrolling
        canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))
    
    def cancel_booking(self):
        self.controller.show_frame("HomePage")
    
    def submit_booking(self):
        # Get form data
        name = self.name_entry.get().strip()
        flight_number = self.flight_entry.get().strip()
        departure = self.departure_entry.get().strip()
        destination = self.destination_entry.get().strip()
        date = self.date_entry.get().strip()
        seat_number = self.seat_entry.get().strip()
        
        # Validate form data
        if not all([name, flight_number, departure, destination, date, seat_number]):
            messagebox.showerror("Error", "Please fill in all fields")
            return
        
        # Validate date format
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid date in YYYY-MM-DD format")
            return
        
        # Add reservation to database
        reservation_id = add_reservation(name, flight_number, departure, destination, date, seat_number)
        
        if reservation_id:
            messagebox.showinfo("Success", f"Flight booked successfully! Reservation ID: {reservation_id}")
            self.clear_form()
            self.controller.show_frame("HomePage")
        else:
            messagebox.showerror("Error", "Failed to book flight. Please try again.")
    
    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.flight_entry.delete(0, tk.END)
        self.departure_entry.delete(0, tk.END)
        self.destination_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.seat_entry.delete(0, tk.END)
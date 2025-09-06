import tkinter as tk
from tkinter import ttk, messagebox
from database import get_all_reservations, delete_reservation

class ReservationsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#f0f8ff")
        
        # Create main container
        main_container = tk.Frame(self, bg="#f0f8ff", padx=20, pady=20)
        main_container.pack(fill="both", expand=True)
        
        # Title
        title_label = tk.Label(
            main_container,
            text="Your Reservations",
            font=("Arial", 24, "bold"),
            fg="#2c3e50",
            bg="#f0f8ff"
        )
        title_label.pack(pady=(0, 20))
        
        # Search and action frame
        search_frame = tk.Frame(main_container, bg="#f0f8ff")
        search_frame.pack(fill="x", pady=(0, 20))
        
        search_label = tk.Label(
            search_frame,
            text="Search reservations:",
            font=("Arial", 10),
            fg="#34495e",
            bg="#f0f8ff"
        )
        search_label.pack(side="left", padx=(0, 10))
        
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(
            search_frame,
            textvariable=self.search_var,
            font=("Arial", 10),
            width=30
        )
        search_entry.pack(side="left", padx=(0, 20))
        search_entry.bind("<KeyRelease>", self.filter_reservations)
        
        book_btn = ttk.Button(
            search_frame,
            text="Book New Flight",
            command=lambda: controller.show_frame("BookingPage")
        )
        book_btn.pack(side="right")
        
        # Reservations table frame
        table_frame = tk.Frame(main_container, bg="#f0f8ff")
        table_frame.pack(fill="both", expand=True)
        
        # Create treeview with scrollbar
        columns = ("id", "name", "flight_number", "departure", "destination", "date", "seat_number")
        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            selectmode="browse",
            height=15
        )
        
        # Define headings
        self.tree.heading("id", text="ID")
        self.tree.heading("name", text="Name")
        self.tree.heading("flight_number", text="Flight Number")
        self.tree.heading("departure", text="Departure")
        self.tree.heading("destination", text="Destination")
        self.tree.heading("date", text="Date")
        self.tree.heading("seat_number", text="Seat Number")
        
        # Define column widths
        self.tree.column("id", width=50, anchor="center")
        self.tree.column("name", width=150, anchor="w")
        self.tree.column("flight_number", width=100, anchor="center")
        self.tree.column("departure", width=120, anchor="w")
        self.tree.column("destination", width=120, anchor="w")
        self.tree.column("date", width=100, anchor="center")
        self.tree.column("seat_number", width=80, anchor="center")
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Pack treeview and scrollbar
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Button frame
        button_frame = tk.Frame(main_container, bg="#f0f8ff", pady=20)
        button_frame.pack(fill="x")
        
        # Style for buttons
        style = ttk.Style()
        style.configure("Res.TButton", font=("Arial", 10), padding=5)
        
        view_btn = ttk.Button(
            button_frame,
            text="View Details",
            style="Res.TButton",
            command=self.view_details
        )
        view_btn.pack(side="left", padx=5)
        
        edit_btn = ttk.Button(
            button_frame,
            text="Edit",
            style="Res.TButton",
            command=self.edit_reservation
        )
        edit_btn.pack(side="left", padx=5)
        
        delete_btn = ttk.Button(
            button_frame,
            text="Delete",
            style="Res.TButton",
            command=self.delete_reservation
        )
        delete_btn.pack(side="left", padx=5)
        
        refresh_btn = ttk.Button(
            button_frame,
            text="Refresh",
            style="Res.TButton",
            command=self.load_reservations
        )
        refresh_btn.pack(side="left", padx=5)
        
        home_btn = ttk.Button(
            button_frame,
            text="Back to Home",
            style="Res.TButton",
            command=lambda: controller.show_frame("HomePage")
        )
        home_btn.pack(side="right", padx=5)
        
        # Load reservations
        self.all_reservations = []
        self.load_reservations()
    
    def load_reservations(self):
        # Clear treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Get reservations from database
        self.all_reservations = get_all_reservations()
        
        # Add reservations to treeview
        for reservation in self.all_reservations:
            self.tree.insert("", "end", values=reservation)
        
        # Show message if no reservations
        if not self.all_reservations:
            self.tree.insert("", "end", values=("", "No Reservations Found", "", "", "", "", ""))
    
    def filter_reservations(self, event):
        search_term = self.search_var.get().lower()
        
        # Clear treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Filter reservations
        filtered_reservations = [
            r for r in self.all_reservations 
            if search_term in str(r).lower()
        ]
        
        # Add filtered reservations to treeview
        for reservation in filtered_reservations:
            self.tree.insert("", "end", values=reservation)
        
        # Show message if no reservations match
        if not filtered_reservations and search_term:
            self.tree.insert("", "end", values=("", "No matching reservations", "", "", "", "", ""))
    
    def get_selected_reservation(self):
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a reservation")
            return None
        
        item = self.tree.item(selection[0])
        reservation_id = item["values"][0]
        
        # Check if it's a valid reservation (not a message row)
        if not reservation_id:
            return None
        
        return reservation_id
    
    def view_details(self):
        reservation_id = self.get_selected_reservation()
        if reservation_id:
            # In a real app, you might show a detailed view
            messagebox.showinfo("Info", f"Viewing details for reservation #{reservation_id}")
    
    def edit_reservation(self):
        reservation_id = self.get_selected_reservation()
        if reservation_id:
            self.controller.frames["EditReservationPage"].load_reservation(reservation_id)
            self.controller.show_frame("EditReservationPage")
    
    def delete_reservation(self):
        reservation_id = self.get_selected_reservation()
        if reservation_id:
            if messagebox.askyesno("Confirm", "Are you sure you want to delete this reservation?"):
                if delete_reservation(reservation_id):
                    messagebox.showinfo("Success", "Reservation deleted successfully")
                    self.load_reservations()
                else:
                    messagebox.showerror("Error", "Failed to delete reservation")
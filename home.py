import tkinter as tk
from tkinter import ttk, font

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#f0f8ff")
        
        # Create main container
        container = tk.Frame(self, bg="#f0f8ff", padx=20, pady=20)
        container.pack(expand=True, fill="both")
        
        # Welcome section
        welcome_frame = tk.Frame(container, bg="#f0f8ff")
        welcome_frame.pack(pady=(0, 30))
        
        title_label = tk.Label(
            welcome_frame, 
            text="Welcome to FlySky Reservations",
            font=("Arial", 24, "bold"),
            fg="#2c3e50",
            bg="#f0f8ff"
        )
        title_label.pack(pady=(0, 15))
        
        desc_label = tk.Label(
            welcome_frame,
            text="Book your flights and manage your reservations with our simple and intuitive system.",
            font=("Arial", 12),
            fg="#34495e",
            bg="#f0f8ff",
            wraplength=600
        )
        desc_label.pack(pady=(0, 20))
        
        # Separator
        separator = ttk.Separator(welcome_frame, orient="horizontal")
        separator.pack(fill="x", pady=10)
        
        # Book Flight section
        book_frame = tk.Frame(container, bg="#f0f8ff")
        book_frame.pack(pady=(0, 20))
        
        book_title = tk.Label(
            book_frame,
            text="Book a Flight",
            font=("Arial", 16, "bold"),
            fg="#2c3e50",
            bg="#f0f8ff"
        )
        book_title.pack(anchor="w", pady=(0, 10))
        
        book_desc = tk.Label(
            book_frame,
            text="Reserve your next flight by providing your details and flight information.",
            font=("Arial", 10),
            fg="#7f8c8d",
            bg="#f0f8ff",
            wraplength=600,
            justify="left"
        )
        book_desc.pack(anchor="w", pady=(0, 15))
        
        # Separator
        separator2 = ttk.Separator(book_frame, orient="horizontal")
        separator2.pack(fill="x", pady=10)
        
        # View Reservations section
        view_frame = tk.Frame(container, bg="#f0f8ff")
        view_frame.pack(pady=(0, 20))
        
        view_title = tk.Label(
            view_frame,
            text="View Reservations",
            font=("Arial", 16, "bold"),
            fg="#2c3e50",
            bg="#f0f8ff"
        )
        view_title.pack(anchor="w", pady=(0, 10))
        
        view_desc = tk.Label(
            view_frame,
            text="Manage your existing reservations, view details, edit or cancel if needed.",
            font=("Arial", 10),
            fg="#7f8c8d",
            bg="#f0f8ff",
            wraplength=600,
            justify="left"
        )
        view_desc.pack(anchor="w", pady=(0, 15))
        
        # Separator
        separator3 = ttk.Separator(view_frame, orient="horizontal")
        separator3.pack(fill="x", pady=10)
        
        # Button section
        button_frame = tk.Frame(container, bg="#f0f8ff")
        button_frame.pack(pady=30)
        
        # Style for buttons
        style = ttk.Style()
        style.configure("Home.TButton", font=("Arial", 12), padding=10)
        
        book_btn = ttk.Button(
            button_frame,
            text="Book Flight",
            style="Home.TButton",
            command=lambda: controller.show_frame("BookingPage")
        )
        book_btn.pack(side="left", padx=20)
        
        view_btn = ttk.Button(
            button_frame,
            text="View Reservations",
            style="Home.TButton",
            command=lambda: controller.show_frame("ReservationsPage")
        )
        view_btn.pack(side="left", padx=20)
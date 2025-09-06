import tkinter as tk
from tkinter import ttk
from home import HomePage
from booking import BookingPage
from reservations import ReservationsPage
from edit_reservation import EditReservationPage

class FlightReservationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Configure main window
        self.title("FlySky Reservations")
        self.geometry("1000x700")
        self.minsize(800, 600)
        
        # Configure style
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        # Create container for frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        # Initialize frames
        self.frames = {}
        for F in (HomePage, BookingPage, ReservationsPage, EditReservationPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        # Show home page initially
        self.show_frame("HomePage")
    
    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = FlightReservationApp()
    app.mainloop()
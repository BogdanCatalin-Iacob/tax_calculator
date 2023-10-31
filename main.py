'''
Tax calculator
'''
import customtkinter as ctk


class TaxCalculator:
    def __init__(self):
        # Initialize the window
        self.window = ctk.CTk()
        self.window.title('Tax Calculator')
        self.window.geometry('280x200')  # size of the window
        self.window.resizable(False, False)

        # Define the padding
        self.padding: dict = {'padx': 20, 'pady': 10}

        # Income label and input
        self.income_label = ctk.CTkLabel(self.window, text='Income:')
        self.income_label.grid(row=0, column=0, **self.padding)

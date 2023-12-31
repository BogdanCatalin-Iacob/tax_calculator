'''
Tax calculator
'''
import customtkinter as ctk


class TaxCalculator:
    '''
    Define the calculator window
    '''
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
        self.income_input = ctk.CTkEntry(self.window)
        self.income_input.grid(row=0, column=1, **self.padding)

        # Tax label and input
        self.tax_label = ctk.CTkLabel(self.window, text='Tax rate (%):')
        self.tax_label.grid(row=1, column=0, **self.padding)
        self.tax_input = ctk.CTkEntry(self.window)
        self.tax_input.grid(row=1, column=1, **self.padding)

        # Resul label and input
        self.result_label = ctk.CTkLabel(self.window, text='Result:')
        self.result_label.grid(row=2, column=0, **self.padding)
        self.result_input = ctk.CTkEntry(self.window)
        self.result_input.insert(0, '0')  # inserd default value
        self.result_input.grid(row=2, column=1, **self.padding)

        # Calculate button
        self.calculate_button = ctk.CTkButton(
            self.window, text='Calculate', command=self.calculate_tax)
        self.calculate_button.grid(row=3, column=1, **self.padding)

    def update_result(self, text: str):
        self.result_input.delete(0, ctk.END)
        self.result_input.insert(0, text)

    def calculate_tax(self):
        '''
        Calculate the tax ammount based on income and tax percentage inputs
        '''
        try:
            income: float = float(self.income_input.get())
            tax_rate: float = float(self.tax_input.get())
            # ':,' place a comma separator to make the number easy to read
            self.update_result(f'{income * (tax_rate / 100):,.2f}')
        except ValueError:
            self.update_result('Invalid input')

    def run(self):
        '''
        Run without ending the program
        '''
        self.window.mainloop()


if __name__ == '__main__':
    tax_calc = TaxCalculator()
    tax_calc.run()

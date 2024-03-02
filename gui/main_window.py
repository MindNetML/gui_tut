import customtkinter as ctk
from gui.cashamount import CashAmountDialog

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Personal Finance Tracker")
        self.geometry("600x400")  # Set the window size
        self.create_widgets()

    def create_widgets(self):
        # Expenses label
        self.expenses = ctk.CTkLabel(self, text="Expense Amount: ")
        self.expenses.grid(column=0, row=0, padx=10, pady=(20, 5))

        # Expenses entry
        self.expenses_entry = ctk.CTkEntry(self)
        self.expenses_entry.grid(column=0, row=1, padx=10, pady=5)

        # Button to submit expenses
        self.submit_button = ctk.CTkButton(self, text="Submit Expense", command=self.submit_expense)
        self.submit_button.grid(column=0, row=2, padx=10, pady=20)

        # Current money label, placed on the right of the expense entry and label, in the same row as the expenses label
        self.current_money = ctk.CTkLabel(self, text="Current Money: ")
        self.current_money.grid(column=1, row=0, padx=10, pady=(20, 5))

        # money entry
        self.money_entry = ctk.CTkEntry(self)
        self.money_entry.grid(column=1, row=1, padx=10, pady=5)

        # Button to submit money
        self.submit_moneybutton = ctk.CTkButton(self, text="Money", command=self.submit_expense)
        self.submit_moneybutton.grid(column=1, row=2, padx=10, pady=20)


        # Button to open the pop-up for entering cash amount
        self.add_cash_button = ctk.CTkButton(self, text="Add Cash Amount", command=self.open_cash_dialog)
        self.add_cash_button.grid(column=2, row=0, padx=10, pady=(20, 5), sticky="ew")

        # Label to display the cash amount
        self.cash_amount_label = ctk.CTkLabel(self, text="Cash Amount: $0")
        self.cash_amount_label.grid(column=2, row=1, padx=10, pady=5, sticky="ew")

        # Configure the grid columns
        # self.grid_columnconfigure(0, weight=1)  # Allow column 0 to expand more than column 1
        # self.grid_columnconfigure(1, weight=3)  # Column 1 takes less space

    def open_cash_dialog(self):
        dialog = CashAmountDialog(self)
        self.wait_window(dialog)  # Wait for the dialog to close

        # Update the cash amount label with the value entered in the dialog
        if dialog.cash_amount:
            self.cash_amount_label.configure(text=f"Cash Amount: ${dialog.cash_amount}")


    def submit_expense(self):
        # Placeholder function to get the value from the entry and print it
        amount = self.expenses_entry.get()
        print(f"Submitting Expense: {amount}")

    

import customtkinter as ctk
from gui.cashamount import CashAmountDialog
from gui.Expenses import ExpensesAmountDialog

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Personal Finance Tracker")
        self.geometry("600x400")  # Set the window size
        self.create_widgets()

    def create_widgets(self):
        # Create a frame for the buttons
        buttons_frame = ctk.CTkFrame(self)
        buttons_frame.pack(side='left', padx=10, pady=10, fill='y', anchor='nw')

        # Button to open the pop-up for entering cash amount
        self.add_cash_button = ctk.CTkButton(buttons_frame, text="Add Cash Amount", command=self.open_cash_dialog)
        self.add_cash_button.pack(side='top', fill='x', padx=0, pady=3)

        # Button to open the pop-up for entering expense amount
        self.add_expense_button = ctk.CTkButton(buttons_frame, text="Add Expense", command=self.submit_expense)
        self.add_expense_button.pack(side='top', fill='x', padx=0, pady=3)

        # Label to display the cash amount, positioned in the main window, not in the frame
        self.cash_amount_label = ctk.CTkLabel(self, text="Cash Amount: $0")
        self.cash_amount_label.pack(side='top', padx=0, pady=0, after=buttons_frame)

        # Add listbox, positioned in the main window, to take the remaining space
        self.listbox = ctk.CTkTextbox(self)
        self.listbox.pack(side='right', fill='both', expand=True, padx=0, pady=0)


    def open_cash_dialog(self):
        dialog = CashAmountDialog(self)
        self.wait_window(dialog)  # Wait for the dialog to close

        # Update the cash amount label with the value entered in the dialog
        if dialog.cash_amount:
            self.cash_amount_label.configure(text=f"Cash Amount: ${dialog.cash_amount}")


    def submit_expense(self):
        dialog = ExpensesAmountDialog(self)
        self.wait_window(dialog)
        if dialog.expense_amount:
            # Format the entry as "Amount - Description"
            entry_text = f"{dialog.expense_amount} - {dialog.expense_description}"
            self.listbox.insert("end", entry_text)



    

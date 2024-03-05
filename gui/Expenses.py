import customtkinter as ctk

class ExpensesAmountDialog(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Enter expense Amount")
        self.geometry("250x100")  # Adjust the size as needed

        # Textbox for entering the expense description
        self.expense_description_entry = ctk.CTkEntry(self)
        self.expense_description_entry.pack()

        # Textbox for entering the expense amount
        self.expense_amount_entry = ctk.CTkEntry(self)
        self.expense_amount_entry.pack()

        # Submit button
        self.submit_button = ctk.CTkButton(self, text="Submit", command=self.submit_expense_amount)
        self.submit_button.pack()

        self.cash_amount = None

    def submit_expense_amount(self):
        # Get the expense amount from the entry and store it
        self.expense_amount = self.expense_amount_entry.get()
        self.destroy()

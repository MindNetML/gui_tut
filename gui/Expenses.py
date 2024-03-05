import customtkinter as ctk

class ExpensesAmountDialog(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Enter Expense Amount")
        self.geometry("250x100")

        self.expense_description_entry = ctk.CTkEntry(self)
        self.expense_description_entry.pack()

        self.expense_amount_entry = ctk.CTkEntry(self)
        self.expense_amount_entry.pack()

        self.submit_button = ctk.CTkButton(self, text="Submit", command=self.submit_expense_amount)
        self.submit_button.pack()

        self.expense_amount = ""  # Initialize as empty string
        self.expense_description = ""  # Initialize as empty string

    def submit_expense_amount(self):
        # Fetch and store the expense description and amount
        self.expense_description = self.expense_description_entry.get()
        self.expense_amount = self.expense_amount_entry.get()
        self.destroy()

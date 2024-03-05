import customtkinter as ctk

class CashAmountDialog(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Enter Cash Amount")
        self.geometry("250x100")  # Adjust the size as needed

        # Textbox for entering the cash amount
        self.cash_amount_entry = ctk.CTkEntry(self)
        self.cash_amount_entry.pack(pady=(5))

        # Submit button
        self.submit_button = ctk.CTkButton(self, text="Submit", command=self.submit_cash_amount)
        self.submit_button.pack()

        self.cash_amount = None

    def submit_cash_amount(self):
        # Get the cash amount from the entry and store it
        self.cash_amount = self.cash_amount_entry.get()
        self.destroy()  # Close the dialog

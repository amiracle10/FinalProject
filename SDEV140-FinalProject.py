# author: Alex Miracle
# IDE: Visual Studio Code


# pseudo code:
# initialize income and expense trackers
# display the home screen where the user can view total income, expenses, remaining balance, and navigate to other options
# provide functionality to add income by prompting the user to input an amount, category, and description
# save the user's income input, update the total income, and return to the home screen
# provide functionality to add an expense by prompting the user to input an amount, category, and description
# save the user's expense input, update total expenses, and return to the home screen
# allow users to export a summary of their total income, expenses, and remaining balance to an Excel file
# ensure the interface clears any existing widgets on the screen when switching between screens


import tkinter as tk
from tkinter import ttk



class BudgetTrackerApp:
    def __init__ (self,root):
        self.root = root
        self.root.title("Budget Tracker App")

        # initialize income and expense trackers
        self.total_income = 0
        self.total_expenses = 0

        self.create_home_screen()

    # create the home screen with a summary of the user's financial status
    def create_home_screen(self):
        self.clear_screen()

        # display summary of income, expense, and remaining balance
        tk.Label(self.root, text ="Welcome to the Budget Tracker App").pack(pady=10)
        tk.Label(self.root, text=f"Total Income: ${self.total_income}").pack()
        tk.Label(self.root, text=f"Total Expenses: ${self.total_expenses}").pack()
        tk.Label(self.root, text=f"Remaining Balance: ${self.total_income - self.total_expenses}").pack()

        # navigation buttons for different sections
        tk.Button(self.root, text="Add Income", command=self.create_add_income_screen).pack(pady=5)
        tk.Button(self.root, text="Add Expense", command=self.create_add_expense_screen).pack(pady=5)
        tk.Button(self.root, text="Export to Excel", command=self.export_to_excel).pack(pady=5)
        # tk.Button(self.root, text="Settings", command=self.create_settings_screen).pack(pady=5)

    # screen to add income details
    def create_add_income_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Add Income").pack(pady=10)

        tk.Label(self.root, text="Amount:").pack()
        income_amount_entry = tk.Entry(self.root)
        income_amount_entry.pack()

        tk.Label(self.root, text="Category:").pack()
        category_options = ["Salary", "Freelance", "Other"]
        category_dropdown = ttk.Combobox(self.root, values=category_options)
        category_dropdown.pack()

        tk.Label(self.root, text="Description:").pack()
        description_entry = tk.Entry(self.root)
        description_entry.pack()

        tk.Button(self.root, text="Save", command=lambda: self.save_income(income_amount_entry, category_dropdown, description_entry)).pack(pady=5)
        tk.Button(self.root, text="Cancel", command=self.create_home_screen).pack(pady=5)

    def save_income(self, amount_entry, category_dropdown, description_entry):
        amount = amount_entry.get()
        try: 
            amount = float(amount)
            self.total_income += amount  
        except ValueError:
            print("Invalid amount, please enter a number.")
            return

        category = category_dropdown.get()
        description = description_entry.get()
        print(f"Income: {amount}, {category}, {description}")

        # update the home screen with new total income
        self.create_home_screen()


    # screen to add expense details
    def create_add_expense_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Add Expense").pack(pady=10)

        tk.Label(self.root, text="Amount:").pack()
        expense_amount_entry = tk.Entry(self.root)
        expense_amount_entry.pack()

        tk.Label(self.root, text="Category:").pack()
        category_options = ["Rent", "Food", "Entertainment", "Utilities", "Other"]
        category_dropdown = ttk.Combobox(self.root, values=category_options)
        category_dropdown.pack()

        tk.Label(self.root, text="Description:").pack()
        description_entry = tk.Entry(self.root)
        description_entry.pack()

        tk.Button(self.root, text="Save", command=lambda: self.save_expense(expense_amount_entry, category_dropdown, description_entry)).pack(pady=5)
        tk.Button(self.root, text="Cancel", command=self.create_home_screen).pack(pady=5)

    
    def save_expense(self, amount_entry, category_dropdown, description_entry):
        amount = amount_entry.get()

        try:
            amount = float(amount)
            self.total_expenses += amount  # update total expenses
        except ValueError:
            print("Invalid amount, please enter a number.")
            return
    
        category = category_dropdown.get()
        description = description_entry.get()

        print(f"Expense: {amount}, {category}, {description}")

        # after saving, update the home screen with new total expenses
        self.create_home_screen()

    def export_to_excel(self):
        import os
        import pandas as pd

        # print("Current Working Directory:", os.getcwd())

        # create a DataFrame 
        # fix to add individual incomes/expense
        data = {
                "Income": [self.total_income],
                "Expenses": [self.total_expenses],
                "Remaining Balance": [self.total_income - self.total_expenses]
        }
        
        df = pd.DataFrame(data)
        
        # export to excel
        df.to_excel('budget_report.xlsx', index=False)
        print("Data exported to budget_report.xlsx")


   
    # settings screen 
    # def create_settings_screen(self):
    #     self.clear_screen()
    #     tk.Label(self.root, text="Settings").pack(pady=10)
    #     tk.Label(self.root, text="Coming Soon").pack(pady=5)

    #     tk.Button(self.root, text="Back", command=self.create_home_screen).pack(pady=5)

    # clear all widgets on the screen
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# create root window
root = tk.Tk()
root.geometry("400x400")

# run app
app = BudgetTrackerApp(root)
root.mainloop()
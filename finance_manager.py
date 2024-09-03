from transaction import Transaction
import matplotlib.pyplot as plt
import csv

class FinanceManager:
    def __init__(self):
        self.transactions = []
        self.current_transactions = []
        self.categories = {
            "1": "Salary",
            "2": "Rent",
            "3": "Entertainment",
            "4": "Utilities",
            "5": "Miscellaneous"
        }
        
    def print_choices(self):
        print("1. Add Transaction\n")
        print("2. Get total income\n")
        print("3. Get total expense\n")
        print("4. Get net savings\n")
        print("5. Print categories\n")
        print("6. Visualise Expense\n")
        print("7. Save report\n")
        print("8. Print current transactions\n")
        print("9. Print previous transactions\n")
        print("0. Exit Program\n")
        
    def add_transaction(self, transaction):
        self.current_transactions.append(transaction)
        
    def save_to_file(self, filename="data/transactions.csv"):
        with open(filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            for t in self.current_transactions:
                writer.writerow([t.amount, t.category, t.date, t.description]) # transaction
                
    def load_from_file(self, filename="data/transactions.csv"):
        with open(filename, mode="r") as file:
            reader = csv.reader(file)
            next(reader) # Skipping the columns
            for r in reader:
                transaction = Transaction(*r)
                self.transactions.append(transaction)
            
    def get_total_income(self):
        total = 0
        for t in self.transactions:
            if (t.amount > 0):
                total += t.amount
        for t in self.current_transactions:
            if (t.amount > 0):
                total += t.amount
        return total
    
    def get_total_expense(self):
        total = 0
        for t in self.transactions:
            if (t.amount < 0):
                total += t.amount    
        for t in self.current_transactions:
            if (t.amount < 0):
                total += t.amount
        return abs(total)
    
    def print_previous_transactions(self, filename="data/transactions.csv"):
        with open(filename, mode="r") as file:
            reader = csv.reader(file)
            next(reader) # Skipping the columns
            for r in reader:
                t = Transaction(*r)
                transaction_str = f"Amount: {t.amount}. Category: {t.category}. Date: {t.date}. Description: {t.description}"
                print(transaction_str)

    
    def print_current_transactions(self):
        for t in self.current_transactions:
            transaction_str = f"Amount: {t.amount}. Category: {t.category}. Date: {t.date}. Description: {t.description}"
            print(transaction_str)
    
    def get_net_savings(self):
        profitOrLoss = self.get_total_income() - self.get_total_expense()
        return profitOrLoss  
    
    def print_categories(self):
        print("Select a category:")
        for key, value in self.categories.items():
            print(f"{key}. {value}")
  
    def save_report(self, filename="reports/summary.csv"):
        with open(filename, mode='w') as file:
            writer = csv.writer(file)
            writer.writerow(["Total Expense", "Total Income", "Profit/Loss"])
            totalExpense = self.get_total_expense()
            totalIncome = self.get_total_income()
            profitLoss = totalIncome - totalExpense
            writer.writerow([totalExpense, totalIncome, profitLoss])  
    
    def visualiseExpense(self):
        categoryAmount = {} 
        for t in self.transactions:
            if (t.amount < 0):
                previousValue = categoryAmount.get(t.category, 0)
                categoryAmount[t.category] = t.amount + previousValue
                
        for t in self.current_transactions:
            if (t.amount < 0):
                previousValue = categoryAmount.get(t.category, 0)
                categoryAmount[t.category] = t.amount + previousValue
                
        categories = categoryAmount.keys()
        amount = categoryAmount.values()
        
        plt.pie([abs(a) for a in amount], labels=categories)
        plt.title("Expense for each category")      
        plt.show()

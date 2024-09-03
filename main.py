from transaction import Transaction
from finance_manager import FinanceManager


finance_manager = FinanceManager()
finance_manager.load_from_file()

print("Welcome to our perosnal finance manager\n")
print("Please select an option\n")

finance_manager.print_choices()

choice = "_"

while (choice != "0"):
    choice = input("Enter your choice\n")
    if(choice == "1"):
        finance_manager.print_categories()
        
        print("\n")
        
        category_choice = input("Enter category number\n")
        category = finance_manager.categories.get(category_choice, 'Miscellaneous')
        
        expenseOrIncome = input("Press e for Expense or i for Income\n")
        
        amount = float(input("Enter amount\n"))
        description = input("Enter description\n")
        date = input("Enter date in this format: YYYY-MM-DD\n")
        
        if(expenseOrIncome == "e"):
            amount = -amount
        
        transaction = Transaction(amount, category, date, description)
        
        finance_manager.add_transaction(transaction)
        print(f"New transaction has been added\n {transaction}")
        
    elif(choice == "2"):
        print(f"Total income is: {finance_manager.get_total_income()}")
        
    elif(choice == "3"):
        print(f"Total expense is: {finance_manager.get_total_expense()}")
        
    elif(choice == "4"):
        print(f"Net savings is: {finance_manager.get_net_savings()}")
        
    elif(choice == "5"):
        finance_manager.print_categories()
        
        print("\n")
        
    elif(choice == "6"):
        finance_manager.visualiseExpense()
        
    elif(choice == "7"):
        finance_manager.save_report()
        print("Report saved")
        
    elif(choice == "8"):
        finance_manager.print_current_transactions()
        
    elif(choice == "9"):
        finance_manager.print_previous_transactions()
        
    elif(choice == "0"):
        print("Saving transactions to file\n")
        finance_manager.save_to_file()
        print("Transactions saved to file\n")
        print("Exiting program")
        break
        
    else:
        print('Invalid input\n')
        finance_manager.print_choices()
        choice = input("Enter your choice\n")
        
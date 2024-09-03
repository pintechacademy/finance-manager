class Transaction:
    def __init__(self, amount, category, date, description = "New Transaction"):
        self.amount = float(amount)
        self.category = category
        self.date = date
        self.description = description
        
    def __str__(self):
        return f"{self.date} - {self.category}: {self.amount} ({self.description})"
1
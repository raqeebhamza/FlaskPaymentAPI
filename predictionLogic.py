class predictGateway():
    def predict(amount):
        if amount <= 20:
            return f"CheapPaymentGateway  ->>>   transaction of  {amount} has done successfully!"
        elif 21 <= amount <= 500:
            return f"ExpensivePaymentGateway  ->>>   transaction of  {amount} has done successfully!"
        else:
            return f"PremiumPaymentGateway  ->>>   transaction of  {amount} has done successfully!"